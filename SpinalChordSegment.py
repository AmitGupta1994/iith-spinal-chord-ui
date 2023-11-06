from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QFont
from PyQt5.QtWidgets import QWidget


class SpinalChordSegment(QWidget):

    def __init__(self,name,muscles_name_list,position):
        super().__init__()

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

    def paintEvent(self, event):



        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the rectangle
        pen = QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)

        brush = QBrush(Qt.lightGray)
        painter.setBrush(brush)

        painter.drawRect(self.rect_x, self.rect_y, self.rect_width, self.rect_height)

        # Draw the text for the rectangle
        font = QFont("Arial", 14)
        painter.setFont(font)
        painter.drawText(self.rect_x + 20, self.rect_y + 20, "Rectangle")

        # Draw the circles
        for center in self.circle_centers:
            circle_x, circle_y = center
            painter.drawEllipse(circle_x - self.circle_radius, circle_y - self.circle_radius, 2 * self.circle_radius, 2 * self.circle_radius)

        # Draw text for each circle
        for i, center in enumerate(self.circle_centers):
            circle_x, circle_y = center
            painter.drawText(circle_x - 10, circle_y + 30, f"Circle {i + 1}")

    def draw_segment(self):
        print("draw")

        segment_x = self.position[0]
        segment_y = self.position[1]

        segment_length = 100
        segment_width = len(self.muscles_name_list)*100

        print("test: ",self.label_spinal_chord.pixmap())

        painter = QPainter(self.label_spinal_chord.pixmap())


        painter.setRenderHint(QPainter.Antialiasing)  # Optional, for smoother rendering

        # Set the pen (outline) and brush (fill) properties
        pen = QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)

        brush = QBrush(Qt.blue)
        painter.setBrush(brush)

        # Draw the rectangle
        painter.drawRect(segment_x, segment_y, segment_length, segment_width)

        self.label_spinal_chord.update()


    def update_segment(self):
        pass