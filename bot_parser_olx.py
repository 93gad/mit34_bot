from bs4 import BeautifulSoup
import requests
import time
import logging
from aiogram import Bot, Dispatcher, executor, types

def all_page_link():
    url = 'https://www.olx.kz/d/semey/q-айфон/?search%5Border%5D=created_at:desc'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    all_link = soup.find_all('a', class_='css-rc5s2u')
    for item in all_link:
        item_href = item.get('href')
        yield item_href



def parser():
    for i in list(all_page_link()):
        url = 'https://www.olx.kz' + i
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        time_public = soup.find('div', class_='css-sg1fy9').text
        try:
            title = soup.find('h1', class_='css-1soizd2 er34gjf0').text
        except:
            title = None
        try:
            price = soup.find('h3', class_='css-ddweki er34gjf0').text
        except:
            price = None
        try:
            description = soup.find('div', class_='css-bgzo2k er34gjf0').text
        except:
            description = None
        try:
            id_ = soup.find('span', class_='css-12hdxwj er34gjf0').text
        except:
            id_ = None
        time.sleep(5)
        all_text = str(title) + '\n' + str(price) + '\n' + str(description) + '\n' + str(id_) + '\n' + str(time_public) + '\n' + str(url)
        # print(title,price,description,id_,time_public)
        yield all_text
        print(all_text)

# for i in list(parser()):
#     print(i)
API_TOKEN = '6025497207:AAHGdB2jeR0YMpowKuiarAvSHpHYuz3sYbA'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    for i in parser():
        await message.reply(i)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)