import fitz
import docx
import json
import jsonlines
from tqdm import tqdm
import time
import validators
from bs4 import BeautifulSoup
import requests
import openai
import numpy as np
from numpy.linalg import norm
import os
import hashlib
import tiktoken
tokenizer = tiktoken.get_encoding("cl100k_base")
with open("openai_api_key.txt", 'r', encoding='utf8') as f:
	openai.api_key = f.readlines()[0].strip()
print("Loaded openai api key.")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def get_text(text_path):
	url = text_path
	suffix = os.path.splitext(text_path)[-1]
	if validators.url(url):
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			soup = BeautifulSoup(response.content, "html.parser")
			text = soup.get_text()
		else:
			raise ValueError(f"Invalid URL! Status code {response.status_code}.")
	elif suffix == ".pdf":
		full_text = ""
		num_pages = 0
		with fitz.open(text_path) as doc:
			for page in doc:
				num_pages += 1
				text = page.get_text()
				full_text += text + "\n"
		text = f"This is a {num_pages}-page document.\n" + full_text
	elif ".doc" in suffix:
		doc = docx.Document(text_path)
		fullText = []
		for para in doc.paragraphs:
			fullText.append(para.text)
		text = '\n'.join(fullText)
	elif suffix == ".txt":
		with open(text_path, 'r', encoding='utf8') as f:
			lines = f.readlines()
		text = '\n'.join(lines)
	else:
		raise ValueError("Invalid document path!")
	text = " ".join(text.split())
	return text

def get_embedding(text, model="text-embedding-ada-002"):
	text = text.replace("\n", " ")
	return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

def get_summary(chunk):
	content = "The following is a passage fragment. Please summarize what information the readers can take away from it:"

	content += "\n" + chunk

	messages = [
				{"role": "user", "content": content}
			]
	summary = chatGPT_api(messages).content

	return summary

def store_info(text, memory_path, chunk_sz = 700, max_memory = 100):
	info = []
	text = text.replace("\n", " ").split()
	# raise error if the anticipated api usage is too massive
	if (len(text) / chunk_sz) >= max_memory:
		raise ValueError("Processing is aborted due to high anticipated costs.")
	for idx in tqdm(range(0, len(text), chunk_sz)):
		chunk = " ".join(text[idx: idx + chunk_sz])
		if len(tokenizer.encode(chunk)) > chunk_sz * 3:
			print("Skipped an uninformative chunk.")
			continue
		attempts = 0
		while True:
			try:
				summary = get_summary(chunk)
				embd = get_embedding(chunk)
				summary_embd = get_embedding(summary)
				item = {
					"id": len(info),
					"text": chunk,
					"embd": embd,
					"summary": summary,
					"summary_embd": summary_embd,
				}
				info.append(item)
				time.sleep(3)  # up to 20 api calls per min
				break
			except Exception as e:
				attempts += 1
				if attempts >= 3:
					raise Exception(f"{str(e)}")
				time.sleep(3)
	with jsonlines.open(memory_path, mode="w") as f:
		f.write(info)
		print(f"Finish storing info in {memory_path}")

def get_question():
	q = input("Enter your question: ")
	return q

def load_info(memory_path):
	with open(memory_path, 'r', encoding='utf8') as f:
		for line in f:
			info = json.loads(line)
	return info

def retrieve(q_embd, info):
	# return the indices of top three related texts
	text_embds = []
	summary_embds = []
	for item in info:
		text_embds.append(item["embd"])
		summary_embds.append(item["summary_embd"])
	# compute the cos sim between info_embds and q_embd
	text_cos_sims = np.dot(text_embds, q_embd) / (norm(text_embds, axis=1) * norm(q_embd))
	summary_cos_sims = np.dot(summary_embds, q_embd) / (norm(summary_embds, axis=1) * norm(q_embd))
	cos_sims = text_cos_sims + summary_cos_sims
	top_args = np.argsort(cos_sims).tolist()
	top_args.reverse()
	indices = top_args[0:3]
	return indices

def chatGPT_api(messages):
	completion = openai.ChatCompletion.create(
	model = 'gpt-3.5-turbo',
	messages=messages,
	temperature = 1,
	top_p = 0.95,
	# max_tokens=2000,
	frequency_penalty = 0.0,
	presence_penalty = 0.0
	)

	return completion.choices[0].message

def get_qa_content(q, retrieved_text):
	content = "After reading some relevant passage fragments from the same document, please respond to the following query. Note that there may be typographical errors in the passages due to the text being fetched from a PDF file or web page."

	content += "\nQuery: " + q

	for i in range(len(retrieved_text)):
		content += "\nPassage " + str(i + 1) + ": " + retrieved_text[i]

	content += "\nAvoid explicitly using terms such as 'passage 1, 2 or 3' in your answer as the questioner may not know how the fragments are retrieved. Please use the same language as in the query to respond."

	return content

def generate_answer(q, retrieved_indices, info):
	while True:
		sorted_indices = sorted(retrieved_indices)
		retrieved_text = [info[idx]["text"] for idx in sorted_indices]
		content = get_qa_content(q, retrieved_text)
		if len(tokenizer.encode(content)) > 3800:
			retrieved_indices = retrieved_indices[:-1]
			print("Contemplating...")
			if not retrieved_indices:
				raise ValueError("Failed to respond.")
		else:
			break
	messages = [
		{"role": "user", "content": content}
	]
	answer = chatGPT_api(messages).content
	return answer

def memorize(text):
	sha = hashlib.sha256(text.encode('UTF-8')).hexdigest()
	memory_path = f"memory/{sha}.json"
	file_exists = os.path.exists(memory_path)
	if file_exists:
		print(f"Detected cached memories in {memory_path}")
	else:
		print("Memorizing...")
		store_info(text, memory_path)
	return memory_path

def answer(q, info):
	q_embd = get_embedding(q, model="text-embedding-ada-002")
	retrieved_indices = retrieve(q_embd, info)
	answer = generate_answer(q, retrieved_indices, info)
	return answer

def chat(memory_path):
	info = load_info(memory_path)
	while True:
		q = get_question()
		if len(tokenizer.encode(q)) > 200:
			raise ValueError("Input query is too long!")
		attempts = 0
		while True:
			try:
				response = answer(q, info)
				print()
				print(f"{bcolors.OKGREEN}{response}{bcolors.ENDC}")
				print()
				time.sleep(3) # up to 20 api calls per min
				break
			except Exception as e:
				attempts += 1
				if attempts >= 3:
					raise Exception(f"{str(e)}")
				time.sleep(3)
