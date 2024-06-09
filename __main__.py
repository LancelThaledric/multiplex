import sys

from src.multiplex_ui.application import MPApplication

if __name__ == "__main__":
    app = MPApplication()
    sys.exit(app.exec())
