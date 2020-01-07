import logging
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QLabel, QWidget, QLineEdit, QPushButton, QHBoxLayout
from snake_game.application import Application


class Launcher(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FANTASTIC MULTIPLAYER SNAKE GAME")
        self.setGeometry(600, 200, 700, 700)

        self.layout = None

        self.center_widget = None
        self.center_widget_layout = None

        self.address_widget = None
        self.address_layout = None

        self.set_ip_label = None
        self.ip_text_field = None
        self.set_port_label = None
        self.port_text_field = None

        self.connect_button = None
        self.start_button = None
        self.exit_button = None

        self.app = Application()

        self.init_UI()

    def init_UI(self):
        self.layout = QVBoxLayout()

        self.center_widget = QWidget()
        self.center_widget_layout = QVBoxLayout()
        self.center_widget.setLayout(self.center_widget_layout)

        self.set_ip_label = QLabel("IP:")
        self.set_port_label = QLabel("PORT:")
        self.ip_text_field = QLineEdit()
        self.port_text_field = QLineEdit()
        self.port_text_field.setMaximumWidth(50)

        self.address_widget = QWidget()
        self.address_layout = QHBoxLayout()
        self.address_widget.setLayout(self.address_layout)
        self.address_widget.setMaximumWidth(250)

        self.address_layout.addWidget(self.set_ip_label)
        self.address_layout.addWidget(self.ip_text_field)
        self.address_layout.addWidget(self.set_port_label)
        self.address_layout.addWidget(self.port_text_field)

        self.center_widget_layout.addWidget(self.address_widget)

        self.connect_button = QPushButton("CONNECT")
        self.connect_button.setMinimumHeight(100)
        self.connect_button.setMinimumWidth(250)
        self.connect_button.clicked.connect(self.button_connect)
        self.connect_button.setStyleSheet(
                        """QWidget {
                               border: 20px solid black;
                               border-radius: 10px;
                               background-color: yellow;
                               font-size:20px;
                               font-weight:bold;
                               selection-background-color:red;
                            }"""
        )

        self.start_button = QPushButton("START")
        self.start_button.setMinimumHeight(100)
        self.start_button.setMinimumWidth(250)
        self.start_button.clicked.connect(self.button_start)
        self.start_button.setDisabled(True)
        self.start_button.setStyleSheet(
                        """QWidget {
                               border: 20px solid black;
                               border-radius: 10px;
                               background-color: yellow;
                               font-size:20px;
                               font-weight:bold;
                               selection-background-color:red;
                            }"""
        )

        self.exit_button = QPushButton("EXIT")
        self.exit_button.setMinimumHeight(100)
        self.exit_button.setMinimumWidth(250)
        self.exit_button.clicked.connect(self.button_exit)
        self.exit_button.setStyleSheet(
                        """QWidget {
                               border: 20px solid black;
                               border-radius: 10px;
                               background-color: yellow;
                               font-size:20px;
                               font-weight:bold;
                               selection-background-color:red;
                            }"""
        )

        self.center_widget_layout.addWidget(self.connect_button, alignment=QtCore.Qt.AlignCenter)
        self.center_widget_layout.addWidget(self.start_button, alignment=QtCore.Qt.AlignCenter)
        self.center_widget_layout.addWidget(self.exit_button, alignment=QtCore.Qt.AlignCenter)

        self.layout.addWidget(self.center_widget, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def button_connect(self):
        self.app.establish_network(port=5556)
        ip = self.ip_text_field.text()
        port = self.port_text_field.text()
        port = int(port)
        self.app.connect_to_peer(ip, port)
        self.start_button.setDisabled(False)

    def button_start(self):
        self.app.set_environment()
        self.app.set_snake_color((0, 255, 255))
        self.close()
        self.app.launch_game()

    def button_exit(self):
        self.close()


def main():
    logging.basicConfig(level=logging.INFO)
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
