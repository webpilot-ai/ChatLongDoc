# ChatLongDoc

## Welcome to this project

This project surpasses the length constraints of using OpenAI Chat-LLMs, such as ChatGPT, enabling you to converse with long documents. It expedites comprehension of the content and facilitates the acquisition of valuable insights. Compared with ChatPDF, it accommodates various file formats, including PDF, doc, docx, and web URLs. The implementation of this project is straightforward to follow, expand, and efficient for integration into other applications.

## Dependencies

Please execute the following command in the terminal to install the required dependencies:

Python>=3.8

```shell
cd ChatLongDoc
pip install -r requirements.txt
```

## Usage

In the **demo.ipynb**, we provide a simple and clear procedure:

1. Please replace the first line of the `./openai_api_key.txt` file with the OpenAI API Key you want to use. It will be read when the dependencies are loaded.
2. Enter the local file path or web URL you want to chat with. The pdf, doc, docx, and txt formats are currently supported. You can also try the `./example/example.pdf` that we provide for toturial. The sample file is the paper [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
3. Memorize the content of the document or web page it read. The memorized information will be stored in `./memory`, where already includes the memory file of the trial document we provide.
4. Enter your question and start chatting with the document.

## 欢迎使用本项目

这个项目突破了使用OpenAI Chat-LLMs（如ChatGPT）的长度限制，使您能够与长文档进行对话。帮助对内容的理解，便于获取有价值的见解。与ChatPDF相比，它支持包括PDF、doc、docx和Web URL在内的各种文件格式。该项目的实现简单易懂，易于扩展，并且能够高效地集成到其他应用程序中。

## 环境依赖

请在终端中执行以下命令，安装所需依赖：

Python>=3.8

```shell
cd ChatLongDoc
pip install -r requirements.txt
```

## 使用流程

在 **demo.ipynb** 中我们给出了简单明了的使用步骤：

1. 请先将 `./openai_api_key.txt` 文件中的第一行替换成您想要使用的 OpenAI API Key，在 demo 加载依赖的过程中会读取。
2. 输入您想要了解的本地文档地址或网页 URL，文档格式目前支持 pdf、doc、docx、txt。也可以使用我们提供的 `./example/example.pdf` 进行试用，样例文件为论文 [Attention Is All You Need](https://arxiv.org/abs/1706.03762)。
3. 记忆所读取的文档或网页内容，记忆后的信息会存储在 `./memory` 中，其中已经包含了我们提供的试用文档的记忆信息文件。
4. 输入问题，开始和文档聊天吧。
