import os
import requests 
from bs4 import BeautifulSoup
import json

pdf_folder = "Papers/pdf"
grobid_url = os.environ.get("GROBID_URL", "http://localhost:8070/api/processFulltextDocument")
datos_articulos = {}

#bUSCAR PDFs
lista_pdfs = [archivo for archivo in os.listdir(pdf_folder) if archivo.endswith('.pdf')]
for nombre_pdf in lista_pdfs:#Procesar PDF 1a1
    print(f"Paper: {nombre_pdf}")
    ruta_pdf = os.path.join(pdf_folder, nombre_pdf)
    with open(ruta_pdf, 'rb') as archivo_pdf:
        files = {'input': (nombre_pdf, archivo_pdf, 'application/pdf')}
        respuesta = requests.post(grobid_url, files=files) #Envio a Grobid
    if respuesta.status_code == 200: #todo bien
        sopa = BeautifulSoup(respuesta.text, 'xml')
        etiqueta_abstract = sopa.find('abstract') #Empiezo con abstract
        if etiqueta_abstract:
            texto_abstract = etiqueta_abstract.get_text(separator=' ', strip=True)
        else:
            texto_abstract = ""

        figuras = sopa.find_all('figure') #buscar figuras
        numero_figuras = len(figuras)
        enlaces = [] #Array enlaces
        for etiqueta in sopa.find_all(['ptr', 'ref']):
            enlace = etiqueta.get('target')
            if enlace and enlace.startswith('http'):
                enlaces.append(enlace)
        datos_articulos[nombre_pdf] = {"abstract": texto_abstract,"numero_figuras": numero_figuras,"enlaces": list(set(enlaces))} 
    else:
        print(f"  No se puede procesar: {nombre_pdf}")

with open("datos_extraidos.json", "w", encoding="utf-8") as archivo_json:
    json.dump(datos_articulos, archivo_json, indent=4)

print("\n=======================\nAnalizado Todos los PDFs\n=======================")
