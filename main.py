from ApplicationGUI import *

import time

# -------------------------------------------------------
# Application Init
MainWindow = loadWindow('MainWindow.ui')
MainWindow.setWindowTitle("PySide Application Template version: 0.0.1")     # Set Window Title
MainWindow.setMinimumSize(850, 550) 

# -------------------------------------------------------
# Init Components
Widget_Clock = MainWindow.findChild(QLabel, "lb_Clock")
Widget_ClockZero = MainWindow.findChild(QPushButton, "pb_ClockZero")

# -------------------------------------------------------
# Functions
def ClockUpdate(widget):
    global time
    widget.setText(time.strftime("%H:%M:%S"))

def ClockZero(widget):
    widget.setText("00:00:00")

# -------------------------------------------------------
# Tasks functions definitions
def task_ClockUpdate():
    global Widget_Clock
    ClockUpdate(Widget_Clock)

# -------------------------------------------------------
# Events functions definitions
def Event_Button_ClockZero_onClick():
    global Widget_Clock
    ClockZero(Widget_Clock)

# -------------------------------------------------------
# Events functions assignment (with args)
Widget_ClockZero.clicked.connect(Event_Button_ClockZero_onClick)

# -------------------------------------------------------
# Tasks Initialization
task_Clock = QTimer()
task_Clock.timeout.connect(task_ClockUpdate)
task_Clock.start(1000)

# -------------------------------------------------------
# Start init
ClockUpdate(Widget_Clock)

# -------------------------------------------------------
# Run Application
ApplicationRun(MainWindow)
