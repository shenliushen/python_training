from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton     
import sys

class MyWidget(QWidget):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle("title")
        self.resize(400, 300)

        self.init_ui()

    def on_button_click(self):
        print("按钮被点击了")


    def init_ui(self):

        self.btn_send = QPushButton("按钮", self)
        self.btn_send.setGeometry(QtCore.QRect(140, 50, 75, 23))
        self.btn_send.clicked.connect(self.on_button_click)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget("窗口标题")
    w.show()

    sys.exit(app.exec_())
