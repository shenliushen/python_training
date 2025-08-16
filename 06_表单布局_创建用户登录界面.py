from PyQt5.QtWidgets import QApplication,QWidget,QFormLayout #QVBoxlayout为竖直布局，QHBoxlayout为水平布局，QFormlayout为表单布局
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QLineEdit

import sys

def print_user_info():
    print("用户名:", user_name.text())
    print("密码:", user_pas.text())
    print("确认密码:", user_confirm.text())


if __name__ == '__main__':
    
        #1.创建应用程序
        app = QApplication(sys.argv)

        #2.创建窗口
        w = QWidget()
        w.setWindowTitle("第一个qt标题")
        #设置窗口大小
        # w.resize(1048,720)
        #-------------------------------------------表单布局 start 
        #创建表单布局
        layout = QFormLayout()
        user_name = QLineEdit()
        user_pas = QLineEdit()
        user_pas.setEchoMode(QLineEdit.Password)  #设置密码输入模式
        user_confirm = QLineEdit()
        layout.addRow("用户名:", user_name)
        layout.addRow("密码:", user_pas)
        layout.addRow("确认密码:", user_confirm)


        button = QPushButton()
        button.setText("提交")
        button.clicked.connect(print_user_info )
        layout.addRow(button)

        w.setLayout(layout)


        #3.显示窗口
        w.show()

        #鼠标悬浮提示
        w.setToolTip("鼠标气泡提示")

        #等待app停止
        sys.exit(app.exec_())

