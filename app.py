from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
HTML_DIR = os.path.join(os.getcwd(), "html_files")

# Nomi dei file HTML che vuoi usare
HTML_FILES = [
    "index.html",
    "attivita.html",
    "area_docenti.html",
    "risultati.html",
    "vita_scolastica.html",
]

@app.route("/")
def home():
    # Controlla quali file esistono nella cartella `html_files`
    available_files = [
        file for file in HTML_FILES if os.path.exists(os.path.join(HTML_DIR, file))
    ]
    return render_template("base.html", html_files=available_files)

@app.route("/view/<path:filename>")
def view_file(filename):
    return send_from_directory(HTML_DIR, filename)

# Crea la cartella per i file HTML se non esiste
if not os.path.exists(HTML_DIR):
    os.makedirs(HTML_DIR)

if __name__ == "__main__":
    app.run(debug=True)
