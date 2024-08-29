import argparse

from NinjaDocks import search_google_data
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Herramienta para realizar búsquedas avanzadas en Google de forma automática.")
    parser.add_argument("-q", "--query", type=str,
                        help="Especifica el dork que deseas buscar. Ejemplo: -q \"filetype:sql 'MySQL dump' (pass|password|passwd|pwd)\"")
    parser.add_argument("-c", "--configure", action="store_true",
                        help="Configura o actualiza el archivo .env. Utiliza esta opción sin otros argumentos para configurar las claves.")
    parser.add_argument("--start-page", type=int, default=1,
                        help="Página de inicio para los resultados de búsqueda. Por defecto es 1.")
    parser.add_argument("--pages", type=int, default=1,
                        help="Número de páginas de resultados a retornar. Por defecto es 1.")
    parser.add_argument("--lang", type=str, default="lang_es",
                        help="Código de idioma para los resultados de búsqueda. Por defecto es 'lang_es' (español).")

    args = parser.parse_args()
    search_google_data()


