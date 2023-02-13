import requests
from PySide6.QtWidgets import QMainWindow, QFileDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, app):

        super().__init__()
        self.app = app
        self.setWindowTitle("Excel Uploader")

        self.upload_button = QPushButton("Upload Excel File")
        self.upload_button.clicked.connect(self.upload_excel_file)

        self.file_label = QLabel("No file selected")

        layout = QVBoxLayout()
        layout.addWidget(self.upload_button)
        layout.addWidget(self.file_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def upload_excel_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xlsx *.xlsm *.xltx *.xltm)", options=options)
        if file_name:
            self.file_label.setText(file_name)
            with open(file_name, 'rb') as f:
                response = requests.post('https://your-website.com/upload-excel-file', files={'file': f})
                if response.status_code == 200:
                    self.file_label.setText("File uploaded successfully")
                else:
                    self.file_label.setText("File upload failed")

