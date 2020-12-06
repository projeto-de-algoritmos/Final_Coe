from lib.file import File
from typing import List


class Commons:

    @staticmethod
    def get_file(file_path: str, encode_type: str, **kwargs) -> List[str]:
        return File.open_file(file_path, encode_type)