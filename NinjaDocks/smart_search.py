import os
import re
import chardet


class PasswordAndLanguageSearch:
    def __init__(self, file_paths):
        if isinstance(file_paths, str):
            file_paths = [file_paths]
        self.file_paths = file_paths
        self.files = self.__read_files()

    def __read_files(self):
        files = {}
        for file_path in self.file_paths:
            try:
                if os.path.isfile(file_path):
                    content = self.__read_text_file(file_path)
                    files[os.path.basename(file_path)] = content
                    print(f"Archivo leído: {file_path}, Tamaño: {len(content)} caracteres")
                else:
                    print(f"La ruta no es un archivo válido: {file_path}")
            except Exception as e:
                print(f"Error al leer el archivo {file_path}: {e}")
        return files

    def __read_text_file(self, file_path):
        with open(file_path, 'rb') as file:
            raw_data = file.read()
        detected = chardet.detect(raw_data)
        encoding = detected['encoding']

        try:
            return raw_data.decode(encoding)
        except:
            return raw_data.decode('utf-8', errors='ignore')

    def search_passwords_and_languages(self):
        pattern = r"\(\d+,'[^']*','([^']+)','([^']+)','([^']+)',\d+,\d+\)"

        results = {}
        for file, text in self.files.items():
            file_results = []
            matches = re.finditer(pattern, text, re.MULTILINE)
            for match in matches:
                language, key, value = match.groups()
                if 'password' in key.lower() or 'senha' in key.lower() or 'contraseña' in key.lower():
                    file_results.append(f"Idioma: {language}, Clave: {key}, Valor: {value}")
            if file_results:
                results[file] = file_results

        return results



