from flask import Flask, request, jsonify, render_template
import threading
from telebot import TeleBot
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
TELEGRAM_TOKEN = "7654476996:AAHF9AzcSWclTnGOavHy-tdqqkrmRf4bihY"
CHAT_ID = '6473127534'
bot = TeleBot(TELEGRAM_TOKEN)

# Инициализация Flask приложения
app = Flask(__name__)

# Меню для сайта
menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Виды экспертиз", "url": "expertise"},
    {"name": "Помощь", "url": "help"},
    {"name": "Партнёры", "url": "partners"},
    {"name": "Документы", "url": "documents"},
    {"name": "О нас", "url": "about"}
]


@app.route('/send-to-telegram', methods=['POST'])
def send_to_telegram():
    try:
        data = request.form
        logger.info(f"Получены данные формы: {data}")

        # Формируем сообщение
        message = (
            "📌 Новая заявка на консультацию:\n\n"
            f"👤 Имя: {data.get('name', 'не указано')}\n"
            f"📞 Телефон: {data.get('phone', 'не указан')}\n"
            f"📝 Комментарий: {data.get('comment', 'нет комментария')}"
        )

        # Отправляем сообщение
        bot.send_message(CHAT_ID, message)
        logger.info(f"Сообщение отправлено в Telegram: {message}")

        return jsonify({"status": "success"})

    except Exception as e:
        logger.error(f"Ошибка при отправке: {str(e)}")
        return jsonify({
            "status": "error",
            "message": "Произошла ошибка при отправке. Пожалуйста, попробуйте позже."
        }), 500


@app.route("/")
def index():
    return render_template('index.html', menu=menu)


@app.route("/expertise")
def expertise():
    return render_template('expertise.html', title="Виды экспертиз", menu=menu)


@app.route("/help")
def help():
    return render_template('help.html', title="Помощь", menu=menu)


@app.route("/partners")
def partners():
    return render_template('partners.html', title="Партнёры", menu=menu)


@app.route("/documents")
def documents():
    return render_template('documents.html', title="Документы", menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title="О нас", menu=menu)

@app.route("/conferences")
def conferences():
    return render_template('conferences.html', title="Конференции", menu=menu)

@app.route("/media")
def media():
    return render_template('media.html', title="СМИ", menu=menu)

@app.route("/resources")
def resources():
    return render_template('resources.html', title="Ресурсы", menu=menu)

@app.route("/networking")
def networking():
    return render_template('networking.html', title="Нетворкинг", menu=menu)

@app.route("/social")
def social():
    return render_template('social.html', title="Социальные сети", menu=menu)

@app.route("/feedback")
def feedback():
    return render_template('feedback.html', title="Обратная связь", menu=menu)

@app.route("/politics")
def politics():
    return render_template('politics.html',
                           title="Политика в отношении обработки персональных данных",
                           menu=menu,
                           site="glav-ceo.ru")

@app.route("/approval")
def approval():
    return render_template('approval.html', title="Политика в отношении обработки персональных данных", menu=menu)


def run_bot():
    logger.info("Бот запущен в отдельном потоке")
    try:
        bot.infinity_polling()
    except Exception as e:
        logger.error(f"Ошибка в работе бота: {e}")


if __name__ == "__main__":
    # Проверяем, что бот работает
    try:
        logger.info(f"Проверяем бота... ID: {bot.get_me().id}")
    except Exception as e:
        logger.error(f"Ошибка доступа к боту: {e}")
        exit(1)

    # Запускаем бота в отдельном потоке
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # Запускаем Flask приложение
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)