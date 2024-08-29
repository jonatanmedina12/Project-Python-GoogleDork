import json
import requests

class GoogleSearch:
    def __init__(self, api_key, engine_id, url, query_name, page, lang):
        self.api_key = api_key
        self.engine_id = engine_id
        self.url = url
        self.query_name = query_name
        self.pages = page
        self.lang = lang

    def search(self, start_page=1):
        try:
            result_per_page = 10
            final_results = []

            for page in range(self.pages):
                start_index = (start_page - 1) * result_per_page + 1 + (page * result_per_page)
                url = (
                    f'{self.url}key={self.api_key}&cx={self.engine_id}&q={self.query_name}&start='
                    f'{start_index}&lr={self.lang}')
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    results = data.get("items")
                    custom_result = self.custom_results(results)
                    final_results.extend(custom_result)
                else:
                    print(f"ERROR obtenido al consultar la pagina {page}: HTTP {response.status_code} ")
                    break
            return final_results
        except Exception as e:
            print(e)

    @staticmethod
    def custom_results(results):
        try:
            custom_result = []
            for f in results:
                data_result = {"title": f.get("title"), "description": f.get("snippet"), "link": f.get("link")}
                custom_result.append(data_result)
            return custom_result
        except Exception as e:
            print(e)

    def save_to_json(self, filename):
        results = self.search()
        print(results)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        print(f"Results saved to {filename}")
        return results