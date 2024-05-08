import sys
import tkinter as tk
from tkinter import ttk
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QStatusBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QTime, QTimer
from datetime import datetime

class TimeSetterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Setter and Trigger")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.current_time_label = QLabel()
        layout.addWidget(self.current_time_label)

        self.time_label = QLabel("Set the trigger time:")
        layout.addWidget(self.time_label)

        self.time_edit = QTimeEdit()
        layout.addWidget(self.time_edit)

        self.trigger_button = QPushButton("Start Trigger Timer")
        self.trigger_button.clicked.connect(self.start_trigger_timer)
        layout.addWidget(self.trigger_button)

        self.setLayout(layout)

        # Start a QTimer to update the current time every second
        self.current_time_timer = QTimer(self)
        self.current_time_timer.timeout.connect(self.update_current_time)
        self.current_time_timer.start(1000)  # Update every second

        self.trigger_timer = QTimer(self)
        self.trigger_timer.timeout.connect(self.check_trigger_time)

    def update_current_time(self):
        current_time = QTime.currentTime()
        self.current_time_label.setText(f"Current Time: {current_time.toString('hh:mm:ss')}")

    def start_trigger_timer(self):
        self.trigger_button.setEnabled(False)  # Disable the trigger button while the timer is running
        self.trigger_timer.start(1000)  # Start the trigger timer to check the trigger time every second

    def check_trigger_time(self):
        current_time = QTime.currentTime()
        set_time = self.time_edit.time()

        if current_time >= set_time:
            self.trigger_timer.stop()  # Stop the trigger timer after the trigger time is reached
            self.trigger_button.setEnabled(True)  # Enable the trigger button again
            self.show_trigger_message()

    def show_trigger_message(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Trigger Time Reached")
        message_box.setText("Trigger time reached!")
        message_box.exec_()


def get_time_period():
    current_time = datetime.now().time()

    if current_time.hour >= 5 and current_time.hour < 12:
        return "Morning"
    elif current_time.hour >= 12 and current_time.hour < 17:
        return "Noon"
    else:
        return "Evening"
    
def pyside6_window():
    app = QApplication(sys.argv)
    app.setStyle("fusion")

    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)

    window = QWidget()
    window.setWindowTitle("Google Meet Scheduler")
    window.setGeometry(100, 100, 600, 400)

    layout = QVBoxLayout()

    label = QLabel(f"Good {get_time_period()}")
    label.setStyleSheet("color: pink; font-size: 20px;")
    layout.addWidget(label)

    entry_label = QLabel("Meet Link")
    entry_label.setStyleSheet("color: white;")
    layout.addWidget(entry_label)


    entry_label = QLabel("Email ID")
    entry_label.setStyleSheet("color: white;")
    layout.addWidget(entry_label)

    entry_field = QLineEdit()
    layout.addWidget(entry_field)

    text_label = QLabel("Text Box:")
    text_label.setStyleSheet("color: white;")
    layout.addWidget(text_label)

    text_box = QTextEdit()
    layout.addWidget(text_box)

    button_pyside6 = QPushButton("Click Me (PySide6)")
    button_pyside6.clicked.connect(lambda: print(f"Entry Field: {entry_field.text()}\nText Box:\n{text_box.toPlainText()}"))
    layout.addWidget(button_pyside6)

    status_bar = QStatusBar()
    status_bar.showMessage("Status: Ready")
    layout.addWidget(status_bar)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    pyside6_window()
