from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout #QVBoxLayout为竖直布局，QHBoxLayout为水平布局，QFormLayout为表单布局
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QLineEdit

import sys


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
        root_layout = QHBoxLayout()

        #col1
        col1_layout = QVBoxLayout()
        col1_layout.addWidget(QPushButton("按钮1"))

        #col2
        col2_layout = QVBoxLayout()
        col2_layout.addWidget(QPushButton("按钮1"))
        col2_layout.addWidget(QPushButton("按钮2"))

        #col3
        col3_layout = QVBoxLayout()
        col3_layout.addWidget(QPushButton("按钮1"))
        col3_layout.addWidget(QPushButton("按钮2"))
        col3_layout.addWidget(QPushButton("按钮3"))

        #col4
        col4_layout = QVBoxLayout()
        col4_layout.addWidget(QPushButton("按钮1"))
        col4_layout.addWidget(QPushButton("按钮2"))
        col4_layout.addWidget(QPushButton("按钮3"))
        col4_layout.addWidget(QPushButton("按钮4"))

        root_layout.addLayout(col1_layout)
        root_layout.addLayout(col2_layout)
        root_layout.addLayout(col3_layout)
        root_layout.addLayout(col4_layout)



        w.setLayout(root_layout)


        #3.显示窗口
        w.show()

        #鼠标悬浮提示
        w.setToolTip("鼠标气泡提示")

        #等待app停止
        sys.exit(app.exec_())

