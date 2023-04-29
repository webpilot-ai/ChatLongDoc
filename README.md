# ChatLongDoc

## Welcome to this project

This project surpasses the length constraints of using OpenAI Chat-LLMs, such as ChatGPT, enabling you to converse with any long document. It expedites comprehension of the content and facilitates the acquisition of valuable insights. Compared with ChatPDF, it accommodates various file formats, including PDF, doc, docx, txt, and web URLs. The implementation of this project is straightforward to follow, expand, and efficient for integration into other applications.

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
2. Enter the path to the local file you wish to chat with. Our program currently supports pdf, doc, docx, txt files, and web URLs. As a tutorial, you may try the `./example/example.pdf file`, which is a paper titled ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762).
3. Once the file is loaded, our system will process the content of the document or web page and store the memorized information in `./memory` for future reference. A memory file is already available in the directory if you're using the example document.
4. Input your query and start chatting with the document.


## 欢迎使用本项目

这个项目突破了使用OpenAI Chat-LLMs（如ChatGPT）的长度限制，使您能够与任何长文档进行对话。帮助对内容的理解，便于获取有价值的见解。与ChatPDF相比，它支持包括PDF、word文档、txt文件 和 网页 在内的各种文件格式。该项目的实现简单易懂，易于扩展，并且能够高效地集成到其他应用程序中。

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
2. 输入您想要聊天的本地文件路径。我们的程序目前支持 pdf、doc、docx、txt 文件和 Web URL。作为教程，您可以尝试使用标题为 "Attention Is All You Need" 的论文，它位于 ./example/example.pdf 文件中。
3. 一旦文件被加载，我们的系统将处理文档或网页的内容，并将记忆的信息存储在 ./memory 中供以后参考。如果您正在使用示例文档，已经在目录中提供了一个记忆文件。
4. 输入您的查询并开始与文档聊天。
