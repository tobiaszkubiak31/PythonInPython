import logging
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QApplication
from qtconsole.qt import QtCore


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setGeometry(600,200,700,700)
        layout = QVBoxLayout()
        logging.basicConfig(level=logging.INFO)
        #:todo make transaperent and add new image
        #self.setStyleSheet("background-image: url(grahpics/background.jpg);")


        self.b1 = QPushButton("Start")
        self.b1.setMinimumHeight(100)
        self.b1.setMinimumWidth(200)
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(self.btnstart)
        layout.addWidget(self.b1,alignment=QtCore.Qt.AlignCenter)
        self.b1.setStyleSheet("""
                    QWidget {
                        border: 20px solid black;
                        border-radius: 10px;
                        background-color: yellow;
                        font-size:20px;
                        font-weight:bold;
                        selection-background-color:red;
                        
                        }
                    """)


        self.b2 = QPushButton("Exit")
        self.b2.setMinimumHeight(100)
        self.b2.setMinimumWidth(200)
        # self.b2.setIcon(QIcon(QPixmap("python.gif")))
        self.b2.clicked.connect(self.btnexit)
        layout.addWidget(self.b2,alignment=QtCore.Qt.AlignCenter)
        self.setLayout(layout)
        self.b2.setStyleSheet("""
            QWidget {
                border: 20px solid black;
                border-radius: 10px;
                background-color: yellow;
                font-size:20px;
                font-weight:bold
                }
            """)

        self.setWindowTitle("Snake")

    def btnstart(self):
        logging.info("Game Started")


    def btnexit(self):
        logging.info("Game Exit")


def main():
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()