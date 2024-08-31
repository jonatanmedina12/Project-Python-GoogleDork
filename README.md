# Google Dork Searcher with AI Optimization

Este proyecto permite realizar búsquedas avanzadas en Google utilizando Google Dorks, mejorando la precisión de las consultas mediante una DLL de inteligencia artificial. Utiliza Python para ejecutar las búsquedas y aprovechar las técnicas de optimización de IA.

## Requisitos

- Python 3.8 o superior
- `google-search-results` (Paquete de Python para acceder a resultados de Google Search)
- Biblioteca de IA (como TensorFlow o PyTorch)
- DLL de optimización de IA personalizada (Asegúrate de tener el archivo DLL correspondiente)

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/jonatanmedina12/Python_Search_Google.git
    ```

2. Instala los paquetes de Python requeridos:
    ```bash
    pip install google-search-results
    pip install tensorflow  # o pytorch, dependiendo de tu DLL de IA
    ```

    

## Uso

1. **Definir los Google Dorks:**
   Los Google Dorks son consultas avanzadas que permiten realizar búsquedas más específicas en Google. Ejemplos de Dorks incluyen:

   ```python
   dorks = [
       'inurl:admin login',
       'intitle:index of passwords',
       'site:example.com filetype:pdf'
   ]
