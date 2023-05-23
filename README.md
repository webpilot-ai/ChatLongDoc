# ChatLongDoc

## Welcome to this project

This project surpasses the length constraints of using OpenAI Chat-LLMs, such as ChatGPT, enabling you to converse with any long document. It expedites comprehension of the content and facilitates the acquisition of valuable insights. Compared with ChatPDF, it accommodates various file formats, including PDF, doc, docx, txt, and web URLs. The implementation of this project is straightforward to follow, expand, and efficient for integration into other applications.

You are welcome to check our [ChatGPT plugin](https://chat.openai.com/?model=gpt-4-plugins) and [Chrome exntension](https://www.webpilot.ai/).

## Dependencies

Please execute the following command in the terminal to install the required dependencies:

Python>=3.8

```shell
cd ChatLongDoc
pip install -r requirements.txt
```

## Usage

In the **demo.ipynb**, we provide a simple and clear procedure:

1. Please replace the first line of the `./openai_api_key.txt` file with your preferred OpenAI API Key. It will be read when the dependencies are loaded.
2. Enter the path to the local file you wish to chat with. Our program currently supports pdf, doc, docx, txt files, and web URLs. As a tutorial, you may try the `./example/example.pdf` and `./example/example2.pdf` files, which are papers titled ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762) and ["Uni-Encoder: A Fast and Accurate Response Selection Paradigm for Generation-Based Dialogue Systems"](https://arxiv.org/abs/2106.01263).
3. Once the file is loaded, our system will process the content of the document or web page and store the memorized information in `./memory` for future reference. A memory file is already available in the directory if you're using the example document.
4. Input your query and start chatting with the document.

You may also use the following command after installing all dependencies and adding your OpenAI API Key:
```shell
cd ChatLongDoc
python chatLongDoc.py --text_path "your_text_path" --memory_path "your_memory_path"
```
`--text_path` is the local file path or web URL that you want to read, e.g. "example/example.pdf" or "https://arxiv.org/abs/2106.01263".

If `--memory_path` is specified, then the program will only load the cached memory file instead of reprocessing texts from `--text_path`.

You only need to specify either one of them, please refer to `-h` for more details.

## 欢迎使用本项目

这个项目突破了使用OpenAI Chat-LLMs（如ChatGPT）的长度限制，使您能够与任何长文档进行对话。帮助对内容的理解，便于获取有价值的见解。与ChatPDF相比，它支持包括PDF、word文档、txt文件 和 网页 在内的各种文件格式。该项目的实现简单易懂，易于扩展，并且能够高效地集成到其他应用程序中。

欢迎关注我们的 [ChatGPT plugin](https://chat.openai.com/?model=gpt-4-plugins) 和 [Chrome扩展](https://www.webpilot.ai/)。

## 环境依赖

请在终端中执行以下命令，安装所需依赖：

Python>=3.8

```shell
cd ChatLongDoc
pip install -r requirements.txt
```

## 使用流程

在 **demo.ipynb** 中我们给出了简单明了的使用步骤：

1. 请将 ./openai_api_key.txt 文件的第一行替换为您喜欢的 OpenAI API 密钥。当加载依赖项时，它将被读取。
2. 输入您想要了解的本地文档地址或网页 URL，文档格式目前支持 pdf、doc、docx、txt。也可以尝试我们提供的`./example/example.pdf`或`./example/example2.pdf`进行试用，样例文件为论文 ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762) 和 ["Uni-Encoder: A Fast and Accurate Response Selection Paradigm for Generation-Based Dialogue Systems"](https://arxiv.org/abs/2106.01263)。
3. 一旦文件被加载，我们的系统将处理文档或网页的内容，并将记忆的信息存储在 ./memory 中供以后参考。如果您正在使用示例文档，已经在目录中提供了一个记忆文件。
4. 输入您的问题，开始与文档聊天吧。

安装完所有的依赖并添加OpenAI API Key后也可以通过以下指令运行程序:
```shell
cd ChatLongDoc
python chatLongDoc.py --text_path "your_text_path" --memory_path "your_memory_path"
```
`--text_path`是您要读取的本地文件路径或Web URL，例如 "example/example.pdf" 或 "https://arxiv.org/abs/2106.01263" 。

如果指定了`--memory_path`, 则程序将仅加载缓存的记忆文件，而不是重新从`--text_path`处理文本。

您只需指定其中一个即可，请参阅`-h`以获取更多详细信息。
