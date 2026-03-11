import json
import os

def test_archivos_generados():
    """Comprobar archivos generados correctos."""
    assert os.path.exists("datos_extraidos.json"), "Falta JSON"
    assert os.path.exists("NubeDePalabras.png"), "Falta imagen"
    assert os.path.exists("figuras_por_articulo.png"), "Falta grafica"
    assert os.path.exists("lista_enlaces.md"), "Falta lista enlaces"

def test_estructura_datos():
    """Comprobar estructura de datos correcta"""
    with open("datos_extraidos.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    assert len(datos) > 0, "No se ha procesado ningun articulo." 
    
    for pdf, info in datos.items():
        assert "abstract" in info, f"Falta el abstract en el paper: {pdf}"
        assert type(info["abstract"]) == str, f"El abstract de {pdf} no es texto"
        assert "numero_figuras" in info, f"Falta contar las figuras en el paper: {pdf}"
        assert type(info["numero_figuras"]) == int, f"Las figuras de {pdf} no son un número"
        assert "enlaces" in info, f"Falta la lista de enlaces en el paper: {pdf}"
        assert type(info["enlaces"]) == list, f"Los enlaces de {pdf} no están listados"
        