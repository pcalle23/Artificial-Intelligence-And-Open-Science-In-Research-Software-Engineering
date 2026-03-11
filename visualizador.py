import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud


with open("datos_extraidos.json", "r", encoding="utf-8") as f: #cargar JSON de analizador
    datos = json.load(f)

abstracts_completos = ""
nombres_articulos = []
numero_figuras = []
lista_enlaces = []

for pdf, info in datos.items():
    abstracts_completos += info["abstract"] + " "
    nombres_articulos.append(pdf.replace(".pdf", ""))
    numero_figuras.append(info["numero_figuras"])
    
    if info["enlaces"]:#Preparar enlaces
        lista_enlaces.append(f" -> {pdf}\n")
        for enlace in info["enlaces"]:
            lista_enlaces.append(f"- {enlace}\n")
        lista_enlaces.append("\n")

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(abstracts_completos) #nube plabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("NubeDePalabras.png")
plt.close()

plt.figure(figsize=(10, 6)) #Graficas
plt.bar(nombres_articulos, numero_figuras, color='blue')
plt.xlabel('Articulos')
plt.ylabel('Numero de Figuras')
plt.title('Figuras por Artículo')
plt.xticks(rotation=45, ha='right') #inclinar nombres porue no se leen sino
plt.tight_layout()
plt.savefig("figuras_por_articulo.png")
plt.close()

#Lista enlaces
with open("lista_enlaces.md", "w", encoding="utf-8") as f:
    f.write("#Enlaces encontrados en los papers\n\n")
    f.writelines(lista_enlaces)

print("\n=======================\nVisualizacion de PDFs completada\n=======================")