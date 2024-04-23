import requests
import aiohttp


api_url = 'http://ip-api.com/json/'


async def get_whois(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                api_url + url
        ) as response:
            response_json = await response.json()
    return response_json
