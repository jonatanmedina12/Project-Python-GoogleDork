from dotenv import  load_dotenv
import  os


from NinjaDocks.file_downloader import FileDownloader, check_virus
from NinjaDocks.search_google import GoogleSearch
from NinjaDocks.smart_search import PasswordAndLanguageSearch
load_dotenv()
API_KEY_GOOGLE=os.getenv("API_KEY_GOOGLE")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
PAGE = 1
LANG ="lang_es"


def search_google_data():
    url_google_api ='https://www.googleapis.com/customsearch/v1?'
    query_name = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
    #query_name ="medina"
    exec_ = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID, url_google_api, query_name, PAGE, LANG)
    results = exec_.save_to_json("search_results.json")

    downloader = FileDownloader("downloads")
    urls = [result['link'] for result in results]
    downloaded_files = downloader.filtrar_descargar_archivos(urls, tipo_archivos=["sql","pdf", "doc", "docx"])

    # Verificar virus
    for file in downloaded_files:
        is_safe = check_virus(file)
        if not is_safe:
            print(f"Eliminando archivo sospechoso: {file}")
            os.remove(file)

    smart_search_ = PasswordAndLanguageSearch(downloaded_files)
    results = smart_search_.search_passwords_and_languages()
    print(results)