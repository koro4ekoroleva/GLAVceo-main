from flask import Flask, render_template

app = Flask(__name__)
menu = [{"name": "Главная", "url": "/"},
    {"name": "Виды экспертиз", "url": ""},
    {"name": "Помощь", "url": "help"},
    {"name": "Партнёры", "url": "partners"},
    {"name": "Документы", "url": "documents"},
    {"name": "О нас", "url": ""}]



@app.route("/")
def index():
    return render_template('index.html', menu=menu)

@app.route("/help")
def help():
    return render_template('help.html', title="Помощь", menu=menu)

@app.route("/partners")
def partners():
    return render_template('partners.html', title="Партнёры", menu=menu)

@app.route("/documents")
def documents():
    return render_template('documents.html', title="Документы", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)