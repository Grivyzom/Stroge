# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QFrame#leftPanel {\n"
"    background-color: #2c3e50;\n"
"    border-right: 3px solid #34495e;\n"
"}\n"
"\n"
"QFrame#rightPanel {\n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 12px;\n"
"    margin: 5px;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #21618c;\n"
"}\n"
"\n"
"QPushButton#btnHome {\n"
"    background-color: #27ae60;\n"
"}\n"
"\n"
"QPushButton#btnHome:hover {\n"
"    background-color: #229954;\n"
"}\n"
"\n"
"QPushButton#btnSettings {\n"
"    background-color: #e74c3c;\n"
"}\n"
"\n"
"QPushButton#btnSettings:hover {\n"
"    background-color: #c0392b;\n"
"}\n"
"\n"
"QLabel#labelTitle {\n"
"    font-size: 24px;\n"
""
                        "    font-weight: bold;\n"
"    color: #2c3e50;\n"
"    padding: 15px;\n"
"    border-bottom: 2px solid #ecf0f1;\n"
"}\n"
"\n"
"QWidget#contentArea {\n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"}")
        self.actionNuevo_Analisis = QAction(MainWindow)
        self.actionNuevo_Analisis.setObjectName(u"actionNuevo_Analisis")
        self.actionAbrir_Carpeta = QAction(MainWindow)
        self.actionAbrir_Carpeta.setObjectName(u"actionAbrir_Carpeta")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionActualizar = QAction(MainWindow)
        self.actionActualizar.setObjectName(u"actionActualizar")
        self.actionVista_Compacta = QAction(MainWindow)
        self.actionVista_Compacta.setObjectName(u"actionVista_Compacta")
        self.actionVista_Compacta.setCheckable(True)
        self.actionVista_Detallada = QAction(MainWindow)
        self.actionVista_Detallada.setObjectName(u"actionVista_Detallada")
        self.actionVista_Detallada.setCheckable(True)
        self.actionVista_Detallada.setChecked(True)
        self.actionLimpiar_Cache = QAction(MainWindow)
        self.actionLimpiar_Cache.setObjectName(u"actionLimpiar_Cache")
        self.actionBuscar_Duplicados = QAction(MainWindow)
        self.actionBuscar_Duplicados.setObjectName(u"actionBuscar_Duplicados")
        self.actionPreferencias = QAction(MainWindow)
        self.actionPreferencias.setObjectName(u"actionPreferencias")
        self.actionGuia_Usuario = QAction(MainWindow)
        self.actionGuia_Usuario.setObjectName(u"actionGuia_Usuario")
        self.actionAcerca_de = QAction(MainWindow)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QFrame(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setMaximumSize(QSize(250, 16777215))
        self.leftPanel.setFrameShape(QFrame.StyledPanel)
        self.leftPanel.setFrameShadow(QFrame.Raised)
        self.leftLayout = QVBoxLayout(self.leftPanel)
        self.leftLayout.setSpacing(10)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(15, 20, 15, 20)
        self.labelLogo = QLabel(self.leftPanel)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setAlignment(Qt.AlignCenter)

        self.leftLayout.addWidget(self.labelLogo)

        self.line = QFrame(self.leftPanel)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: #ffffff;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.leftLayout.addWidget(self.line)

        self.btnHome = QPushButton(self.leftPanel)
        self.btnHome.setObjectName(u"btnHome")

        self.leftLayout.addWidget(self.btnHome)

        self.btnAnalyzer = QPushButton(self.leftPanel)
        self.btnAnalyzer.setObjectName(u"btnAnalyzer")

        self.leftLayout.addWidget(self.btnAnalyzer)

        self.btnOrganizer = QPushButton(self.leftPanel)
        self.btnOrganizer.setObjectName(u"btnOrganizer")

        self.leftLayout.addWidget(self.btnOrganizer)

        self.btnTags = QPushButton(self.leftPanel)
        self.btnTags.setObjectName(u"btnTags")

        self.leftLayout.addWidget(self.btnTags)

        self.btnCleanup = QPushButton(self.leftPanel)
        self.btnCleanup.setObjectName(u"btnCleanup")

        self.leftLayout.addWidget(self.btnCleanup)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftLayout.addItem(self.verticalSpacer)

        self.btnSettings = QPushButton(self.leftPanel)
        self.btnSettings.setObjectName(u"btnSettings")

        self.leftLayout.addWidget(self.btnSettings)

        self.btnAbout = QPushButton(self.leftPanel)
        self.btnAbout.setObjectName(u"btnAbout")

        self.leftLayout.addWidget(self.btnAbout)


        self.mainLayout.addWidget(self.leftPanel)

        self.rightPanel = QFrame(self.centralwidget)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setFrameShape(QFrame.StyledPanel)
        self.rightPanel.setFrameShadow(QFrame.Raised)
        self.rightLayout = QVBoxLayout(self.rightPanel)
        self.rightLayout.setSpacing(0)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.rightPanel)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.rightLayout.addWidget(self.labelTitle)

        self.contentArea = QWidget(self.rightPanel)
        self.contentArea.setObjectName(u"contentArea")
        self.contentArea.setStyleSheet(u"QWidget#contentArea {\n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"    margin: 5px;\n"
"}")
        self.contentLayout = QVBoxLayout(self.contentArea)
        self.contentLayout.setSpacing(10)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(15, 15, 15, 15)
        self.scrollArea = QScrollArea(self.contentArea)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #ecf0f1;\n"
