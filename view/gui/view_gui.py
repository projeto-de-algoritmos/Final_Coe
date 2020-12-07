import PySimpleGUI as sg
from typing import Final
from view.gui.decode.decode_view import DecodeView
from view.gui.encode.encode_view import EncodeView
from view.gui.diff.diff_view import DiffView

FILE_PATH: Final = "FILE_PATH"
FILE_PATH_DIFF: Final = "FILE_PATH_DIFF"
FILEBROWSE: Final = "FILEBROWSE"
FILEBROWSE_DIFF: Final = "FILEBROWSE_DIFF"
ENC_TYPE: Final = "ENC_TYPE"
ENC_RADIO: Final = "ENC_RADIO"
DEC_RADIO: Final = "DEC_RADIO"
DIFF_ENC_RADIO: Final = "DIFF_ENC_RADIO"
HANDLE_ACTION: Final = "HANDLE_ACTION"
DIFF_BUTTON: Final = "DIFF_BUTTON"
DIFF_FRAME: Final = "DIFF_FRAME"

class ViewGui(DecodeView, EncodeView, DiffView):

    def __init__(self):
        super(ViewGui, self).__init__()
        self.diff = False
        self.window = sg.Window('Coé - Greed compressor', self.mount_interface(), finalize=True)
        self.values = None
        self.event = None
        self.action_handlers = {
            "decode": super().handle_decode_action,
            "encode": super().handle_encode_action,
            "diff": super().handle_diff_action
        }

    def init(self):
        while True: 
            self.event, self.values = self.window.read() 

            if self.event in  (None, 'Sair', 'WIN_CLOSED'): 
                self.exit_program()
            
            if self.event in (ENC_RADIO, DEC_RADIO, DIFF_ENC_RADIO):
                self.window[DIFF_BUTTON].update(disabled = not self.values[DIFF_ENC_RADIO])
                self.window[DIFF_FRAME].update(visible = self.values[DIFF_ENC_RADIO])

            if self.event == FILEBROWSE: 
                self.window[FILE_PATH].update(self.values[FILEBROWSE]) 
            
            if self.event == FILEBROWSE_DIFF:
                self.window[FILE_PATH_DIFF].update(self.values[FILEBROWSE_DIFF]) 

            if self.event == HANDLE_ACTION:
                self.handle_action()


    def mount_interface(self):
        diff_layout = [
            [ sg.Input(key=FILEBROWSE_DIFF, enable_events=True, visible=False)],
            [ sg.Text('Arquivo escolhido (diff):'), sg.Text(' '* 23),  sg.FileBrowse('Selecionar', key=DIFF_BUTTON, disabled=True, target=FILEBROWSE_DIFF,file_types=(("Text Files", "*.txt"), ("Compressed Files", "*.greed_compressed")))],
            [ sg.Input(key=FILE_PATH_DIFF, readonly=True, justification='center')],
        ]

        return [
            [ sg.Input(key=FILEBROWSE, enable_events=True, visible=False)],
            [ sg.Text('Arquivo escolhido:'), sg.Text(' '* 31),  sg.FileBrowse('Selecionar', target=FILEBROWSE,file_types=(("Text Files", "*.txt"), ("Compressed Files", "*.greed_compressed")))],
            [ sg.Input(key=FILE_PATH, readonly=True, justification='center')],
            [ sg.Radio('Comprimir', ENC_TYPE, default=True, key=ENC_RADIO, enable_events=True), 
              sg.Radio('Descomprimir', ENC_TYPE, key=DEC_RADIO, enable_events=True), 
              sg.Radio('Diff', ENC_TYPE, key=DIFF_ENC_RADIO, enable_events=True)
            ],
            [sg.Frame('Diff', diff_layout, key=DIFF_FRAME, font='Any 12', visible=False)],
            [ sg.Button('Confirmar', key=HANDLE_ACTION), sg.Text(' '* 48), sg.Button('Sair')]
        ]
    
    def handle_action(self) -> None:
        try:
            handler = self.get_selected_radio_option()
            self.action_handlers[handler](self.values[FILE_PATH], self.values[FILE_PATH_DIFF])
        except FileNotFoundError:
            self.show_popup("Erro: nenhum arquivo selecionado.")

    def get_selected_radio_option(self) -> None:
        options = {
            ENC_RADIO: "encode",
            DEC_RADIO: "decode",
            DIFF_ENC_RADIO: "diff"
        }

        if not self.values[FILEBROWSE]:
            raise FileNotFoundError()
        else:
            if self.values[ENC_RADIO]: return options[ENC_RADIO]
            elif self.values[DEC_RADIO]: return options[DEC_RADIO]
            elif self.values[DIFF_ENC_RADIO]: return options[DIFF_ENC_RADIO]

    def show_popup(self, *args, **kwargs):
        sg.popup(*args, **kwargs)

    def exit_program(self):
        self.window.close()
        exit(0)