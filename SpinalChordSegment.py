from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QFont, QColor
from PyQt5.QtWidgets import QWidget


class SpinalChordSegment(QWidget):

    def __init__(self, name, muscles_name_list):
        super().__init__()

        self.name = name
        self.muscles_name_list = muscles_name_list

        self.rect_width = 600

        # Calculate the height of the rectangle based on the number of circles
        self.circle_radius = 3.5
        self.circle_spacing = 6
        self.num_circles = 2
        # self.circle_y = 0
        self.circle_y = 4
        num_of_rows = len(muscles_name_list) / 2 + 1

        print('num_of_rows', num_of_rows)

        self.rect_height = int(2 * (self.circle_radius + self.circle_spacing) * (num_of_rows // 2))

        self.setFixedWidth(self.rect_width)  # Adjust the width as needed
        self.setFixedHeight(self.rect_height)  # Adjust the width as needed

        self.setAutoFillBackground(True)
        self.circle_color = QColor(255, 255, 255)  # Default circle color

        self.num_rows = int(len(muscles_name_list) / 2)

    # def muscles_name_list_data(self,muscles_name_list):
    #     self.muscles_name_list = muscles_name_list

    def update_segment(self):
        self.update()

    def setColor(self, color):
        self.color = color
        self.update()  # Trigger a repaint

    def setCircleColor(self, color):
        self.circle_color = color
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(QBrush(QColor(255, 255, 255)))  # Change the color of the rectangle as needed
        painter.drawRect(0, 0, self.width(), self.height())

        font = QFont("Arial", 10)  # Adjust the font as needed
        painter.setFont(font)
        text_rect = painter.boundingRect(self.rect(), 0, self.name)
        text_x = (self.width() - text_rect.width()) / 2
        text_y = (self.height() + text_rect.height()) / 2
        painter.drawText(text_x, text_y, self.name)

        # For Circles Inside
        # Calculate circle properties

        # Draw circles in rows
        count = 0

        for row in range(self.num_rows):
            circle_x = self.circle_spacing + self.circle_radius + 200

            # Draw the name of the first circle to the left of the circle
            circle_color_value = self.muscles_name_list[count].value

            circle_color = QColor(circle_color_value, 0, 0)

            circle_name = self.muscles_name_list[count].desc
            circle_name_font = QFont("Arial", 8)  # Adjust the font as needed
            painter.setFont(circle_name_font)
            circle_name_rect = painter.boundingRect(self.rect(), 0, circle_name)
            circle_name_x = circle_x - 10
            circle_name_y = self.circle_y + row * self.height() / self.num_rows + self.circle_y
            painter.drawText(circle_name_x - circle_name_rect.width(), circle_name_y, circle_name)

            # Draw the first circle
            painter.setBrush(QBrush(circle_color))  # Circle color
            painter.drawEllipse(circle_x, self.circle_y + row * self.height() / self.num_rows, 2 * self.circle_radius,
                                2 * self.circle_radius)

            # Draw the name of the second circle to the right of the circle
            circle_color_value = self.muscles_name_list[count+1].value

            circle_color = QColor(circle_color_value, 0, 0)

            circle_name = self.muscles_name_list[count + 1].desc
            circle_name_font = QFont("Arial", 8)  # Adjust the font as needed
            painter.setFont(circle_name_font)
            circle_name_rect = painter.boundingRect(self.rect(), 0, circle_name)
            circle_name_x = circle_x - (circle_name_rect.width() - 2 * self.circle_radius) / 2
            circle_name_y = self.circle_y + row * self.height() / self.num_rows + self.circle_y
            painter.drawText(circle_x + 20 * (self.circle_radius + self.circle_spacing), circle_name_y, circle_name)

            # Draw the second circle
            painter.setBrush(QBrush(circle_color))  # Circle color
            painter.drawEllipse(circle_x + 18 * (self.circle_radius + self.circle_spacing),
                                self.circle_y + row * self.height() / self.num_rows, 2 * self.circle_radius,
                                2 * self.circle_radius)

            count = count + 2

        # for row in range(self.num_rows):
        #     y = row * self.height()
        #     # painter.setBrush(QBrush(QColor(255, 0, 0)))  # Change the color of the rectangle as needed
        #     # painter.drawRect(self.rect_x, self.rect_y, rect_width, rect_height)
        #
        #     # Draw circles inside the rectangle
        #     circle_radius = min(self.width(), self.height()) // 4
        #     circle_spacing = 10
        #     circle_x = circle_radius + circle_spacing
        #     circle_y = y + self.height() // 2
        #
        #     for _ in range(2):
        #         painter.setBrush(QBrush(self.circle_color))  # Use the dynamic circle color
        #         painter.drawEllipse(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2,
        #                             circle_radius * 2)
        #         circle_x += 2 * (circle_radius + circle_spacing)
