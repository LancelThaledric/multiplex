from pathlib import Path

from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QFileDialog

type PickerData = list[Path]


class MPPicker(QObject):
    open = Signal(list)

    def __init__(self):
        super().__init__()
        self.dialog = QFileDialog()

    def pick_files(self) -> PickerData:
        paths_raw, _ = self.dialog.getOpenFileNames()
        paths = [Path(p) for p in paths_raw]
        self.open.emit(paths)
        return paths

    def pick_folder(self):
        path_raw = self.dialog.getExistingDirectory()
        paths = [Path(path_raw)]
        self.open.emit(paths)
        return paths
