from browser.implementations import Browser
from parsers.soups import BeautifulSoupHTMLParser
from parsers.sites import CybersportParser, NoobClubParser
import telegram
import asyncio

bot_token = '5716906743:AAFaps5CeNR69-geOZzC4zQpkzz2yc9jsPI'

chat_id = '1075370059'

bot = telegram.Bot(token=bot_token)

cybersport_url = 'https://www.cybersport.ru/'
noob_club_url = 'https://www.noob-club.ru/'


def get_data():
    cybersport_browser = Browser(url=cybersport_url)
    noob_club_browser = Browser(url=noob_club_url)
    cybersport_soup = BeautifulSoupHTMLParser(browser=cybersport_browser, browser_type='Chrome')
    noob_club_soup = BeautifulSoupHTMLParser(browser=noob_club_browser, browser_type='Chrome')
    parser_cybersport = CybersportParser(parser=cybersport_soup)
    parser_noobclub = NoobClubParser(parser=noob_club_soup)
    data_cybersport = parser_cybersport.parse()
    data_noobclub = parser_noobclub.parse()
    return data_cybersport, data_noobclub


message_cache = {}


async def send_message():
    data_cyberport, data_noob_club = get_data()

    all_data = data_cyberport + data_noob_club

    for n in all_data[::-1]:
        title = n['title']
        if n['title'] not in message_cache:
            message = f"Title: {n['title']}\nLink: {n['link']}"
            await bot.send_message(chat_id=chat_id, text=message)
            message_cache[title] = True


async def main():
    while True:
        await send_message()
        await asyncio.sleep(300)


if __name__ == "__main__":
    asyncio.run(main())
