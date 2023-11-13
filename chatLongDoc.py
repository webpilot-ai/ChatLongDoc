from argparse import ArgumentParser
from utils import *

def main():
    parser = ArgumentParser(
        usage="chatLongDoc.py [<args>] [-h | --help]"
    )
    parser.add_argument(
        "--text_path",
        type=str,
        default=None,
        help='''Local file path or web URL.
        e.g. 'example/example.pdf' or 'https://arxiv.org/abs/1706.03762'.
        ''',
    )
    parser.add_argument(
        "--memory_path",
        type=str,
        default=None,
        help='''Local file path to cached memory file.
        e.g. 'memory/315b4f4c655530196ef5f4f6f1d1f0b57d24fa2b08ff006c44b535d50499b487.json'.
        If '--memory_path' is specified, the program will load the cached memory instead of processing texts from '--text_path'.
        ''',
    )
    args = parser.parse_args()

    if args.text_path is None and args.memory_path is None:
        raise ValueError("Either '--text_path' or '--memory_path' must be specified.")
    elif args.memory_path is not None:
        chat(args.memory_path)
    else:
        text = get_text(args.text_path)
        memory_path = memorize(text)
        chat(memory_path)

if __name__ == '__main__':
    main()
