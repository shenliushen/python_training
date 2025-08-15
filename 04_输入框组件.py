from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QPlainTextEdit
from PyQt5.QtGui import QPixmap
import sys

def _init_pixmap(w:QWidget):
    #-------------------------------------------单行文本排列 start 
    #创建垂直排列布局
    layout = QVBoxLayout()
    edit = QLineEdit( )

    #设置文本框内提示词
    edit.setPlaceholderText("请输入用户名")

    #设置文本最大长度
    edit.setMaxLength(10)
    layout.addWidget(edit)
    edit_pwd = QLineEdit( )     
    edit_pwd.setPlaceholderText("请输入密码")

    #设置密码的显示格式
    edit_pwd.setEchoMode(edit_pwd.Password)
    layout.addWidget(edit_pwd)

    #------------------------------------------- end 

    #-------------------------------------------多行文本排列
    plain_text = QPlainTextEdit()
    #文本框内预制
    plain_text.setPlainText("我是xxx。来自老百姓")
    #多行文本内提示词语
    plain_text.setPlaceholderText("请输入你的个人简介")
    layout.addWidget(plain_text)

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

