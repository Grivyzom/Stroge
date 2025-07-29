import os
import psutil
from typing import List, Dict, Tuple
from pathlib import Path

class StorageAnalyzer:
    """Clase para analizar y gestionar información de almacenamiento"""
    
    @staticmethod
    def get_disk_usage() -> List[Dict]:
        """
        Obtiene información de uso de todos los discos disponibles
        Returns: Lista de diccionarios con información de cada disco
        """
        disk_info = []
        partitions = psutil.disk_partitions()
        
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info.append({
                    'device': partition.device,
                    'mountpoint': partition.mountpoint,
                    'fstype': partition.fstype,
                    'total': usage.total,
                    'used': usage.used,
                    'free': usage.free,
                    'percent': (usage.used / usage.total) * 100
                })
            except PermissionError:
                continue
                
        return disk_info
    
    @staticmethod
    def format_bytes(bytes_value: int) -> str:
        """
        Convierte bytes a formato legible (KB, MB, GB, TB)
        """
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.1f} {unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.1f} PB"
    
    @staticmethod
    def get_folder_size(folder_path: str) -> int:
        """
        Calcula el tamaño total de una carpeta
        Args: folder_path - Ruta de la carpeta
        Returns: Tamaño en bytes
        """
        total_size = 0
        try:
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    try:
                        total_size += os.path.getsize(file_path)
                    except (OSError, FileNotFoundError):
                        continue
        except (OSError, FileNotFoundError):
            pass
        return total_size
    
    @staticmethod
    def analyze_folder_contents(folder_path: str) -> Dict:
        """
        Analiza el contenido de una carpeta y agrupa por tipo de archivo
        """
        file_types = {}
        total_files = 0
        total_size = 0
        
        try:
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    try:
                        file_size = os.path.getsize(file_path)
                        file_ext = Path(filename).suffix.lower()
                        
                        if not file_ext:
                            file_ext = 'Sin extensión'
                        
                        if file_ext not in file_types:
                            file_types[file_ext] = {
                                'count': 0,
                                'size': 0,
                                'files': []
                            }
                        
                        file_types[file_ext]['count'] += 1
                        file_types[file_ext]['size'] += file_size
                        file_types[file_ext]['files'].append({
                            'name': filename,
                            'path': file_path,
                            'size': file_size
                        })
                        
                        total_files += 1
                        total_size += file_size
                        
                    except (OSError, FileNotFoundError):
                        continue
        except (OSError, FileNotFoundError):
            pass
        
        return {
            'total_files': total_files,
            'total_size': total_size,
            'file_types': file_types
        }
    
    @staticmethod
    def get_largest_files(folder_path: str, limit: int = 10) -> List[Dict]:
        """
        Obtiene los archivos más grandes de una carpeta
        """
        files_info = []
        
        try:
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    try:
                        file_size = os.path.getsize(file_path)
                        files_info.append({
                            'name': filename,
                            'path': file_path,
                            'size': file_size,
                            'formatted_size': StorageAnalyzer.format_bytes(file_size)
                        })
                    except (OSError, FileNotFoundError):
                        continue
        except (OSError, FileNotFoundError):
            pass
        
        # Ordenar por tamaño (mayor a menor) y limitar resultados
        files_info.sort(key=lambda x: x['size'], reverse=True)
        return files_info[:limit]
    
    @staticmethod
    def get_system_info() -> Dict:
        """
        Obtiene información general del sistema
        """
        return {
            'cpu_count': psutil.cpu_count(),
            'memory_total': psutil.virtual_memory().total,
            'memory_available': psutil.virtual_memory().available,
            'memory_percent': psutil.virtual_memory().percent,
            'disk_count': len(psutil.disk_partitions()),
            'boot_time': psutil.boot_time()
        }

# Funciones auxiliares para tags y categorización
class FileOrganizer:
    """Clase para organizar archivos por categorías y etiquetas"""
    
    # Diccionario de categorías predefinidas
    CATEGORIES = {
        'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
        'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages'],
        'Hojas de Cálculo': ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
        'Presentaciones': ['.ppt', '.pptx', '.odp', '.key'],
        'Archivos Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Código': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.php', '.sql'],
        'Ejecutables': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.app'],
        'Otros': []  # Para archivos que no coincidan con ninguna categoría
    }
    
    @staticmethod
    def categorize_file(file_path: str) -> str:
        """
        Determina la categoría de un archivo basándose en su extensión
        """
        file_ext = Path(file_path).suffix.lower()
        
        for category, extensions in FileOrganizer.CATEGORIES.items():
            if file_ext in extensions:
                return category
        
        return 'Otros'
    
    @staticmethod
    def categorize_folder(folder_path: str) -> Dict[str, List]:
        """
        Categoriza todos los archivos de una carpeta
        """
        categorized_files = {category: [] for category in FileOrganizer.CATEGORIES.keys()}
        
        try:
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    category = FileOrganizer.categorize_file(file_path)
                    categorized_files[category].append({
                        'name': filename,
                        'path': file_path,
                        'size': os.path.getsize(file_path) if os.path.exists(file_path) else 0
                    })
        except (OSError, FileNotFoundError):
            pass
        
        return categorized_files