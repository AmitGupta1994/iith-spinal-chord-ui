import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.uic import loadUi

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
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_l1= SpinalChordSegment("L1", self.segment_c8_muscles)

        # L2
        self.segment_c8_muscles = [
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

        main_layout = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

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

        # Add the UI loaded from the .ui file to the main layout
        main_layout.addWidget(self.centralWidget())

        # Set the main layout for the main window


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
