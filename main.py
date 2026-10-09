"""Run NovaLang's source-to-output pipeline or inspect tokens and AST."""

import argparse
from pathlib import Path
import sys

from environment import EnvironmentError
from interpreter import Interpreter, RuntimeErrorNova
from lexer import LexicalError, tokenize
from parser import ParseError, Parser


def main(argv=None):
    arguments = argparse.ArgumentParser(description=__doc__)
    arguments.add_argument("program_file", type=Path, help="UTF-8 NovaLang source file")
    inspection = arguments.add_mutually_exclusive_group()
    inspection.add_argument("--tokens", action="store_true", help="show tokens without execution")
    inspection.add_argument("--ast", action="store_true", help="show the AST without execution")
    options = arguments.parse_args(argv)

    try:
        source = options.program_file.read_text(encoding="utf-8")
        tokens = tokenize(source)
        if options.tokens:
            for token in tokens:
                print(f"{token} @ {token.line}:{token.column}")
            return 0
        program = Parser(tokens).parse_program()
        if options.ast:
            print(program.pretty())
        else:
            Interpreter().execute(program)
        return 0
    except (LexicalError, ParseError) as error:
        print(error, file=sys.stderr)
    except (EnvironmentError, RuntimeErrorNova) as error:
        print(f"Runtime error: {error}", file=sys.stderr)
    except RecursionError:
        print("Runtime error: maximum recursion depth exceeded", file=sys.stderr)
    except (OSError, UnicodeError) as error:
        print(f"File error: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
