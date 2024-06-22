from PySide6.QtWidgets import QMainWindow

from src.ffmpeg_client.walker import FileWalker
from src.multiplex_ui.picker import PickerData

type ProcessData = list


class MPWindow(QMainWindow):

    def __init__(self, data: PickerData):
        super().__init__()
        self.data = FileWalker(data)
        print(self.data._input)
        for f in self.data.iterfiles():
            print([f])
        self.show()
