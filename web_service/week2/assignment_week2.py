import os
from typing import List

COMMAND = ["echo", "cat", ">"]


class Compiler:
    @staticmethod
    def echo_to_c_language(sentence: str, *args, **kwargs) -> str:
        return f'printf({sentence});\n'

    @staticmethod
    def cat_to_c_language(sentence: str, *args, **kwargs) -> str:
        return f'f1 = fopen("{sentence}", "r");\n' \
               f'while((c = getc(f1)) != EOF)\n' \
               f'    printf("%c", c);\n' \
               f'fclose(f1);\n'

    @staticmethod
    def direct_to_c_language(*args, **kwargs) -> str:
        file1, file2 = kwargs["sentence"].split(" > ")
        return f'f1 = fopen("{file1}", "r");\n' \
               f'f2 = fopen("{file2}", "w");\n' \
               f'while((c = getc(f1)) != EOF)\n' \
               f'    fputc((int)c,f2);\n' \
               f'fclose(f2);\n' \
               f'fclose(f1);\n'


def write_file(command: str, sentence: str):
    compiler = {
        "echo": Compiler.echo_to_c_language, "cat": Compiler.cat_to_c_language,
        "cat >": Compiler.direct_to_c_language,
    }
    with open(f"./week2/test.c", "a") as f:
        c_language = compiler[command](sentence=sentence)
        f.write(c_language)


def start_up_compiler() -> None:  # 명령어를 c언어로 변경 전 필요한 요소를 test.c에 추가하는 method
    c_language = '#include <stdio.h>\nint main(){\nFILE *f1, *f2;\nchar c;\n'
    with open("./week2/test.c", "w") as f:
        f.write(c_language)


def read_file_lines() -> List[str]:  # test.n에 있는 명령어를 읽어오는 method
    with open("./week2/test.n", "r") as f:
        file_lines = f.read().splitlines()
    return file_lines


def end_up_compiler() -> None:  # 명령어를 c언어로 변경 후 필요한 요소를 test.c에 마지막으로 추가하는 method
    c_language = 'return 0;\n}'
    with open("./week2/test.c", "a") as f:
        f.write(c_language)


def parse_command(line) -> str:
    parse_cmd = []
    for cmd in COMMAND:
        if cmd in line.split(" "):
            parse_cmd.append(cmd)
    return ' '.join(parse_cmd)


def main():
    start_up_compiler()
    lines = read_file_lines()
    for line in lines:
        parse_cmd = parse_command(line)
        write_file(parse_cmd, line.split("cat ")[1])
    end_up_compiler()


if __name__ == '__main__':
    main()
