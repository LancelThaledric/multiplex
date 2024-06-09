from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMenuBar

from src.multiplex_ui.picker import MPPicker, PickerData
from src.multiplex_ui.portal import MPPortal


class MPApplication(QApplication):

    def __init__(self):
        super().__init__()

        # State
        self.files: PickerData = []

        # Actions
        self.open_files = QAction(text='Open files...')
        self.open_folder = QAction(text='Open folder...')
        self.menu = QMenuBar(None)
        self.menu_file = self.menu.addMenu('File')
        self.menu_file.addAction(self.open_files)
        self.menu_file.addAction(self.open_folder)

        # Members
        self.picker = MPPicker()
        self.portal = MPPortal(self.open_files, self.open_folder)

        # Reactive
        self.open_files.triggered.connect(self.picker.pick_files)
        self.open_folder.triggered.connect(self.picker.pick_folder)
        self.picker.open.connect(self.load)

    def exec(self):
        # Startup time
        self.portal.show()
        # self.files = self.picker.pick_files()
        # print(self.files)
        # if len(self.files) == 0:
        #     return
        # Launch event loop
        super().exec()

    @Slot(list)
    def load(self, data: PickerData):
        print('OPEN', data)
