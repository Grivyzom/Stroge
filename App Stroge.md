# 📘 Guía de Comandos - Proyecto PySide6 (usuario: grivy)

Esta guía contiene todos los comandos esenciales para configurar y trabajar con tu aplicación de escritorio hecha con **PySide6 + Qt Designer**.

---

## 1. Crear entorno virtual

bash
mkdir Stroge
cd Stroge
python -m venv venv

# Activar el entorno virtual:
# En Windows:
venv\Scripts\activate



## 4. Ejecutar Qt Designer

`& "C:\Users\grivy\AppData\Roaming\Python\Python313\Scripts\pyside6-designer.exe"`


## 5. Convertir archivo `.ui` a `.py`

`& "C:\Users\grivy\AppData\Roaming\Python\Python313\Scripts\pyside6-uic.exe" interfaz_modernita.ui -o interfaz_modernita.py`


## 6. Ejecutar tu aplicación

Desde PowerShell:

`& C:\Python313\python.exe E:\Informática\Stroge\main.py`