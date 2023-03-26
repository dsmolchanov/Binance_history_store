import ccxt
import pandas as pd
import json
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def fetch_ohlcv_data(symbol, timeframe, since, now, limit):
    """
    Fetch OHLCV data for a given symbol and timeframe from the Binance exchange using ccxt.
    """
    exchange = ccxt.binance({
        'rateLimit': 1200,
        'enableRateLimit': True,
    })
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
    return ohlcv_data

def save_to_csv(data, filename):
    """
    Save data as a CSV file.
    """
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("datetime", inplace=True)
    df.to_csv(filename)

def save_to_parquet(data, filename):
    """
    Save data as a Parquet file.
    """
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("datetime", inplace=True)
    df.to_parquet(filename)

def save_to_json(data, filename):
    """
    Save data as a JSON file.
    """
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("datetime", inplace=True)
    df.index = df.index.astype(str)
    with open(filename, 'w') as f:
        json.dump(df.to_dict(orient='index'), f)

def save_to_hdf5(data, filename):
    """
    Save data as an HDF5 file.
    """
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("datetime", inplace=True)
    df.to_hdf(filename, key='data', mode='w')

def save_to_feather(data, filename):
    """
    Save data as a Feather file.
    """
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("datetime", inplace=True)
    df.reset_index(inplace=True)
    df.to_feather(filename)

def measure_time_and_size(save_function, file_extension, data):
    """
    Measure the time taken and file size for saving data in a specific file format.
    """
    filename = f"ethusdt_1m_{file_extension}"
    start_time = time.time()
    save_function(data, filename)
    elapsed_time = time.time() - start_time
    file_size = os.path.getsize(filename)
    return elapsed_time, file_size

def plot_comparison_chart(df_results):
    """
    Generate a bar chart comparing time and file size for different file formats.
    """
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()

    x = np.arange(len(df_results['Format']))
    y1 = df_results['Time (seconds)']
    y2 = df_results['Size (MB)']
    width = 0.4
    rects1 = ax1.bar(x - width / 2, y1, width, color='b', label='Time (seconds)')
    rects2 = ax2.bar(x + width / 2, y2, width, color='g', label='Size (MB)')

    ax1.set_xticks(x)
    ax1.set_xticklabels(df_results['Format'])
    ax1.set_ylabel('Time (seconds)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2.set_ylabel('Size (MB)', color='g')
    ax2.tick_params(axis='y', labelcolor='g')

    def autolabel(rects, ax, color):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{:.2f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom',
                        color=color)

    autolabel(rects1, ax1, 'b')
    autolabel(rects2, ax2, 'g')

    fig.tight_layout()
    plt.title("File Format Comparison - Time and Size")
    plt.show()

symbol = "ETH/USDT"
timeframe = "1m"
now = int(time.time() * 1000)
three_months_ago = now - 3 * 30 * 24 * 60 * 60 * 1000
limit = 1000

data = fetch_ohlcv_data(symbol, timeframe, three_months_ago, now, limit)

file_formats = [
    ('CSV', save_to_csv, 'csv'),
    ('Parquet', save_to_parquet, 'parquet'),
    ('JSON', save_to_json, 'json'),
    ('HDF5', save_to_hdf5, 'h5'),
    ('Feather', save_to_feather, 'feather')
]

results = []

for format_name, save_function, file_extension in file_formats:
    elapsed_time, file_size = measure_time_and_size(save_function, file_extension, data)
    results.append((format_name, elapsed_time, file_size))
    print(f"{format_name}: Time = {elapsed_time:.2f} seconds, Size = {file_size / 1024 / 1024:.2f} MB")

df_results = pd.DataFrame(results, columns=['Format', 'Time (seconds)', 'Size (MB)'])
print("\nComparison Table:")
print(df_results)

plot_comparison_chart(df_results)
