from PySide6 import QtWidgets
from PySide6.QtCore import Slot, QProcess
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow

from src.ffmpeg_client.walker import FileWalker
from src.multiplex_ui.picker import PickerData

type ProcessData = list


class MPWindow(QMainWindow):

    @Slot()
    def on_process_message(self):
        process = self.sender()
        output = bytes(process.readAllStandardOutput()).decode('UTF-8').strip()
        self.console.appendPlainText(output)

    @Slot()
    def on_process_error(self):
        process = self.sender()
        output = bytes(process.readAllStandardOutput()).decode('UTF-8').strip()
        self.console.appendPlainText(output)

    def __init__(self, data: PickerData):
        super().__init__()

        # State
        self.data = FileWalker(data)

        # Test UI
        self.console = QtWidgets.QPlainTextEdit()
        self.console.setReadOnly(True)
        monospace_font = QFont('Menlo')
        monospace_font.setStyleHint(QFont.Monospace)
        self.console.setFont(monospace_font)
        self.setCentralWidget(self.console)
        self.console.appendPlainText(' === MULTIPLEX === \n')

        # Test Process
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.on_process_message)
        self.process.readyReadStandardError.connect(self.on_process_error)

        files = self.data.iterfiles()
        test_file = next(files)
        self.process.start('ffprobe', ['-show_streams', '-of', 'json', str(test_file)])

        self.show()
