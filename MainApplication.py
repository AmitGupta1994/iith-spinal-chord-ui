import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

from SpinalChordMuscle import SpinalChordMuscle
from SpinalChordSegment import SpinalChordSegment


class MainApplication(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = loadUi("iith-spinal-chord-main.ui", self)

        self.setWindowTitle("Spinal Chord")

        # self.label_spinal_chord.setPixmap(QPixmap('white-bg.jpeg'))

        self.segment_c5_muscles = [
            SpinalChordMuscle('ercspn_l','Erector Spinae Left'), SpinalChordMuscle('ercspn_r','Erector Spinae Right'),
            SpinalChordMuscle('DELT1','Deltoid 1 Right'), SpinalChordMuscle('DELT2','Deltoid 1 Left'),

        ]
        self.segment_c5 = SpinalChordSegment("C2",self.segment_c5_muscles, [100, 20])
        # self.segment_c6 = SpinalChordSegment("C3",[],[100,500])

        # self.initialize_ui()

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
