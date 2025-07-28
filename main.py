import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaz_modernita import Ui_MainWindow  # El archivo generado desde el .ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar eventos
        self.ui.btnHome.clicked.connect(self.mostrar_inicio)
        self.ui.btnSettings.clicked.connect(self.mostrar_configuracion)

    def mostrar_inicio(self):
        self.ui.labelTitle.setText("Estás en Inicio 🏠")
        self.ui.listContent.clear()
        self.ui.listContent.addItems(["Canción 1", "Canción 2", "Canción 3"])

    def mostrar_configuracion(self):
        self.ui.labelTitle.setText("Configuración ⚙️")
        self.ui.listContent.clear()
        self.ui.listContent.addItems(["Ajuste 1", "Ajuste 2", "Modo oscuro"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
