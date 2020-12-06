import PySimpleGUI as sg
from typing import Final
from view.gui.decode.decode_view import DecodeView
from view.gui.encode.encode_view import EncodeView

FILE_PATH: Final = "FILE_PATH"
FILEBROWSE: Final = "FILEBROWSE"
ENC_TYPE: Final = "ENC_TYPE"
ENC_RADIO: Final = "ENC_RADIO"
DEC_RADIO: Final = "DEC_RADIO"
HANDLE_ACTION: Final = "HANDLE_ACTION"

class ViewGui(DecodeView, EncodeView):

    def __init__(self):
        super(ViewGui, self).__init__()
        self.window = sg.Window('Greed compressor', self.mount_interface(), finalize=True)
        self.values = None
        self.event = None
        self.action_handlers = {
            "decode": super().handle_decode_action,
            "encode": super().handle_encode_action
        }

    def init(self):
        while True: 
            self.event, self.values = self.window.read() 
            
            if self.event in  (None, 'Sair', 'WIN_CLOSED'): 
                self.exit_program()
            
            if self.event == FILEBROWSE: 
                self.window[FILE_PATH].update(self.values[FILEBROWSE]) 
            
            if self.event == HANDLE_ACTION:
                self.handle_action()


    def mount_interface(self):
        return [
            [sg.Input(key=FILEBROWSE, enable_events=True, visible=False)],
            [sg.Text('Arquivo escolhido:'), sg.Text(' '* 31),  sg.FileBrowse('Selecionar', target=FILEBROWSE,file_types=(("Text Files", "*.txt"), ("Compressed Files", "*.greed_compressed")))],
            [sg.Input(key=FILE_PATH, readonly=True, justification='center')],
            [sg.Radio('Comprimir', ENC_TYPE, default=True, key=ENC_RADIO), sg.Radio('Descomprimir', ENC_TYPE, key=DEC_RADIO)],
            [sg.Button('Confirmar', key=HANDLE_ACTION), sg.Text(' '* 48), sg.Button('Sair')]
        ]
    
    def handle_action(self) -> None:
        try:
            handler = self.get_selected_radio_option()
            self.action_handlers[handler](self.values[FILE_PATH])
        except FileNotFoundError:
            self.show_popup("Erro: nenhum arquivo selecionado.")

    def get_selected_radio_option(self) -> None:
        if not self.values[FILEBROWSE]:
            raise FileNotFoundError()
        return "encode" if self.values[ENC_RADIO] else "decode"

    def show_popup(self, *args, **kwargs):
        sg.popup(*args, **kwargs)

    def exit_program(self):
        self.window.close()
        exit(0)