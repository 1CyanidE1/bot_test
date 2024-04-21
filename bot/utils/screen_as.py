import os

import aiohttp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from urllib.parse import urlparse
import asyncio


async def get_name(url: str, user_id: int):
    timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M')
    parsed_url = urlparse(url).netloc.split('.')
    if len(parsed_url) > 2:
        return f'{user_id}_{parsed_url[1]}_{timestamp}.png'
    else:
        return f'{user_id}_{parsed_url[0]}_{timestamp}.png'


async def upload_to_telegraph(image_path):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            'https://telegra.ph/upload',
            data={'file': open(image_path, 'rb')}
        ) as response:
            response_json = await response.json()

    image_url = 'https://telegra.ph' + response_json[0]['src']
    return image_url


async def get_screenshot(url: str, user_id: int) -> tuple:
    chrome_options = Options()
    # Headless mode needs only when you are using OS without GUI
    # It works faster, but screenshots are in the lower quality
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--remote-debugging-pipe')
    chrome_options.add_argument(f"--crash-dumps-dir={os.path.expanduser('~/tmp/Crashpad')}")

    file_name = await get_name(url, user_id)

    loop = asyncio.get_event_loop()
    driver = await loop.run_in_executor(None, webdriver.Chrome, chrome_options)
    await loop.run_in_executor(None, driver.get, url)
    title = driver.title
    await loop.run_in_executor(None, driver.save_screenshot, f'./bot/media/{file_name}')
    driver.quit()

    file_url = await upload_to_telegraph(f'./bot/media/{file_name}')

    return file_url, title, file_name
