import base64
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Header e Página inicial
st.title('DataInvest - Dados de análise financeira')
st.write("""
# Welcome to DataInvest Financial Data Analysis App
This app retrieves financial data using Yahoo Finance.
""")

# Sidebar Inputs
st.sidebar.header('User Input')
ticker = st.sidebar.text_input("Enter a Stock Ticker:", 'AAPL')

# Retrieve Data from Yahoo Finance
data = yf.Ticker(ticker)
ticker_df = data.history(period='1d', start='2010-01-01', end='2022-01-01')

# Main Content
st.header(f'Stock Data for {ticker}')
st.write(ticker_df.tail())

# Line Chart
st.subheader('Closing Price')
fig, ax = plt.subplots(figsize=(10, 6))
ticker_df['Close'].plot(ax=ax)
plt.title(f'Closing Price for {ticker}')
st.pyplot(fig)

# Statistics
st.subheader('Data Statistics')
st.write(ticker_df.describe())

# Histogram
st.subheader('Volume Histogram')
fig2, ax2 = plt.subplots(figsize=(10, 6))
ticker_df['Volume'].hist(ax=ax2)
plt.title(f'Volume Histogram for {ticker}')
st.pyplot(fig2)

# Download Data
csv_downld='<a href="data:file/csv;base64,{}">Download CSV File</a>'
csv_base64 = base64.b64encode(ticker_df.to_csv(index=False).encode()).decode()
st.markdown(csv_downld.format(csv_base64), unsafe_allow_html=True)
