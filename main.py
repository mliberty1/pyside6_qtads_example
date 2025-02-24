# Adapted from https://github.com/mborgerson/Qt-Advanced-Docking-System/blob/pyside6/examples/simple/main.py


import os
import sys
print(list(sorted(sys.modules.keys())))
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QMenuBar, QMenu, QStatusBar, QSizePolicy
from PySide6QtAds import CDockManager, CDockWidget, TopDockWidgetArea
# from PySide6QtAds.PySide6QtAds.ads import CDockManager, CDockWidget, TopDockWidgetArea
for module_name in list(sorted(sys.modules.keys())):
    module = sys.modules[module_name]
    if hasattr(module, '__path__'):
        path = module.__path__
    else:
        path = ''
    print(f'  {module_name} {path}')


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PySide6-QtAds Main Window')
 
        # Create the dock manager. Because the parent parameter is a QMainWindow
        # the dock manager registers itself as the central widget.
        self.dock_manager = CDockManager(self)
        
        # Create example content label - this can be any application specific
        # widget
        l = QLabel()
        l.setWordWrap(True)
        l.setAlignment(Qt.AlignTop | Qt.AlignLeft);
        l.setText("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. ")

        # Create a dock widget with the title Label 1 and set the created label
        # as the dock widget content
        dock_widget = CDockWidget("Label 1")
        dock_widget.setWidget(l)
        
        # Add the dock widget to the top dock widget area
        self.dock_manager.addDockWidget(TopDockWidgetArea, dock_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = MainWindow()
    w.show()
    app.exec_()
