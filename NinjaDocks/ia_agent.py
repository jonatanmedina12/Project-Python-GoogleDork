from gpt4all import GPT4All

class IAAgent:
    def __init__(self, model="gpt4all-13b-snoozy-q4_0.gguf"):
        self.model = None
        self.initialize_model(model)

    def initialize_model(self, model_name):
        try:
            self.model = GPT4All(model_name)
        except ValueError as e:
            print(f"Error al cargar el modelo {model_name}: {e}")
            self.try_alternative_models()

    def try_alternative_models(self):
        alternative_models = [
            "orca-mini-3b.gguf",
            "gpt4all-falcon-q4_0.gguf",
            "mistral-7b-openorca.Q4_0.gguf"
        ]
        for alt_model in alternative_models:
            try:
                print(f"Intentando cargar modelo alternativo: {alt_model}")
                self.model = GPT4All(alt_model)
                print(f"Modelo {alt_model} cargado exitosamente.")
                return
            except Exception as e:
                print(f"No se pudo cargar {alt_model}: {e}")

        print("No se pudo cargar ningún modelo. Por favor, descargue manualmente un modelo compatible.")

    def generate_dork(self, description):
        if self.model is None:
            return "Error: No se ha cargado ningún modelo. No se puede generar el dork."

        prompt = self._build_prompt(description)
        try:
            output = self.model.generate(prompt)
            return output
        except Exception as e:
            print(f"Error al generar el dork: {e}")
            return "No se pudo generar el dork debido a un error."

    @staticmethod
    def _build_prompt(description):
        return f"""Genera un Google Dork específico basado en la descripción del usuario. Un Google Dork utiliza operadores avanzados en motores de búsqueda para encontrar información específica que es difícil de encontrar mediante una búsqueda normal. Tu tarea es convertir la descripción del usuario en un Google Dork preciso. A continuación, se presentan algunos ejemplos de cómo deberías formular los Google Dorks basándote en diferentes descripciones:

        Descripción: Documentos PDF relacionados con la seguridad informática publicados en el último año.
        Google Dork: filetype:pdf "seguridad informática" after:2023-01-01

        Descripción: Presentaciones de Powerpoint sobre cambio climático disponibles en sitios .edu.
        Google Dork: site:.edu filetype:ppt "cambio climático"

        Descripción: Listas de correos electrónicos en archivos de texto dentro de dominios gubernamentales.
        Google Dork: site:.gov filetype:txt "email" | "correo electrónico"

        Ahora, basado en la siguiente descripción proporcionada por el usuario, genera el Google Dork correspondiente:

        Descripción: {description}."""


if __name__ == "__main__":
    description = "Listado de usuarios y contraseñas en el contenido de ficheros de texto"
    ia = IAAgent()
    prompt=ia._build_prompt(description)

    if ia.model is not None:
        print(ia.generate_dork(prompt))
    else:
        print("No se pudo inicializar el modelo. Por favor, revise los mensajes de error anteriores.")