from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QFont, QColor
from PyQt5.QtWidgets import QWidget


class SpinalChordSegment(QWidget):

    def __init__(self,name,muscles_name_list,position):
        super().__init__()

        self.setFixedWidth(100)  # Adjust the width as needed
        self.setAutoFillBackground(True)
        self.circle_color = QColor(0, 0, 255)  # Default circle color

        self.name = name
        self.muscles_name_list = muscles_name_list
        self.position = position

        # self.draw_segment()

        segment_x = self.position[0]
        segment_y = self.position[1]

        segment_length = 100
        segment_width = len(self.muscles_name_list) * 4

        self.rect_x = segment_x
        self.rect_y = segment_y
        self.rect_width = segment_length
        self.rect_height = segment_width

        # self.rect_x = 50
        # self.rect_y = 50
        # self.rect_width = 300
        # self.rect_height = 200

        self.circle_centers = [(100, 100), (200, 150), (250, 100)]
        self.circle_radius = 4

    def setCircleColor(self, color):
        self.circle_color = color
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(255, 0, 0)))  # Change the color of the rectangle as needed
        painter.drawRect(0, 0, self.width(), self.height())

        # Draw circles
        circle_radius = 20
        circle_spacing = 10
        circle_x = circle_radius + circle_spacing
        circle_y = self.height() // 2

        for _ in range(2):  # Two columns
            for _ in range(2):  # Two rows
                painter.setBrush(QBrush(self.circle_color))  # Use the dynamic circle color
                painter.drawEllipse(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2,
                                    circle_radius * 2)
                circle_x += 2 * (circle_radius + circle_spacing)