"    width: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #bdc3c7;\n"
"    border-radius: 6px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #95a5a6;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 917, 69))
        self.scrollContentLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollContentLayout.setSpacing(10)
        self.scrollContentLayout.setObjectName(u"scrollContentLayout")
        self.scrollContentLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.contentLayout.addWidget(self.scrollArea)


        self.rightLayout.addWidget(self.contentArea)


        self.mainLayout.addWidget(self.rightPanel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 33))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"    background-color: #34495e;\n"
"    color: white;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #2c3e50;\n"
"    border-radius: 3px;\n"
"}")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        self.menuHerramientas = QMenu(self.menubar)
        self.menuHerramientas.setObjectName(u"menuHerramientas")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"QStatusBar {\n"
"    background-color: #ecf0f1;\n"
"    border-top: 1px solid #bdc3c7;\n"
"    color: #2c3e50;\n"
"}")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionNuevo_Analisis)
        self.menuArchivo.addAction(self.actionAbrir_Carpeta)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuVer.addAction(self.actionActualizar)
        self.menuVer.addSeparator()
        self.menuVer.addAction(self.actionVista_Compacta)
        self.menuVer.addAction(self.actionVista_Detallada)
        self.menuHerramientas.addAction(self.actionLimpiar_Cache)
        self.menuHerramientas.addAction(self.actionBuscar_Duplicados)
        self.menuHerramientas.addSeparator()
        self.menuHerramientas.addAction(self.actionPreferencias)
        self.menuAyuda.addAction(self.actionGuia_Usuario)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Stroge - Administrador de Almacenamiento", None))
        self.actionNuevo_Analisis.setText(QCoreApplication.translate("MainWindow", u"Nuevo An\u00e1lisis", None))
#if QT_CONFIG(shortcut)
        self.actionNuevo_Analisis.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir_Carpeta.setText(QCoreApplication.translate("MainWindow", u"Abrir Carpeta", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir_Carpeta.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionActualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
#if QT_CONFIG(shortcut)
        self.actionActualizar.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionVista_Compacta.setText(QCoreApplication.translate("MainWindow", u"Vista Compacta", None))
        self.actionVista_Detallada.setText(QCoreApplication.translate("MainWindow", u"Vista Detallada", None))
        self.actionLimpiar_Cache.setText(QCoreApplication.translate("MainWindow", u"Limpiar Cache", None))
        self.actionBuscar_Duplicados.setText(QCoreApplication.translate("MainWindow", u"Buscar Duplicados", None))
        self.actionPreferencias.setText(QCoreApplication.translate("MainWindow", u"Preferencias", None))
#if QT_CONFIG(shortcut)
        self.actionPreferencias.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuia_Usuario.setText(QCoreApplication.translate("MainWindow", u"Gu\u00eda de Usuario", None))
#if QT_CONFIG(shortcut)
        self.actionGuia_Usuario.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionAcerca_de.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.labelLogo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">\ud83d\udcbe STROGE</span></p></body></html>", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"\ud83c\udfe0 Dashboard", None))
        self.btnAnalyzer.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcca Analizador", None))
        self.btnOrganizer.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcc1 Organizador", None))
        self.btnTags.setText(QCoreApplication.translate("MainWindow", u"\ud83c\udff7\ufe0f Etiquetas", None))
        self.btnCleanup.setText(QCoreApplication.translate("MainWindow", u"\ud83e\uddf9 Limpieza", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f Configuraci\u00f3n", None))
        self.btnAbout.setText(QCoreApplication.translate("MainWindow", u"\u2139\ufe0f Acerca de", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcca Dashboard de Almacenamiento", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuHerramientas.setTitle(QCoreApplication.translate("MainWindow", u"Herramientas", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

