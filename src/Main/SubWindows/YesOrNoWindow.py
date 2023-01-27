from PyQt5.QtWidgets import *


class YesOrNoWindow(QDialog):
    def __init__(self, title: str, description: str, parent: QWidget):
        super().__init__()
        self.setFixedSize(270, 120)
        self.move(parent.x()+parent.width()//2-self.width()//2, parent.y()+parent.height()//2-self.height()//2)
        self.setWindowTitle(title)
        self.setFont(parent.font())
        main_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum))
        cancel_button = QPushButton("아니오", self)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        ok_button = QPushButton("예", self)
        ok_button.clicked.connect(self.accept)
        button_layout.addWidget(ok_button)
        main_layout.addWidget(QLabel(description, self))
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def show(self):
        return super().exec_()