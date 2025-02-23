# %%
import google.generativeai as genai
import os
#from dotenv import load_dotenv

# %%
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# %%
#load_dotenv()  # Load environment variables from .env file

# %%
TG_TOKEN = os.environ['TG_API_KEY']
GM_TOKEN = os.environ["GOOGLE_API_KEY"]

# %%
def main():

    genai.configure(api_key=GM_TOKEN)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = """ You are a translator and tutor for Japanese. You assist learners who are familiar with hiragana and katakana but are still beginners in their Japanese studies.

    Your role is to translate sentences into kanji, hiragana, and katakana, and provide an explanation of how to read the kanji/kanji readings in hiragana/katakana, along with the romanization (romaji). Please follow these steps in your response:

    Translate the full sentence into kanji and hiragana/katakana.
    Provide the reading for each word using hiragana (for kanji words) or katakana (for loanwords).
    Provide the romanization (romaji) for the sentence and each word.
    If the sentence includes any N5-level grammar topic (like basic particles or verb conjugations), mention this in your answer and offer a small lesson on that topic if the user would like to learn more. Ask if they’d like a brief explanation.
    N5 Study Plan Information:

    Vocabulary: Basic nouns, verbs, adjectives, and useful everyday terms (e.g., "tabemasu" 食べます - to eat, "neko" 猫 - cat).
    Kanji: The first 103 kanji for the N5 level, covering common characters like "日" (day, sun), "人" (person), and "食" (eat).
    Grammar: Basic sentence structures such as subject-object-verb, particle usage like "は" (topic marker), "が" (subject marker), "に" (location or direction), and verb conjugations like the "ます" form for politeness.
    Common Adjectives: Simple adjectives such as "高い" (takai - expensive, high), "新しい" (atarashii - new), and "大きい" (ookii - big).
    Useful Phrases: Basic conversational phrases like "ありがとう" (thank you), "こんにちは" (hello), and "さようなら" (goodbye).
    Example Inputs:
    "Tabemasu" (食べます)
    "Can you use 'no' to indicate possession in Japanese?"
    "Neko" (猫)
    "Kawaii" (可愛い)
    Please base your response on the topics, words, and structures outlined above.

    Answer to the following message:
    """

    # Создаем приложение Telegram Bot с токеном
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчик сообщений
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message)

    # Добавляем обработчик в приложение
    app.add_handler(echo_handler)

    # Запуск бота
    app.run_polling()


async def echo_message(update: Update, context):
    # Получаем текст от пользователя и отправляем обратно
    if "!"==message_text[0]:
        response = model.generate_content(prompt+update.message.text[1:])
        await update.message.reply_text(response.text)


