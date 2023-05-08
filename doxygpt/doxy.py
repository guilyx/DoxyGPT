"""
Calling on ChatGPT API Wrapper to generate Doxygen documentation.
"""

from .gpt import GPT
from .codefile import FileInformation

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_gpt(text: str):
    print(f"\n{bcolors.OKBLUE}[CHATGPT] - {text}{bcolors.ENDC}\n")

class Doxy:
    def __init__(self, dotenv: str, file_information: FileInformation):
        self.file_information = file_information
        self.llm = GPT(dotenv)

        # self.__prepare_llm()

        with open(self.file_information.abs_filepath, "r") as file:
            self.file_content = file.read()

        new_content = self.__get_doxygen_doc_llm(self.file_content)

        print_gpt(new_content)

        new_path = self.file_information.abs_filepath.split("/")
        new_filename = "DoxyGPT_" + new_path[-1]
        new_path = new_path[:-1]
        new_path_complete = ""
        for elem in new_path:
            new_path_complete += elem
            new_path_complete += "/"
        new_path_complete += new_filename

        print(new_path_complete)

        with open(new_path_complete, "w") as f:
            f.write(new_content)
    
    def __prepare_llm(self):
        print("Rubbing ChatGPT to use your Input Information...")

        res = self.llm.ask(
            f"Let's do a Doxygen documentation for a C++ file. \n"
            f"Use the Doxygen tags @file, @author, @brief, @version, @date and @copyright in the file header documentation. \n"
            f"@file is {self.file_information.filename} \n"
            f"@author is {self.file_information.author} \n"
            f"@version is {self.file_information.version} \n"
            f"@date is {self.file_information.date} \n"
            f"@copyright is {self.file_information.copyright} \n"
            f"Use the code from the next input to generate the documentation."
        )

        print_gpt(res)

        print("ChatGPT is now ready to generate Doxygen.")

    def __get_doxygen_doc_llm(self, content: str):
        new_content = self.llm.ask(
            f"Let's do a Doxygen documentation for a C++ file. \n"
            f"Use the Doxygen tags @file, @author, @brief, @version, @date and @copyright in the file header documentation. \n"
            f"@file is {self.file_information.filename} \n"
            f"@author is {self.file_information.author} \n"
            f"@version is {self.file_information.version} \n"
            f"@date is {self.file_information.date} \n"
            f"@copyright is {self.file_information.copyright} \n"
            f"Use the code from the next input to generate the documentation."
            f"Input the header documentation you provided one message ago, as well as intelligently document this file. Output ONLY the entire new file.\n"
            f"\n"
            f"{self.file_content}"
        )

        return new_content