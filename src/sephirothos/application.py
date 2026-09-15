from PySide6.QtWidgets import QApplication

class SephirothOS:
    def __init__(self, argv: list[str]):
        self.qt = QApplication(argv)
        self.shell = None

    def run(self) -> int:
        from sephirothos.ui.shell import Shell

        self.shell = Shell(self)
        self.shell.show()

        return self.qt.exec()