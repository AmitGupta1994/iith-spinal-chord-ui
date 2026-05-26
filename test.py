import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class VideoPlayerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Video Player")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create a video widget
        self.video_widget = QVideoWidget()

        # Create a video player and set the video output
        self.video_player = QMediaPlayer()
        self.video_player.setVideoOutput(self.video_widget)

        # Create a play button
        self.play_button = QPushButton("Play Video")
        self.play_button.clicked.connect(self.play_video)

        # Add the video widget to the layout
        self.layout.addWidget(self.video_widget)

        # Add the play button to the layout
        self.layout.addWidget(self.play_button)

    def play_video(self):
        # Load and play a video file
        video_url = "path_to_your_video_file.mp4"  # Replace with the path to your video file
        media = QMediaContent(QUrl.fromLocalFile('/Users/amitgupta/PycharmProjects/iith-spinal-cord-ui/S17_Malasana.mp4'))
        self.video_player.setMedia(media)
        self.video_player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoPlayerApp()
    window.show()
    sys.exit(app.exec_())
