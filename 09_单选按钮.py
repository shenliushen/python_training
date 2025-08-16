from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout #QVBoxLayout为竖直布局，QHBoxLayout为水平布局，QFormLayout为表单布局
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QLineEdit,QMessageBox,QRadioButton,QButtonGroup #QCheckBox为复选框，QRadioButton为单选按钮

import sys



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
        but1 = QRadioButton("男")
        but2 = QRadioButton("女")
        but1.clicked.connect(lambda: print("男被选中"))
        but2.clicked.connect(lambda: print("女被选中"))

        group = QButtonGroup()
        group.addButton(but1)
        group.addButton(but2)
        group.buttonToggled.connect(lambda btn,checked:print(btn.text() + "被选中" if checked else btn.text() + "被取消选中"))
        
        root_layout.addWidget(but1)
        root_layout.addWidget(but2)
        w.setLayout(root_layout)


        #3.显示窗口
        w.show()

        #鼠标悬浮提示
        w.setToolTip("鼠标气泡提示")

        #等待app停止
        sys.exit(app.exec_())

