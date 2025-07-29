import sys
import psutil
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                               QHBoxLayout, QWidget, QLabel, QProgressBar, 
                               QFrame, QFileDialog, QMessageBox, QListWidget,
                               QListWidgetItem, QSplitter)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPixmap, QAction
from interfaz_main import Ui_MainWindow  # El archivo generado desde interfaz_main.ui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from storage_utils import StorageAnalyzer, FileOrganizer

class StorageWidget(QWidget):
    """Widget personalizado para mostrar información de almacenamiento"""
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.update_storage_info()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # Información del sistema
        self.create_system_info()
        layout.addWidget(self.system_info_frame)
        
        # Gráfica de barras
        self.create_chart()
        layout.addWidget(self.canvas)
        
        # Información detallada de discos
        self.create_disk_details()
        layout.addWidget(self.disk_details_frame)
    
    def create_system_info(self):
        """Crear widget de información del sistema"""
        self.system_info_frame = QFrame()
        self.system_info_frame.setFrameStyle(QFrame.Box)
        self.system_info_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
                background-color: #ebf5ff;
            }
        """)
        
        layout = QHBoxLayout(self.system_info_frame)
        
        # Información del sistema
        system_info = StorageAnalyzer.get_system_info()
        
        info_labels = [
            f"💻 CPU: {system_info['cpu_count']} núcleos",
            f"🧠 RAM: {StorageAnalyzer.format_bytes(system_info['memory_total'])}",
            f"📀 Discos: {system_info['disk_count']} unidades",
            f"📊 Uso RAM: {system_info['memory_percent']:.1f}%"
        ]
        
        for info in info_labels:
            label = QLabel(info)
            label.setFont(QFont("Arial", 10, QFont.Bold))
            label.setStyleSheet("color: #2c3e50; padding: 5px;")
            layout.addWidget(label)
    
    def create_chart(self):
        """Crear gráfica de matplotlib"""
        self.figure = Figure(figsize=(12, 6))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumHeight(300)
        self.ax = self.figure.add_subplot(111)
    
    def create_disk_details(self):
        """Crear área de detalles de discos"""
        self.disk_details_frame = QFrame()
        self.disk_details_layout = QVBoxLayout(self.disk_details_frame)
    
    def update_storage_info(self):
        """Actualizar información de almacenamiento"""
        # Limpiar layout anterior de detalles
        for i in reversed(range(self.disk_details_layout.count())):
            widget = self.disk_details_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        
        # Obtener información de discos
        disk_data = StorageAnalyzer.get_disk_usage()
        
        # Crear widgets para cada disco
        for disk in disk_data:
            disk_widget = self.create_disk_widget(disk)
            self.disk_details_layout.addWidget(disk_widget)
        
        # Actualizar gráfica
        self.update_chart(disk_data)
        
        # Actualizar información del sistema
        self.update_system_info()
    
    def update_system_info(self):
        """Actualizar información del sistema"""
        # Limpiar layout anterior
        for i in reversed(range(self.system_info_frame.layout().count())):
            widget = self.system_info_frame.layout().itemAt(i).widget()
            if widget:
                widget.setParent(None)
        
        # Crear nueva información
        system_info = StorageAnalyzer.get_system_info()
        
        info_labels = [
            f"💻 CPU: {system_info['cpu_count']} núcleos",
            f"🧠 RAM: {StorageAnalyzer.format_bytes(system_info['memory_total'])}",
            f"📀 Discos: {system_info['disk_count']} unidades",
            f"📊 Uso RAM: {system_info['memory_percent']:.1f}%"
        ]
        
        for info in info_labels:
            label = QLabel(info)
            label.setFont(QFont("Arial", 10, QFont.Bold))
            label.setStyleSheet("color: #2c3e50; padding: 5px;")
            self.system_info_frame.layout().addWidget(label)
    
    def create_disk_widget(self, disk_info):
        """Crear widget individual para cada disco"""
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box)
        frame.setStyleSheet("""
            QFrame {
                border: 2px solid #cccccc;
                border-radius: 10px;
                padding: 10px;
                margin: 5px;
                background-color: #f9f9f9;
            }
        """)
        
        layout = QVBoxLayout(frame)
        
        # Información del disco
        info_layout = QHBoxLayout()
        
        # Nombre del disco
        name_label = QLabel(f"💾 {disk_info['device']}")
        name_label.setFont(QFont("Arial", 12, QFont.Bold))
        info_layout.addWidget(name_label)
        
        # Tipo de sistema de archivos
        fs_label = QLabel(f"({disk_info['fstype']})")
        fs_label.setStyleSheet("color: #666666;")
        info_layout.addWidget(fs_label)
        
        info_layout.addStretch()
        layout.addLayout(info_layout)
        
        # Barra de progreso
        progress = QProgressBar()
        progress.setMaximum(100)
        progress.setValue(int(disk_info['percent']))
        
        # Color de la barra según el porcentaje
        if disk_info['percent'] > 90:
            color = "#e74c3c"  # Rojo
        elif disk_info['percent'] > 70:
            color = "#f39c12"  # Naranja
        else:
            color = "#27ae60"  # Verde
            
        progress.setStyleSheet(f"""
            QProgressBar {{
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
                font-weight: bold;
            }}
            QProgressBar::chunk {{
                background-color: {color};
                border-radius: 3px;
            }}
        """)
        layout.addWidget(progress)
        
        # Información detallada
        details_layout = QHBoxLayout()
        
        used_label = QLabel(f"Usado: {StorageAnalyzer.format_bytes(disk_info['used'])}")
        free_label = QLabel(f"Libre: {StorageAnalyzer.format_bytes(disk_info['free'])}")
        total_label = QLabel(f"Total: {StorageAnalyzer.format_bytes(disk_info['total'])}")
        
        used_label.setStyleSheet("color: #e74c3c; font-weight: bold;")
        free_label.setStyleSheet("color: #27ae60; font-weight: bold;")
        total_label.setStyleSheet("color: #3498db; font-weight: bold;")
        
        details_layout.addWidget(used_label)
        details_layout.addWidget(free_label)
        details_layout.addWidget(total_label)
        
        layout.addLayout(details_layout)
        
        return frame
    
    def update_chart(self, disk_data):
        """Actualizar gráfica de barras"""
        self.ax.clear()
        
        if not disk_data:
            self.ax.text(0.5, 0.5, 'No hay datos de disco disponibles', 
                        ha='center', va='center', transform=self.ax.transAxes)
            self.canvas.draw()
            return
        
        # Preparar datos
        names = [disk['device'] for disk in disk_data]
        used_gb = [disk['used'] / (1024**3) for disk in disk_data]
        free_gb = [disk['free'] / (1024**3) for disk in disk_data]
        
        # Crear gráfica de barras apiladas
        width = 0.6
        x_pos = range(len(names))
        
        bars1 = self.ax.bar(x_pos, used_gb, width, label='Usado', color='#e74c3c', alpha=0.8)
        bars2 = self.ax.bar(x_pos, free_gb, width, bottom=used_gb, label='Libre', color='#27ae60', alpha=0.8)
        
        # Configurar gráfica
        self.ax.set_xlabel('Discos', fontsize=12, fontweight='bold')
        self.ax.set_ylabel('Espacio (GB)', fontsize=12, fontweight='bold')
        self.ax.set_title('Uso de Almacenamiento por Disco', fontsize=14, fontweight='bold')
        self.ax.set_xticks(x_pos)
        self.ax.set_xticklabels(names)
        self.ax.legend()
        self.ax.grid(True, alpha=0.3)
        
        # Añadir etiquetas de valores
        for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
            height1 = bar1.get_height()
            height2 = bar2.get_height()
            
            # Etiqueta para espacio usado
            if height1 > 10:
                self.ax.text(bar1.get_x() + bar1.get_width()/2., height1/2,
                           f'{height1:.0f}GB', ha='center', va='center', 
                           color='white', fontweight='bold')
            
            # Etiqueta para espacio libre
            if height2 > 10:
                self.ax.text(bar2.get_x() + bar2.get_width()/2., height1 + height2/2,
                           f'{height2:.0f}GB', ha='center', va='center', 
                           color='white', fontweight='bold')
        
        self.figure.tight_layout()
        self.canvas.draw()

class FolderAnalyzerWidget(QWidget):
    """Widget para analizar carpetas específicas"""
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Título
        title = QLabel("📁 Analizador de Carpetas")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Área de contenido
        content_label = QLabel("Selecciona una carpeta para analizar su contenido...")
        content_label.setAlignment(Qt.AlignCenter)
        content_label.setStyleSheet("color: #7f8c8d; font-size: 14px; padding: 50px;")
        layout.addWidget(content_label)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Configurar ventana
        self.setWindowTitle("Stroge - Administrador de Almacenamiento")
        self.setMinimumSize(1200, 800)
        
        # Crear widgets personalizados
        self.storage_widget = StorageWidget()
        self.folder_analyzer_widget = FolderAnalyzerWidget()
        
        # Configurar timer para actualización automática
        self.timer = QTimer()
        self.timer.timeout.connect(self.auto_refresh)
        self.timer.start(30000)  # Actualizar cada 30 segundos
        
        # Conectar eventos de botones
        self.ui.btnHome.clicked.connect(self.mostrar_dashboard)
        self.ui.btnAnalyzer.clicked.connect(self.mostrar_analizador)
        self.ui.btnOrganizer.clicked.connect(self.mostrar_organizador)
        self.ui.btnTags.clicked.connect(self.mostrar_etiquetas)
        self.ui.btnCleanup.clicked.connect(self.mostrar_limpieza)
        self.ui.btnSettings.clicked.connect(self.mostrar_configuracion)
        self.ui.btnAbout.clicked.connect(self.mostrar_acerca_de)
        
        # Conectar acciones del menú
        self.ui.actionAbrir_Carpeta.triggered.connect(self.abrir_carpeta)
        self.ui.actionActualizar.triggered.connect(self.actualizar_datos)
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionAcerca_de.triggered.connect(self.mostrar_acerca_de)
        
        # Configurar barra de estado
        self.ui.statusbar.showMessage("Listo - Stroge v1.0", 0)
        
        # Mostrar dashboard por defecto
        self.mostrar_dashboard()
    
    def clear_content_area(self):
        """Limpiar el área de contenido"""
        # Obtener el layout del área de scroll
        scroll_layout = self.ui.scrollAreaWidgetContents.layout()
        
        # Remover todos los widgets
        for i in reversed(range(scroll_layout.count())):
            widget = scroll_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
    
    def mostrar_dashboard(self):
        """Mostrar el dashboard principal con información de almacenamiento"""
        self.ui.labelTitle.setText("📊 Dashboard de Almacenamiento")
        self.clear_content_area()
        
        # Añadir el widget de almacenamiento al área de scroll
        self.ui.scrollAreaWidgetContents.layout().addWidget(self.storage_widget)
        self.storage_widget.show()
        
        # Actualizar datos
        self.storage_widget.update_storage_info()
        
        # Actualizar barra de estado
        disk_count = len(StorageAnalyzer.get_disk_usage())
        self.ui.statusbar.showMessage(f"Dashboard activo - {disk_count} discos detectados", 0)
    
    def mostrar_analizador(self):
        """Mostrar el analizador de carpetas"""
        self.ui.labelTitle.setText("📊 Analizador de Carpetas")
        self.clear_content_area()
        
        # Añadir el widget del analizador
        self.ui.scrollAreaWidgetContents.layout().addWidget(self.folder_analyzer_widget)
        self.folder_analyzer_widget.show()
        
        self.ui.statusbar.showMessage("Analizador de carpetas activo", 0)
    
    def mostrar_organizador(self):
        """Mostrar el organizador de archivos"""
        self.ui.labelTitle.setText("📁 Organizador de Archivos")
        self.clear_content_area()
        
        # Crear contenido temporal
        organizer_label = QLabel("🚧 Organizador en desarrollo...\n\nPróximamente podrás:\n• Organizar archivos por tipo\n• Crear categorías personalizadas\n• Mover archivos automáticamente")
        organizer_label.setAlignment(Qt.AlignCenter)
        organizer_label.setStyleSheet("""
            color: #7f8c8d; 
            font-size: 16px; 
            padding: 50px;
            background-color: #ecf0f1;
            border-radius: 10px;
            margin: 20px;
        """)
        
        self.ui.scrollAreaWidgetContents.layout().addWidget(organizer_label)
        self.ui.statusbar.showMessage("Organizador de archivos (en desarrollo)", 0)
    
    def mostrar_etiquetas(self):
        """Mostrar el gestor de etiquetas"""
        self.ui.labelTitle.setText("🏷️ Gestor de Etiquetas")
        self.clear_content_area()
        
        # Crear contenido temporal
        tags_label = QLabel("🚧 Gestor de etiquetas en desarrollo...\n\nPróximamente podrás:\n• Crear etiquetas personalizadas\n• Asignar etiquetas a archivos\n• Buscar por etiquetas\n• Filtrar contenido")
        tags_label.setAlignment(Qt.AlignCenter)
        tags_label.setStyleSheet("""
            color: #7f8c8d; 
            font-size: 16px; 
            padding: 50px;
            background-color: #ecf0f1;
            border-radius: 10px;
            margin: 20px;
        """)
        
        self.ui.scrollAreaWidgetContents.layout().addWidget(tags_label)
        self.ui.statusbar.showMessage("Gestor de etiquetas (en desarrollo)", 0)
    
    def mostrar_limpieza(self):
        """Mostrar herramientas de limpieza"""
        self.ui.labelTitle.setText("🧹 Herramientas de Limpieza")
        self.clear_content_area()
        
        # Crear contenido temporal
        cleanup_label = QLabel("🚧 Herramientas de limpieza en desarrollo...\n\nPróximamente podrás:\n• Encontrar archivos duplicados\n• Limpiar archivos temporales\n• Detectar archivos grandes\n• Liberar espacio automáticamente")
        cleanup_label.setAlignment(Qt.AlignCenter)
        cleanup_label.setStyleSheet("""
            color: #7f8c8d; 
            font-size: 16px; 
            padding: 50px;
            background-color: #ecf0f1;
            border-radius: 10px;
            margin: 20px;
        """)
        
        self.ui.scrollAreaWidgetContents.layout().addWidget(cleanup_label)
        self.ui.statusbar.showMessage("Herramientas de limpieza (en desarrollo)", 0)
    
    def mostrar_configuracion(self):
        """Mostrar configuración de la aplicación"""
        self.ui.labelTitle.setText("⚙️ Configuración")
        self.clear_content_area()
        
        # Crear widget de configuración
        config_widget = QWidget()
        config_layout = QVBoxLayout(config_widget)
        
        # Lista de configuraciones
        config_list = QListWidget()
        config_list.setStyleSheet("""
            QListWidget {
                background-color: #ffffff;
                border: 2px solid #ecf0f1;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #ecf0f1;
            }
            QListWidget::item:hover {
                background-color: #f8f9fa;
            }
            QListWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
        """)
        
        # Añadir opciones de configuración
        config_options = [
            "🎨 Tema de la aplicación (Claro/Oscuro)",
            "📁 Carpetas de monitoreo automático",
            "⏰ Intervalo de actualización (30s)",
            "📊 Tipo de gráficas predeterminadas",
            "🔔 Notificaciones de espacio bajo",
            "💾 Límite de espacio en disco (advertencia)",
            "🗂️ Categorías de archivos personalizadas",
            "🚀 Iniciar con Windows",
            "📈 Mostrar estadísticas detalladas",
            "🔄 Actualización automática de datos"
        ]
        
        for option in config_options:
            config_list.addItem(option)
        
        config_layout.addWidget(config_list)
        
        # Información adicional
        info_label = QLabel("💡 Selecciona una opción para configurarla")
        info_label.setStyleSheet("color: #7f8c8d; font-style: italic; padding: 10px;")
        config_layout.addWidget(info_label)
        
        self.ui.scrollAreaWidgetContents.layout().addWidget(config_widget)
        self.ui.statusbar.showMessage("Configuración de la aplicación", 0)
    
    def mostrar_acerca_de(self):
        """Mostrar información sobre la aplicación"""
        QMessageBox.about(self, "Acerca de Stroge", 
                         """
                         <h2>🗂️ Stroge v1.0</h2>
                         <p><b>Administrador de Almacenamiento Inteligente</b></p>
                         
                         <p>Stroge te ayuda a administrar y organizar el almacenamiento 
                         de tu computadora de manera eficiente.</p>
                         
                         <h3>Características:</h3>
                         <ul>
                         <li>📊 Visualización del uso de discos</li>
                         <li>📁 Análisis de carpetas</li>
                         <li>🏷️ Sistema de etiquetas</li>
                         <li>🧹 Herramientas de limpieza</li>
                         <li>📈 Estadísticas detalladas</li>
                         </ul>
                         
                         <p><b>Desarrollado con:</b> Python + PySide6 + Matplotlib</p>
                         <p><b>Usuario:</b> grivy</p>
                         """)
    
    def abrir_carpeta(self):
        """Abrir diálogo para seleccionar carpeta"""
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta para analizar")
        if folder:
            self.ui.statusbar.showMessage(f"Analizando carpeta: {folder}", 2000)
            # Aquí puedes añadir la lógica para analizar la carpeta seleccionada
    
    def actualizar_datos(self):
        """Actualizar todos los datos de la aplicación"""
        if hasattr(self, 'storage_widget') and self.storage_widget.isVisible():
            self.storage_widget.update_storage_info()
        self.ui.statusbar.showMessage("Datos actualizados", 2000)
    
    def auto_refresh(self):
        """Actualización automática periódica"""
        if hasattr(self, 'storage_widget') and self.storage_widget.isVisible():
            self.storage_widget.update_storage_info()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Configurar estilo de la aplicación
    app.setStyle('Fusion')
    
    # Aplicar estilo global
    app.setStyleSheet("""
        QMainWindow {
            background-color: #f5f5f5;
        }
        QWidget {
            font-family: 'Segoe UI', Arial, sans-serif;
        }
    """)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())