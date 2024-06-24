import subprocess
import sys
import os

#Realiza a instalação dos pacotes
def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "venv/requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

#Inicia a API
def run_flask_app():
    try:
        os.system("python app.py")
    except Exception as e:
        print(f"Error running Flask app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
    run_flask_app()
