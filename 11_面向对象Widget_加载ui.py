from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton     
import sys
from ui.Ui_my_wedget import Ui_Form

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_ui()

    def on_button_click(self):
        print("按钮被点击了")


    def init_ui(self):
        self.ui.btn_send.clicked.connect(self.on_button_click)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()

    sys.exit(app.exec_())
