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


        self.segment_c5_muscles = [
            SpinalChordMuscle('ercspn_l','Erector Spinae Left'), SpinalChordMuscle('ercspn_r','Erector Spinae Right'),
            SpinalChordMuscle('DELT1','Deltoid 1 Right'), SpinalChordMuscle('DELT2','Deltoid 1 Left'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_c5 = SpinalChordSegment("C5",self.segment_c5_muscles, [10, 20])

        self.segment_c6_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1', 'Deltoid 1 Right'), SpinalChordMuscle('DELT2', 'Deltoid 1 Left'),

        ]
        self.segment_c6 = SpinalChordSegment("C6",self.segment_c6_muscles,[0,100])

        ####################################
        # Create a layout for the main window
        self.segments = []

        main_layout = QVBoxLayout()

        self.segments.append(self.segment_c5)
        self.segments.append(self.segment_c6)

        main_layout.addWidget(self.segment_c5)
        main_layout.addWidget(self.segment_c6)

        # Set the main layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


        ####################################
        # Create a layout for the main window
        main_layout = QHBoxLayout()

        # Add the vertical rectangles widget to the left side
        # main_layout.addWidget(self.segment_c5)
        main_layout.addWidget(self.segment_c6)

        # Add the UI loaded from the .ui file to the main layout
        main_layout.addWidget(self.centralWidget())

        # Set the main layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

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
