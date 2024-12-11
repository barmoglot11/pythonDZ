from PySide6.QtWidgets import QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Загрузка файла")

        # Создаем виджет и layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Создаем кнопку
        self.button = QPushButton("Загрузить файл")
        self.button.clicked.connect(self.load_file)

        # Создаем метку для отображения имени файла
        self.label = QLabel("Выберите файл для загрузки")

        # Добавляем виджеты в layout
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

    def load_file(self):
        # Открываем диалог выбора файла
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*);;Текстовые файлы (*.txt)",
                                                   options=options)

        if file_name:
            # Если файл выбран, обновляем метку с именем файла
            self.label.setText(f"Выбранный файл: {file_name}")


# Запуск приложения
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
