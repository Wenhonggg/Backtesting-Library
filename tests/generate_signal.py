import requests
import pandas as pd
from validation_service import Backtester

class SimpleSMAStrategy:
    def should_enter(self, row):
        return row['signal'] == 1

    def should_exit(self, row):
        return row['signal'] == -1

def fetch_data(symbol, interval, start_time, end_time, api_key):
    url = "https://api.datasource.cybotrade.rs/bybit-spot/candle"
    headers = {"X-API-Key": api_key}
    params = {
        "symbol": symbol,
        "interval": interval,
        "start_time": start_time,
        "end_time": end_time,
    }

    response = requests.get(url, headers=headers, params=params)
    print("Status:", response.status_code)
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

    json_data = response.json()
    data = json_data.get("data") or json_data.get("result")
    if not data or not isinstance(data, list):
        raise Exception("Unexpected response format: Expected a list under 'data' or 'result'.")

    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['start_time'], unit='ms')
    df['price'] = df['close'].astype(float)
    return df

def generate_signals(df):
    df['sma_fast'] = df['price'].rolling(window=10).mean()
    df['sma_slow'] = df['price'].rolling(window=20).mean()
    df['prev_sma_fast'] = df['sma_fast'].shift(1)
    df['prev_sma_slow'] = df['sma_slow'].shift(1)

    df['raw_signal'] = 0
    df.loc[(df['sma_fast'] > df['sma_slow']) & (df['prev_sma_fast'] <= df['prev_sma_slow']), 'raw_signal'] = 1
    df.loc[(df['sma_fast'] < df['sma_slow']) & (df['prev_sma_fast'] >= df['prev_sma_slow']), 'raw_signal'] = -1

    # Forward fill the signal to hold position
    df['signal'] = df['raw_signal'].replace(0, pd.NA).ffill().fillna(0).astype(int)
    return df

def save_to_csv(df, filename):
    df[['timestamp', 'price', 'signal']].to_csv(filename, index=False)
    print(f"CSV saved as {filename}")

def run_backtest(df):
    strategy = SimpleSMAStrategy()
    bt = Backtester(strategy, df)
    bt.run()
    print("Backtest Results:", bt.results)

if __name__ == "__main__":
    API_KEY = "DSmnX6j2i4KD9oFfX8gmFyejU5F4s693N1InmpFVVedHOWj5"
    SYMBOL = "BTCUSDT"
    INTERVAL = "1h"
    START_TIME = "1640995200000"
    END_TIME = "1735689600000"  # 2025-01-01T00:00:00Z in ms

    df = fetch_data(SYMBOL, INTERVAL, START_TIME, END_TIME, API_KEY)
    df = generate_signals(df)
    save_to_csv(df, "btc_signal_data.csv")
    run_backtest(df)