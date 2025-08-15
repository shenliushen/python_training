from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QPixmap
import sys

def _init_pixmap(w:QWidget):
     #-------------------------------------------组件初始配置 start 
    label = QLabel()
    Pixmap = QPixmap("./img.png")#这里填写图片的路径
    label.setPixmap(Pixmap)
    #将创建的窗口设置为标签的父类
    label.setParent(w)
    #根据图片大小设置窗口大小
    w.resize(Pixmap.width(),Pixmap.height())
    #-------------------------------------------组件初始配置 end 


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

