# ChatLongDoc

## Welcome to this project

This project aims to use the OpenAI API to enable the memory and understanding of long text documents. By conversing with the system, you can quickly understand the content in the document, breaking the limit of the maximum text length that APIs can handle. This project supports multiple file formats, including PDFs, as provided by ChatPDF, as well as doc, docx, and txt files. It also allows conversations based on the input URLs. We believe that this project is one of the simplest and most effective ways to implement and deploy.

## Dependencies

Please execute the following command in the terminal to install the required dependencies:

Python>=3.8

```shell
cd ChatLongDoc
pip install -r requirements.txt
```

## Usage

In the demo.ipynb, we provide a simple and clear procedure:

1. Please replace the first line of the `./openai_api_key.txt` file with the OpenAI API Key you want to use. It will be read when the dependencies are loaded.
2. Enter the local file path or web URL you want to chat with. The pdf, doc, docx, and txt formats are currently supported. You can also try the `./example/example.pdf` that we provide for toturial. The sample file is the paper [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
3. Memorize the content of the document or web page it read. The memorized information will be stored in `./memory`, where already includes the memory file of the trial document we provide.
4. Enter your question and start chatting with the document.

## 欢迎使用本项目

本项目利用 OpenAI 的 API 实现了对长文本文档的记忆和理解。通过与系统进行对话，您可以快速了解文档所述内容，打破了 API 处理最长文本长度的限制。本项目支持多种文件格式，包括 ChatPDF 提供的 PDF 辅助阅读，也支持 doc、docx 和 txt 文件，同时还允许输入网址进行基于网页内容的对话。我们相信，这个项目是实现类似需求最简单有效的方法之一。

## 环境依赖

请在终端中执行以下命令，安装所需依赖：

Python>=3.8

```shell
cd ChatLongDoc
pip install -r requirements.txt
```

## 使用流程

在 demo.ipynb 中我们给出了简单明了的使用步骤：

1. 请先将 `./openai_api_key.txt` 文件中的第一行替换成您想要使用的 OpenAI API Key，在 demo 加载依赖的过程中会读取。
2. 输入您想要了解的本地文档地址或网页 URL，文档格式目前支持 pdf、doc、docx、txt。也可以使用我们提供的 `./example/example.pdf` 进行试用，样例文件为论文 [Attention Is All You Need](https://arxiv.org/abs/1706.03762)。
3. 记忆所读取的文档或网页内容，记忆后的信息会存储在 `./memory` 中，其中已经包含了我们提供的试用文档的记忆信息文件。
4. 输入问题，开始和文档聊天吧。
