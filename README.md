# Cripto CLI Tool

A lightweight, asynchronous command-line tool designed to fetch real-time cryptocurrency prices from the official **Bybit V5 API**.

## Features
* **Asynchronous Requests:** Powered by `asyncio` and `aiohttp` for fast, non-blocking data fetching.
* **Rate-Limit Protection:** Utilizes an `asyncio.Semaphore` capped at 2 concurrent requests to prevent IP bans or API rate-limiting.
* **Supported Tickers:** Tracks major spot pairs including BTC, ETH, SOL, USDC, XRP, ADA, DOGE, AVAX, and DOT against USDT.

## Requirements
* **Python 3.7+**
* `aiohttp` library

## Installation & Setup

1. Clone this repository or download the script files.
2. Install the required dependency:
   ```bash
   pip install aiohttp
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Sample Console Output
```text
1. BTCUSDT = 96420.50 usdt
2. ETHUSDT = 2710.15 usdt
3. SOLUSDT = 185.30 usdt
...
