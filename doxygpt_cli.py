"""
CLI to generate documented code.
"""

from argparse import ArgumentParser
from doxygpt.codefile import FileInformation
from doxygpt.doxy import Doxy


class CLI:
    def __init__(self):
        parser = ArgumentParser(prog="DoxyGPT")
        parser.add_argument("dotenv", help="The absolute path to the dotenv file.")
        parser.add_argument(
            "codefile", help="The absolute path to the code file to document."
        )
        args = parser.parse_args()

        self.dotenv = args.dotenv
        self.codefile = args.codefile

        filename = input("Enter [FILENAME].    ")
        author = input("Enter [AUTHOR].    ")
        version = input("Enter [VERSION].    ")
        date = input("Enter [CREATION_DATE].    ")
        cr = input("Enter [COPYRIGHT].    ")

        self.file_info = FileInformation(
            filename, author, version, date, cr, self.codefile
        )
        self.doxygpt = Doxy(self.dotenv, self.file_info)


if __name__ == "__main__":
    CLI()
