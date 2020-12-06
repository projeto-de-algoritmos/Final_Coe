from view.commons.commons import Commons
from view.commons.decode_commons import DecodeCommons
from datetime import datetime
from lib.file import File
import os

script_dir = os.path.dirname(__file__) 
rel_path = "../../../examples/"
abs_file_path = os.path.join(script_dir, rel_path)


class DecodeView:
    def __init__(self,):
        super(DecodeView, self).__init__()

    def handle_decode_action(self, file_path: str):
        file_extension = file_path.split("/")[-1].split(".")[-1] == "greed_compressed"
        
        if not file_extension:
            self.show_popup("Não foi possível abrir o arquivo selecionado", "Verifique se você escolheu um arquivo no formato .greed_compressed!!")
            return

        try:
            file = Commons.get_file(file_path=file_path, encode_type='rb')
        except Exception as ex:
            self.show_popup("Não foi possível abrir o arquivo selecionado", "Verifique se você escolheu um arquivo no formato .greed_compressed!!")
            return

        decoded_text = DecodeCommons.get_decoded_text(file)

        decoded_content_path = abs_file_path + self.get_file_extension(file_path) + datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".txt"

        decoded_file_path = os.path.join(decoded_content_path)

        File.save_file(decoded_file_path, file_content=decoded_text, type='wt')

        self.show_popup("Arquivo descomprimido com sucesso!!", "Você pode vê-lo na pasta:", decoded_file_path)

    def get_file_extension(self, file_path: str) -> str:
        return file_path.split("/")[-1].split(".")[0]