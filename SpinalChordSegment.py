from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QFont, QColor
from PyQt5.QtWidgets import QWidget


class SpinalChordSegment(QWidget):

    def __init__(self,name,muscles_name_list,position):
        super().__init__()

        self.setFixedWidth(80)  # Adjust the width as needed
        self.setAutoFillBackground(True)
        self.circle_color = QColor(0, 0, 255)  # Default circle color

        self.num_rows = int(len(muscles_name_list)/2)

        self.name = name
        self.muscles_name_list = muscles_name_list
        self.position = position

        # self.draw_segment()

        segment_x = self.position[0]
        segment_y = self.position[1]

        print("x,y",segment_x,segment_y)

        self.rect_x = segment_x
        self.rect_y = segment_y
        self.rect_width = 200

        # Calculate the height of the rectangle based on the number of circles
        circle_radius = 5
        circle_spacing = 10
        num_circles = len(muscles_name_list)/2
        self.rect_height = 2 * (circle_radius + circle_spacing) * (num_circles // 2)

    def setCircleColor(self, color):
        self.circle_color = color
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        rect_width = 200
        rect_height = self.rect_height

        painter.setBrush(QBrush(QColor(255, 0, 0)))  # Change the color of the rectangle as needed
        painter.drawRect(self.rect_x, self.rect_y, rect_width, rect_height)

        for row in range(self.num_rows):
            y = row * rect_height
            # painter.setBrush(QBrush(QColor(255, 0, 0)))  # Change the color of the rectangle as needed
            # painter.drawRect(self.rect_x, self.rect_y, rect_width, rect_height)

            # Draw circles inside the rectangle
            circle_radius = min(rect_width, rect_height) // 4
            circle_spacing = 10
            circle_x = circle_radius + circle_spacing
            circle_y = y + rect_height // 2

            for _ in range(2):
                painter.setBrush(QBrush(self.circle_color))  # Use the dynamic circle color
                painter.drawEllipse(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2,
                                    circle_radius * 2)
                circle_x += 2 * (circle_radius + circle_spacing)