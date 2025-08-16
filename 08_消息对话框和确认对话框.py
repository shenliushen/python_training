from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout #QVBoxLayout为竖直布局，QHBoxLayout为水平布局，QFormLayout为表单布局
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QLineEdit,QMessageBox

import sys

def userdelete():
        print("删除用户")
        result = QMessageBox.information(w,
                                         "删除提示","是否删除用户？",
                                         QMessageBox.Yes|QMessageBox.No,
                                         QMessageBox.No)
        if result == QMessageBox.Yes:
            print("用户已删除")
        else:
            print("用户未删除")
               





if __name__ == '__main__':
    
        #1.创建应用程序
        app = QApplication(sys.argv)

        #2.创建窗口
        w = QWidget()
        w.setWindowTitle("第一个qt标题")
        #设置窗口大小
        w.resize(1048,720)
        #-------------------------------------------表单布局 start 
        #创建表单布局
        root_layout = QVBoxLayout()
        but = QPushButton("删除")
        but.clicked.connect(userdelete)
        root_layout.addWidget(but)
        w.setLayout(root_layout)


        #3.显示窗口
        w.show()

        #鼠标悬浮提示
        w.setToolTip("鼠标气泡提示")

        #等待app停止
        sys.exit(app.exec_())

