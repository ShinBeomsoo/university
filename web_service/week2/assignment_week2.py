import os
from typing import List

COMMAND = ["echo", "cat", ">"]


class Compiler:
    @staticmethod
    def echo_to_c_language(sentence: str, *args, **kwargs) -> str:
        """
        echo 명령어를 c 언어로 변경해주는 메소드
        """
        return f'// echo {sentence}\n' \
               f'printf("{sentence}\\n");\n\n'

    @staticmethod
    def cat_to_c_language(sentence: str, *args, **kwargs) -> str:
        """
        cat 명령어를 c 언어로 변경해주는 메소드
        """
        return f'// cat {sentence}\n' \
               f'f1 = fopen("{sentence}", "r");\n' \
               f'while((c = getc(f1)) != EOF)\n' \
               f'    printf("%c", c);\n' \
               f'fclose(f1);\n\n'

    @staticmethod
    def cat_redirect_to_c_language(*args, **kwargs) -> str:
        """
        cat 에 redirect 가 포함된 명령어를 c 언어로 변경해주는 메소드
        """
        file1, file2 = kwargs["sentence"].split(" > ")
        return f'// cat {kwargs["sentence"]}\n' \
               f'f1 = fopen("{file1}", "r");\n' \
               f'f2 = fopen("{file2}", "w");\n' \
               f'while((c = getc(f1)) != EOF)\n' \
               f'    fputc((int)c,f2);\n' \
               f'fclose(f2);\n' \
               f'fclose(f1);\n\n'


def write_file(command: str, sentence: str) -> None:
    """
    컴파일된 코드를 파일에 출력해주는 함수
    :param command: parser를 통해 얻은 명령어. "echo" | "cat" | "cat >"
    :param sentence: 명령어에 있는 argument 문자열
    :return: None
    """
    compiler = {
        "echo": Compiler.echo_to_c_language, "cat": Compiler.cat_to_c_language,
        "cat >": Compiler.cat_redirect_to_c_language,
    }
    with open(f"./week2/test.c", "a") as f:
        c_language = compiler[command](sentence=sentence.replace('"', ''))
        f.write(c_language)


def parse_command(line: str) -> str:
    """
    test.n에 있는 명령어에서 echo 와 cat 그리고 redirect(>) 를 추출하는 함수
    :param line: test.n에 있는 명령어
    :return: "echo" | "cat" | "cat >"
    """
    parse_cmd = []
    for cmd in COMMAND:
        if cmd in line.split(" "):
            parse_cmd.append(cmd)
    if not parse_cmd:
        os.remove("./week2/test.c")
        raise AttributeError
    return ' '.join(parse_cmd)


# test.n에 있는 명령어를 읽어오는 method
def read_command_file_lines() -> List[str]:
    with open("./week2/test.n", "r") as f:
        file_lines = f.read().splitlines()
    return file_lines


def process_compiler() -> None:
    """
    명령어를 c 언어로 변경해주는 method
    """
    lines = read_command_file_lines()
    for line in lines:
        parse_cmd = parse_command(line)
        if "echo" in parse_cmd:
            write_file(parse_cmd, line.split("echo ")[1])
        elif "cat" in parse_cmd:
            write_file(parse_cmd, line.split("cat ")[1])


# 명령어를 c언어로 변경 전 필요한 요소를 test.c에 추가하는 method
def start_up_compiler() -> None:
    c_language = '#include <stdio.h>\nint main(){\nFILE *f1, *f2;\nchar c;\n'
    with open("./week2/test.c", "w") as f:
        f.write(c_language)


# 명령어를 c언어로 변경 후 필요한 요소를 test.c에 마지막으로 추가하는 method
def end_up_compiler() -> None:
    c_language = 'return 0;\n}'
    with open("./week2/test.c", "a") as f:
        f.write(c_language)


def main():
    start_up_compiler()
    process_compiler()
    end_up_compiler()


if __name__ == '__main__':
    main()
