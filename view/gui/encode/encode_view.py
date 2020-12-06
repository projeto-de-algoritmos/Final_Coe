from PySimpleGUI import popup
from view.commons.encode_commons import EncodeCommons
from view.commons.commons import Commons
from lib.file import File
import os
from pathlib import Path

script_dir = os.path.dirname(__file__) 
rel_path = "../../../compressed_files/"
abs_file_path = os.path.join(script_dir, rel_path)

class EncodeView:
    def __init__(self,):
        super(EncodeView, self).__init__()

    def handle_encode_action(self, file_path: str):
        try:
            file = Commons.get_file(file_path=file_path, encode_type='r')
        except Exception as ex:
            print(ex)
            self.show_popup("Não foi possível abrir o arquivo selecionado", "Verifique se você escolheu um arquivo no formato .txt!!")
            return

        file_content = EncodeCommons.encode_file(file)

        encoded_file_path = abs_file_path + self.get_file_extension(file_path) + ".greed_compressed"

        File.save_file(path = encoded_file_path, file_content = file_content.tobytes())

        popup(
            "Encode realizado com sucesso!!",
            "Você pode ver o arquivo comprmido em:",
            encoded_file_path,
            self.calculate_size_diference(file_path, encoded_file_path))

    def get_file_extension(self, file_path: str) -> str:
        return file_path.split("/")[-1].split(".")[0]
    
    def calculate_size_diference(self, original_file_path: str, encoded_file_path: str) -> None:
        original_file_size = Path(original_file_path).stat().st_size
        encoded_file_size = Path(encoded_file_path).stat().st_size
        
        return f"""\nCompressão feita com sucesso!!
            Tamanho do arquivo original:: {original_file_size} bytes
            Tamanho do arquivo comprimido:: {encoded_file_size} bytes
            Diferença de tamanho entre os arquivos:: {original_file_size - encoded_file_size} \
            Porcentagem de compressão:: { (1 - (encoded_file_size / original_file_size)) * 100 } %"""