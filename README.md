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
```


## Usage
To execute the script, simply run:

```bash
python ethusdt_data_comparison.py
```
The script will download the 1-minute OHLCV data for the ETH/USDT trading pair, save it in different file formats, and then compare the time taken and file size for each format. It will print a comparison table and display a bar chart to visualize the comparison.

## Results
Sample results:
CSV: Time = 0.76 seconds, Size = 9.17 MB
Parquet: Time = 0.16 seconds, Size = 4.61 MB
JSON: Time = 1.51 seconds, Size = 17.32 MB
HDF5: Time = 1.74 seconds, Size = 3.64 MB
Feather: Time = 0.42 seconds, Size = 4.24 MB

Based on these results, it is recommended to choose either Parquet or Feather file formats for deep learning tasks, as they offer efficient storage and fast read/write operations. Feather format, in particular, provides faster read and write times while maintaining relatively small file sizes.

## License
This project is licensed under the MIT License.
