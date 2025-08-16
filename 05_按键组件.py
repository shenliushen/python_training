from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton
import sys


#槽函数 slot函数不要直接调用，
@pyqtSlot
def button_clicked():
      print("火箭发射")


def _init_pixmap(w:QWidget):
    #-------------------------------------------单行文本排列 start 
    #创建垂直排列布局
    layout = QVBoxLayout()
    button = QPushButton()
    button.setText("发射")
    #1、关联函数，点击按钮后执行的函数
    # button.clicked.connect(button_clicked )
    #2、单行函数可用lambda
    # button.clicked.connect(lambda: print("火箭发射") )
    #3、直接调用系统quit函数
    button.clicked.connect(QApplication.quit )
    layout.addWidget(button)

    w.setLayout(layout)



if __name__ == '__main__':
    
        #1.创建应用程序
        app = QApplication(sys.argv)

        #2.创建窗口
        w = QWidget()
        w.setWindowTitle("第一个qt标题")
        #设置窗口大小
        # w.resize(1048,720)
        _init_pixmap(w)

        #3.显示窗口
        w.show()

        #鼠标悬浮提示
        w.setToolTip("鼠标气泡提示")

        #等待app停止
        sys.exit(app.exec_())

