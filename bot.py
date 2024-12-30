import time
import requests
from telegram import Bot
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
BTC_API_URL = os.getenv('BTC_API_URL')
MEMPOOL_API_URL = os.getenv('MEMPOOL_API_URL')

bot = Bot(token=TOKEN)

async def get_btc_price():
    try:
        response = requests.get(BTC_API_URL)
        print(f"Status code (BTC API): {response.status_code}")
        if response.status_code == 200:
            return response.json()['bitcoin']['usd']
        else:
            print(f"Erro ao acessar API do Bitcoin: {response.text}")
            return None
    except Exception as e:
        print(f"Erro na chamada à API do Bitcoin: {str(e)}")
        return None

async def get_mempool_fees():
    try:
        response = requests.get(MEMPOOL_API_URL)
        print(f"Status code (Mempool API): {response.status_code}")
        if response.status_code == 200:
            fees_data = response.json()
            fastest_fee = fees_data.get("fastestFee", "N/A")
            half_hour_fee = fees_data.get("halfHourFee", "N/A")
            hour_fee = fees_data.get("hourFee", "N/A")
            return {
                "fastest": fastest_fee,
                "half_hour": half_hour_fee,
                "hour": hour_fee
            }
        else:
            print(f"Erro ao acessar API da Mempool: {response.text}")
            return None
    except Exception as e:
        print(f"Erro na chamada à API da Mempool: {str(e)}")
        return None

async def send_update():
    while True:
        btc_price = await get_btc_price()  
        mempool_fees = await get_mempool_fees()
        
        if btc_price and mempool_fees:
            message = f"Preço do BTC: ${btc_price}\n"
            message += f"Taxa mais rápida (menos de 10 minutos): {mempool_fees['fastest']} sat/byte\n"
            message += f"Taxa para 30 minutos: {mempool_fees['half_hour']} sat/byte\n"
            message += f"Taxa para 1 hora: {mempool_fees['hour']} sat/byte"
            await bot.send_message(chat_id=CHAT_ID, text=message)
        else:
            await bot.send_message(chat_id=CHAT_ID, text="Erro ao obter dados das APIs.")

        await asyncio.sleep(1800)

if __name__ == "__main__":
    asyncio.run(send_update())
