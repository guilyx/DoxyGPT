from dataclasses import dataclass

@dataclass
class FileInformation:
    filename: str
    author: str
    version: str
    date: str
    copyright: str
    abs_filepath: str
