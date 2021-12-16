######################
# Import libraries
######################

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")
#define the ticker symbol
ticker_symbol="GOOGL"
#get data on this ticker
tickerData=yf.Ticker(ticker_symbol)
#Get the historical prices for this ticker
tickerDF=tickerData.history(period="id",start="2010-12-9",end="2021-12-9")
#Open High Low Close Volume Dividends Stocksplits

st.write("""

## Closing Price

""")
st.line_chart(tickerDF.Close)


st.write("""

## Volume Price

""")
st.line_chart(tickerDF.Volume)
