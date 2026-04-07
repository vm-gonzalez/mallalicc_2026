import json
import time
import requests
from bs4 import BeautifulSoup

# Importamos todo desde la app
from app import malla_data, lista_optativos, lista_ciencias

def obtener_prerrequisitos_online(sigla):
    # Usamos la URL del catálogo de cursos donde están alojados los requisitos
    url = f"https://catalogo.uc.cl/index.php?tmpl=component&view=requisitos&sigla={sigla}"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for td in soup.find_all('td'):
            if "Prerrequisitos" in td.text:
                span_regla = td.find_next_sibling('td').find('span')
                if span_regla:
                    return span_regla.text.strip()
    except Exception as e:
        print(f"Error obteniendo {sigla}: {e}")
    return ""

def generar_diccionario():
    mapa_prerrequisitos = {}
    print("Iniciando extracción de prerrequisitos...")
    
    # 1. Procesar cursos fijos de la malla
    print("\n--- Procesando Malla Base ---")
    for semestre, cursos in malla_data.items():
        for curso in cursos:
            partes = curso["nombre"].split(" - ")
            if len(partes) > 1:
                sigla = partes[0].strip()
                if sigla not in mapa_prerrequisitos:
                    print(f"Consultando: {sigla}...")
                    reqs = obtener_prerrequisitos_online(sigla)
                    if reqs and reqs != "No tiene":
                        mapa_prerrequisitos[sigla] = reqs
                    time.sleep(0.5)

    # 2. Procesar los cursos optativos y minor
    print("\n--- Procesando Optativos/Minor ---")
    for opt in lista_optativos:
        sigla = opt["sigla"]
        if sigla not in mapa_prerrequisitos:
            print(f"Consultando: {sigla}...")
            reqs = obtener_prerrequisitos_online(sigla)
            if reqs and reqs != "No tiene":
                mapa_prerrequisitos[sigla] = reqs
            time.sleep(0.5)

    # 3. Procesar los cursos de ciencias
    print("\n--- Procesando Optativos de Ciencias ---")
    for cien in lista_ciencias:
        sigla = cien["sigla"]
        if sigla not in mapa_prerrequisitos:
            print(f"Consultando: {sigla}...")
            reqs = obtener_prerrequisitos_online(sigla)
            if reqs and reqs != "No tiene":
                mapa_prerrequisitos[sigla] = reqs
            time.sleep(0.5)

    with open('prerrequisitos.json', 'w', encoding='utf-8') as f:
        json.dump(mapa_prerrequisitos, f, indent=4, ensure_ascii=False)
        
    print("\n¡Archivo prerrequisitos.json actualizado con éxito!")

if __name__ == '__main__':
    generar_diccionario()