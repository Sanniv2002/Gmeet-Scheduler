import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTimeEdit, QPushButton, QMessageBox
from PySide6.QtCore import QTime, QTimer

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeSetterApp()
    window.show()
    sys.exit(app.exec_())
