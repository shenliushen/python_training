from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
import sys

#1.创建应用程序
app = QApplication(sys.argv)

#2.创建窗口
w = QWidget()
w.setWindowTitle("第一个qt标题")
#设置窗口大小
w.resize(1048,720)

#设置程序图标
# icon = QIcon("图片位置")
# w.setWindowIcon(icon)


#3.显示窗口
w.show()

#鼠标悬浮提示
w.setToolTip("鼠标气泡提示")

#等待app停止
sys.exit(app.exec_())

