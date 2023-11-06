import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFrame, QHBoxLayout
from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5 import uic

class Rectangle(QWidget):
    def __init__(self,width,height):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setFixedWidth(width)  # Adjust the width as needed
        self.setFixedHeight(height)  # Adjust the width as needed

        # self.width = width
        # self.height = height

    def setColor(self, color):
        self.color = color
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(self.color))
        painter.drawRect(0, 0, self.width(), self.height())

class MyWindow(QMainWindow):
    def __init__(self, num_rectangles):
        super().__init__()

        # Load the .ui file
        uic.loadUi("iith-spinal-chord-main.ui", self)

        # Get references to the buttons in the .ui file
        self.button1 = self.findChild(QPushButton, "button1")
        self.button2 = self.findChild(QPushButton, "button2")

        # Create a layout for the main window
        main_layout = QVBoxLayout()

        # Create and add the rectangle widgets to the layout
        self.rectangles = []

        # for _ in range(num_rectangles):
        rectangle1 = Rectangle(40,100)
        rectangle2 = Rectangle(100, 400)
        rectangle3 = Rectangle(10, 100)

        self.rectangles.append(rectangle1)
        self.rectangles.append(rectangle2)
        self.rectangles.append(rectangle3)

        main_layout.addWidget(rectangle1)
        main_layout.addWidget(rectangle2)
        main_layout.addWidget(rectangle3)

        # Add the UI loaded from the .ui file to the main layout
        main_layout.addWidget(self.centralWidget())

        # Set the main layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect button signals to functions
        # self.button1.clicked.connect(self.button1_clicked)
        # self.button2.clicked.connect(self.button2_clicked)

        # Example of dynamically updating rectangle colors
        for index, rectangle in enumerate(self.rectangles):
            rectangle.setColor(QColor(255, 0, 0) if index % 2 == 0 else QColor(0, 0, 255))  # Alternate colors

    def button1_clicked(self):
        print("Button 1 clicked!")

    def button2_clicked(self):
        print("Button 2 clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    num_rectangles = 4  # Specify the number of rectangles
    window = MyWindow(num_rectangles)
    window.show()
    sys.exit(app.exec_())
