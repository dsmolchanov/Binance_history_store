# Binance_history_store
# ETH/USDT OHLCV Data Comparison

This repository contains a Python script that downloads 1-minute OHLCV (Open, High, Low, Close, Volume) data of the ETH/USDT trading pair from Binance for the last 3 months. It then saves the data in different file formats: CSV, Parquet, JSON, HDF5, and Feather, and compares the time taken and file size for each format.

## Requirements

- Python 3.6+
- ccxt
- pandas
- pyarrow (for Parquet format)
- h5py (for HDF5 format)
- matplotlib (for plotting)

To install the required packages, run:

```bash
pip install ccxt pandas pyarrow h5py matplotlib


```bash

### Usage
To execute the script, simply run:

```bash
python ethusdt_data_comparison.py
