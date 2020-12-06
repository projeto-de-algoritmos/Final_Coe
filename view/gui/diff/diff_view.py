from PySimpleGUI import popup
from view.commons.encode_commons import EncodeCommons
from view.commons.commons import Commons
from view.commons.decode_commons import DecodeCommons
from lib.file import File
from lib.diff import Diff
import os
from pathlib import Path
from lib.file import File

script_dir = os.path.dirname(__file__) 
rel_path = "../../../compressed_files/"
abs_file_path = os.path.join(script_dir, rel_path)

class DiffView:
    def __init__(self,):
        super(DiffView, self).__init__()
        self.diff_lib = Diff()
        self.diff_lst = []
        self.is_different = 0

    def handle_diff_action(self, file_1, file_2) -> None:
        self.diff_lst = []
        self.is_different = 0

        file1 = self.handle_file(file_1)
        file2 = self.handle_file(file_2)

        c = self.diff_lib.lcslen(file1, file2)
        self.get_differences(c, file1, file2, len(file1) - 1, len(file2) - 1)

        out_path = os.path.join(script_dir, "../../../diff/") + file_1.split("/")[-1] + "__" + file_1.split("/")[-1] + "__diff"
        if self.is_different > 0:
            File.save_file(
                out_path, 
                file_content= "".join(self.diff_lst), 
                type='wt'
            )

            self.show_popup("Foram encontradas diferenças entre os arquivos selecionados", "Você pode vê-las no arquivo gerado em:", out_path)
        else:
            self.show_popup("Não foram encontradas diferenças entre os arquivos selecionados")

    def handle_file(self, file_path):
        file = None
        try:
            file = Commons.get_file(file_path=file_path, encode_type='r')

        except Exception as ex:
            file = Commons.get_file(file_path=file_path, encode_type='rb')
            
            file = DecodeCommons.get_decoded_text(file).splitlines(True)

        return file

    def get_differences(self, c, x, y, i, j):
        if i < 0 and j < 0:
            return ""
        elif i < 0:
            self.get_differences(c, x, y, i, j-1)
            self.is_different += 1
            self.diff_lst.append("+ " + y[j])
        elif j < 0:
            self.get_differences(c, x, y, i-1, j)
            self.is_different += 1
            self.diff_lst.append("- " + x[i])
        elif x[i] == y[j]:
            self.get_differences(c, x, y, i-1, j-1)
            self.diff_lst.append("  " + x[i])
        elif c[i][j-1] >= c[i-1][j]:
            self.get_differences(c, x, y, i, j-1)
            self.is_different += 1
            self.diff_lst.append("+ " + y[j])
        elif c[i][j-1] < c[i-1][j]:
            self.get_differences(c, x, y, i-1, j)
            self.is_different += 1
            self.diff_lst.append("- " + x[i])