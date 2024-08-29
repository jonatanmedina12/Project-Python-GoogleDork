import hashlib
import os

import requests


class FileDownloader:
    def __init__(self, directorio_destino):
        self.directorio_destino = directorio_destino
        self.crear_directorio()

    def crear_directorio(self):
        if not os.path.exists(self.directorio_destino):
            os.mkdir(self.directorio_destino)

    def descargar_archivo(self, url):
        try:
            respuesta = requests.get(url)
            nombre_archivo = url.split("/")[-1]
            ruta_completa = os.path.join(self.directorio_destino, nombre_archivo)
            with open(ruta_completa, 'wb') as a:
                a.write(respuesta.content)
            print(f"Archivo {nombre_archivo} descargado en {ruta_completa}")
            return ruta_completa
        except Exception as e:
            print(f"Error al descargar {url}: {e}")
            return None

    def filtrar_descargar_archivos(self, urls, tipo_archivos="all"):
        archivos_descargados = []
        if tipo_archivos == "all":
            for url in urls:
                archivo = self.descargar_archivo(url)
                if archivo:
                    archivos_descargados.append(archivo)
        else:
            for url in urls:
                if any(url.endswith(f".{tipo}") for tipo in tipo_archivos):
                    archivo = self.descargar_archivo(url)
                    if archivo:
                        archivos_descargados.append(archivo)
        return archivos_descargados


def check_virus(file_path):
    # Esta es una implementación básica. En un escenario real, 
    # deberías usar una API de antivirus o una biblioteca más robusta.
    try:
        with open(file_path, "rb") as file:
            content = file.read()
            file_hash = hashlib.md5(content).hexdigest()

        # Aquí podrías comparar el hash con una base de datos de hashes de virus conocidos
        # Por ahora, solo simulamos una verificación
        virus_hashes = ["a" * 32, "b" * 32]  # Ejemplo de hashes de virus
        if file_hash in virus_hashes:
            print(f"¡Alerta! Posible virus detectado en {file_path}")
            return False
        else:
            print(f"Archivo {file_path} parece seguro")
            return True
    except Exception as e:
        print(f"Error al verificar el archivo {file_path}: {e}")
        return False
