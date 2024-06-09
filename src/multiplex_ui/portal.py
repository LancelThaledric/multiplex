from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton


class MPPortal(QFrame):

    def __init__(self, action_files: QAction, action_folder: QAction):
        super().__init__()
        self.layout = QVBoxLayout()
        self.button_files = QPushButton('Open files...')
        self.button_folder = QPushButton('Open folder...')
        self.layout.addWidget(self.button_files)
        self.layout.addWidget(self.button_folder)
        self.setLayout(self.layout)
        self.button_files.clicked.connect(action_files.trigger)
        self.button_folder.clicked.connect(action_folder.trigger)
