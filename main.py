import subprocess
import sys

def ejecutar_script(flname):
    print(f"\nEjecutando: {flname}\n===============================")
    resultado = subprocess.run([sys.executable, flname])
    
    if resultado.returncode != 0: #comprobar que no falla
        print(f"error al ejecutar {flname}")
        sys.exit(1)

if __name__ == "__main__":
    ejecutar_script("analizador.py")
    ejecutar_script("visualizador.py")
    print("\nEjecutar tests")
    subprocess.run([sys.executable, "-m", "pytest", "test_valid.py"])
