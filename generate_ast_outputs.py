from pathlib import Path

from lexer import tokenize
from parser import Parser


PROGRAMS_DIR = Path("tests/programs")
OUTPUTS_DIR = Path("tests/outputs")


def generate_ast(program_file):
    source = program_file.read_text(encoding="utf-8")

    tokens = tokenize(source)
    parser = Parser(tokens)

    ast = parser.parse_program()

    output_file = OUTPUTS_DIR / f"{program_file.stem}.txt"

    output_file.write_text(
        ast.pretty() + "\n",
        encoding="utf-8"
    )

    print(f"Generated: {output_file}")


def main():
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    for program_file in sorted(PROGRAMS_DIR.glob("ast_example_*.nova")):
        generate_ast(program_file)


if __name__ == "__main__":
    main()
