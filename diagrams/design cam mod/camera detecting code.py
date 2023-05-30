import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import cv2


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the widgets
        self.label = QLabel('Welcome to the vein Detector')
        self.label.setStyleSheet("font-size: 24px;")

        self.setGeometry(200, 200, 800, 600)
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_camera)

        self.close_button = QPushButton('Close')
        self.close_button.clicked.connect(self.close)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

    def start_camera(self):
        self.label.setText('Camera is on')
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            self.resize(640, 480)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 