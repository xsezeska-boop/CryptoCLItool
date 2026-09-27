import asyncio
import aiohttp

async def get_price(symbol: str, session, semaphore) -> dict:
    URL = "https://api.bybit.com/v5/market/tickers"
    params = {
        "category": "spot", 
        "symbol": symbol
    }

    async with semaphore:
        try:
            async with session.get(URL, params=params) as response:
                if response.status != 200:
                    raise RuntimeError(
                        f"{symbol}: HTTP status {response.status}"
                    )
                return await response.json()
        except aiohttp.ClientError as error:

            raise RuntimeError(f"{symbol} Request failed")

def catch_price(data: dict) -> str | None:
    try:
        return data['result']['list'][0]['lastPrice']
    except (KeyError, IndexError, TypeError):
        return None


async def main():
    semaphore = asyncio.Semaphore(2)
    SYMBOLS = (
        "BTCUSDT",
        "ETHUSDT",
        "SOLUSDT",
        "USDCUSDT",
        "XRPUSDT",
        "ADAUSDT",
        "DOGEUSDT",
        "AVAXUSDT",
        "DOTUSDT"
    )
    prices = []
    timeout = aiohttp.ClientTimeout(total=5)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [get_price(symbol, session, semaphore) for symbol in SYMBOLS]

        result = await asyncio.gather(*tasks, return_exceptions=True)


    for json in result:
        prices.append(catch_price(json))

    for counter, symbol in enumerate(SYMBOLS, 1):
        print(f"{counter}. {symbol} = {prices[counter - 1]} usdt")

if __name__ == "__main__":
    asyncio.run(main())