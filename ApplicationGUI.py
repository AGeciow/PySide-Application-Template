# -------------------------------------------------------
# Import QtDesigner Components
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QTimer
from PySide6.QtWidgets import QLabel, QPushButton

# -------------------------------------------------------
# Init Application
MainApplication = QApplication([])

# -------------------------------------------------------
# Load UI from file
def loadWindow(windowFile):
    file = QFile(windowFile)
    file.open(QFile.ReadOnly)
    res = QUiLoader().load(file)
    file.close()
    return res

# -------------------------------------------------------
# Events functions


# -------------------------------------------------------
# Start Application
def ApplicationRun(Window):
    global MainApplication
    Window.show()
    MainApplication.exec()
