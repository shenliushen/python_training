from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QFormLayout #QVBoxLayout为竖直布局，QHBoxLayout为水平布局，QFormLayout为表单布局
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QLineEdit,QMessageBox,QRadioButton,QButtonGroup #QCheckBox为复选框，QRadioButton为单选按钮

import sys



if __name__ == '__main__':
    
        #1.创建应用程序
        app = QApplication(sys.argv)

        #2.创建窗口
        w = QWidget()
        w.setWindowTitle("注册登录")
        #设置窗口大小
        w.resize(1048,720)
        #-------------------------------------------表单布局 start 
        #创建表单布局
        root_layout = QFormLayout()
        user_name = QLineEdit()
        user_name.setPlaceholderText("请输入用户名")
        root_layout.addRow("用户名",user_name)
        user_password = QLineEdit()
        user_password.setPlaceholderText("请输入密码")
        root_layout.addRow("密码",user_password)

        sex_layout = QHBoxLayout()
        but1 =QRadioButton("男")
        but2 =QRadioButton("女")

        group = QButtonGroup()
        group.addButton(but1)
        group.addButton(but2)
        sex_layout.addWidget(but1)
        sex_layout.addWidget(but2)
 
        root_layout.addRow("性别:",sex_layout)

   



        w.setLayout(root_layout)


        #3.显示窗口
        w.show()

        #鼠标悬浮提示
        w.setToolTip("鼠标气泡提示")

        #等待app停止
        sys.exit(app.exec_())

