import openai
import requests
import telegram

openai.api_key = "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"
bot = telegram.Bot(token="6084946021:AAFajYA643e2sD0m_U3xZ5t08cfyOEdELZc")

def respond(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Hello, how can I help you today?',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).get("choices")[0].text
    bot.send_message(chat_id=message.chat_id, text=response)

def main():
    last_update_id = bot.get_updates()[-1].update_id
    while True:
        for update in bot.get_updates(offset=last_update_id, timeout=10):
            last_update_id = update.update_id + 1
            if update.message:
                respond(update.message)

if __name__ == "__main__":
    main()
