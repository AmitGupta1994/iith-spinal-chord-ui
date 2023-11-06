import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFrame, QHBoxLayout
from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5 import uic

class VerticalRectangles(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(300)  # Adjust the width as needed
        self.setAutoFillBackground(True)

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setBrush(QBrush(QColor(255, 0, 0)))  # Change the color as needed
    #     painter.drawRect(0, 0, 300, 50)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(255, 0, 0)))  # Change the color as needed
        painter.drawRect(0, 0, 300, 300)

        # Draw circles
        circle_radius = 20
        circle_spacing = 10
        circle_x = circle_radius + circle_spacing
        circle_y = self.height() // 2

        for _ in range(2):  # Two columns
            for _ in range(2):  # Two rows
                painter.setBrush(QBrush(QColor(0, 0, 255)))  # Change the circle color as needed
                painter.drawEllipse(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2,
                                    circle_radius * 2)
                circle_x += 2 * (circle_radius + circle_spacing)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file
        uic.loadUi("iith-spinal-chord-main.ui", self)

        # Get references to the buttons in the .ui file
        self.button1 = self.findChild(QPushButton, "button1")
        self.button2 = self.findChild(QPushButton, "button2")

        # Create a layout for the main window
        main_layout = QHBoxLayout()

        # Add the vertical rectangles widget to the left side
        vertical_rectangles = VerticalRectangles()
        main_layout.addWidget(vertical_rectangles)

        # Add the UI loaded from the .ui file to the main layout
        main_layout.addWidget(self.centralWidget())

        # Set the main layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect button signals to functions
        # self.button1.clicked.connect(self.button1_clicked)
        # self.button2.clicked.connect(self.button2_clicked)

    def button1_clicked(self):
        print("Button 1 clicked!")

    def button2_clicked(self):
        print("Button 2 clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
