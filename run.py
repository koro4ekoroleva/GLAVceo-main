from flask import Flask, request, jsonify, render_template
import requests
import threading
from telebot import TeleBot

app = Flask(__name__)

# Конфигурация бота
TELEGRAM_TOKEN = "7654476996:AAHF9AzcSWclTnGOavHy-tdqqkrmRf4bihY"
CHAT_ID = '922226528'
bot = TeleBot(TELEGRAM_TOKEN)

# Меню для сайта
menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Виды экспертиз", "url": ""},
    {"name": "Помощь", "url": "help"},
    {"name": "Партнёры", "url": "partners"},
    {"name": "Документы", "url": "documents"},
    {"name": "О нас", "url": ""}
]


# Обработчик формы
@app.route('/send-to-telegram', methods=['POST'])
def send_to_telegram():
    try:
        data = request.form
        message = f"Новая заявка:\nИмя: {data['name']}\nТелефон: {data['phone']}\nКомментарий: {data['comment']}"

        bot.send_message(CHAT_ID, message)
        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Маршруты сайта
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


def run_bot():
    print("Бот запущен в отдельном потоке\n")
    bot.infinity_polling()


if __name__ == "__main__":
    # Запускаем бота в отдельном потоке
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True  # Поток завершится при завершении основного
    bot_thread.start()

    # Запускаем Flask приложение
    print("Сервер запускается...")
    app.run(debug=True, use_reloader=False)  # Отключаем reloader для корректной работы с потоками