import random
import sys

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QVBoxLayout, QScrollArea, QPushButton
from PyQt5.uic import loadUi
from PyQt5.uic.uiparser import QtCore

from SpinalChordMuscle import SpinalChordMuscle
from SpinalChordSegment import SpinalChordSegment


class MainApplication(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = loadUi("iith-spinal-chord-main.ui", self)

        self.setWindowTitle("Spinal Chord")

        # C5
        self.segment_c5_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1_l', 'Deltoid 1 Left'), SpinalChordMuscle('DELT1', 'Deltoid 1 Right'),
            SpinalChordMuscle('DELT2_l', 'Deltoid 2 Left'), SpinalChordMuscle('DELT2', 'Deltoid 2 Right'),
            SpinalChordMuscle('DELT3_l', 'Deltoid 3 Left'), SpinalChordMuscle('DELT3', 'Deltoid 3 Right'),
            SpinalChordMuscle('INFSP_l', 'Infraspinatus Left'), SpinalChordMuscle('INFSP', 'Infraspinatus Right'),
            SpinalChordMuscle('SUPSP_l', 'Supraspinatus Left'), SpinalChordMuscle('SUPSP', 'Supraspinatus Right'),
            SpinalChordMuscle('TMIN_l', 'Teres Minor Left'), SpinalChordMuscle('TMIN', 'Teres Minor Right'),
            SpinalChordMuscle('BIClong_l', 'Biceps Brachii Long Head Left'), SpinalChordMuscle('BIClong', 'Biceps Brachii Long Head Right'),
            SpinalChordMuscle('BICshort_l', 'Biceps Brachii Short Head Left'), SpinalChordMuscle('BICshort', 'Biceps Brachii Short Head Right'),
            SpinalChordMuscle('CORB_l', 'Corachobrachialis Left'), SpinalChordMuscle('CORB', 'Corachobrachialis Right'),
            SpinalChordMuscle('PECM1_l', 'Pectoralis Major 1 Left'), SpinalChordMuscle('PECM1', 'Pectoralis Major 1 Right'),
            SpinalChordMuscle('PECM2_l', 'Pectoralis Major 2 Left'), SpinalChordMuscle('PECM2', 'Pectoralis Major 2 Right'),
            SpinalChordMuscle('PECM3_l', 'Pectoralis Major 2 Left'), SpinalChordMuscle('PECM3', 'Pectoralis Major 2 Right'),

        ]
        self.segment_c5 = SpinalChordSegment("C5", self.segment_c5_muscles)

        # C6
        self.segment_c6_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_c6 = SpinalChordSegment("C6", self.segment_c6_muscles)

        # C7
        self.segment_c7_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_c7 = SpinalChordSegment("C7", self.segment_c7_muscles)

        # C8
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_c8 = SpinalChordSegment("C8", self.segment_c8_muscles)

        # T7-T12
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_t7_t12 = SpinalChordSegment("T7-T12", self.segment_c8_muscles)

        # L1
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
        ]
        self.segment_l1= SpinalChordSegment("L1", self.segment_c8_muscles)

        # L2
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_l2 = SpinalChordSegment("L2", self.segment_c8_muscles)

        # L3
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_l3= SpinalChordSegment("L3", self.segment_c8_muscles)

        # L4
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_l4 = SpinalChordSegment("L4", self.segment_c8_muscles)

        # L5
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_l5 = SpinalChordSegment("L5", self.segment_c8_muscles)

        # S1
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_s1 = SpinalChordSegment("S1", self.segment_c8_muscles)

        # S2
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_s2 = SpinalChordSegment("S2", self.segment_c8_muscles)

        ####################################
        # Create a layout for the main window
        self.segments = []

        # # Create a scrollable area
        # scroll_area = QScrollArea()
        # scroll_area.setWidgetResizable(True)

        main_layout = QVBoxLayout()

        # Create a widget to hold the rectangles
        rectangles_widget = QWidget()
        rectangles_layout = QVBoxLayout(rectangles_widget)


        self.segments.append(self.segment_c5)
        self.segments.append(self.segment_c6)
        self.segments.append(self.segment_c7)
        self.segments.append(self.segment_c8)
        self.segments.append(self.segment_c8)
        self.segments.append(self.segment_t7_t12)
        self.segments.append(self.segment_l1)
        self.segments.append(self.segment_l2)
        self.segments.append(self.segment_l3)
        self.segments.append(self.segment_l4)
        self.segments.append(self.segment_l5)
        self.segments.append(self.segment_s1)
        self.segments.append(self.segment_s2)

        # Get references to the buttons in the .ui file
        self.button1 = self.findChild(QPushButton, "activity1")
        self.button2 = self.findChild(QPushButton, "activity2")
        self.button3 = self.findChild(QPushButton, "activity3")
        self.button4 = self.findChild(QPushButton, "activity4")

        # Create a layout for the main window
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Create a horizontal layout for the buttons at the top
        buttons_layout = QHBoxLayout()

        # Add the buttons to the buttons layout
        buttons_layout.addWidget(self.button1)
        buttons_layout.addWidget(self.button2)
        buttons_layout.addWidget(self.button3)
        buttons_layout.addWidget(self.button4)

        # Add the buttons layout to the main layout
        main_layout.addLayout(buttons_layout)

        main_layout.addWidget(self.segment_c5)
        main_layout.addWidget(self.segment_c6)
        main_layout.addWidget(self.segment_c7)
        main_layout.addWidget(self.segment_c8)
        main_layout.addWidget(self.segment_t7_t12)
        main_layout.addWidget(self.segment_l1)
        main_layout.addWidget(self.segment_l2)
        main_layout.addWidget(self.segment_l3)
        main_layout.addWidget(self.segment_l4)
        main_layout.addWidget(self.segment_l5)
        main_layout.addWidget(self.segment_s1)
        main_layout.addWidget(self.segment_s2)



        # Set the main layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Update Every 1 second
        self.color_timer = QTimer(self)
        self.color_timer.timeout.connect(self.updateColors)
        self.color_timer.start(1000)  # 1000 ms (1 second) interval

    def updateColors(self):

        # TODO Loop for the ROW in the File to be Provided
        for segment in self.segments:
            for muscles in segment.muscles_name_list:
                muscles.value = random.randint(0, 3)

            segment.update_segment()

    def initialize_ui(self):
        # self.ui.layout.addWidget(self.segment_c5)
        self.setCentralWidget(self.segment_c5)
        # self.setCentralWidget(self.segment_c6)

        pass


# Run the App
def main():
    app = QApplication(sys.argv)
    window = MainApplication()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
