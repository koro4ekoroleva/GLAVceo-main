from flask import Flask, request, jsonify, render_template
import requests
import telebot

bot = telebot.TeleBot("7654476996:AAHF9AzcSWclTnGOavHy-tdqqkrmRf4bihY", parse_mode=None)

app = Flask(__name__)

TELEGRAM_TOKEN = "7654476996:AAHF9AzcSWclTnGOavHy-tdqqkrmRf4bihY"
TELEGRAM_USERNAME = 'seeLizenka'
CHAT_ID = '922226528'

@app.route('/send-to-telegram', methods=['POST'])
def send_to_telegram():
    try:
        data = request.form
        message = f"Новая заявка:\nИмя: {data['name']}\nТелефон: {data['phone']}\nКомментарий: {data['comment']}"

        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": message}
        )

        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
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
    bot.remove_webhook()
    bot.polling()
    app.run(debug=True)