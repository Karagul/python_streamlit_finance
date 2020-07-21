import yfinance as yf
import streamlit as st
import datetime
import talib
import ta
import pandas as pd
import requests

yf.pdr_override()

st.write("""
# Technical Analysis Web Application
Shown below are the  **Moving Average Crossovers**, **Bollinger Bands**, **MACD's**, **Commodity Channel Indexes**, and **Relative Strength Indexes** of any stock!
""")

st.sidebar.header('User Input Parameters')

today = datetime.date.today()

def user_input_features():
    ticker = st.sidebar.text_input('Ticker', 'CCL')
    start_date = st.sidebar.text_input('Start Date', '2020-01-01')
    end_date = st.sidebar.text_input('End Date', '2020-07-21')
    return ticker, start_date, end_date

symbol, start, end = user_input_features()

def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    result = requests.get(url).json()
    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']

company_name = get_symbol(symbol.upper())

start = pd.to_datetime(start)
end = ps.to_datetime(end)

data = yf.download(symbol, start, end)