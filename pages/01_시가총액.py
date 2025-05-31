import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("🌍 전 세계 시가총액 Top 10 기업의 3년간 변화")

st.markdown("""
**💡 시가총액이란?**  
시가총액은 기업의 전체 가치를 나타내는 지표로, _주가 × 발행주식 수_로 계산됩니다. 일반적으로 기업의 규모를 판단하는 데 사용됩니다.
""")

companies = {
    "Apple": {"ticker": "AAPL", "desc": "아이폰과 맥북 등 하드웨어 중심의 글로벌 기술 기업"},
    "Microsoft": {"ticker": "MSFT", "desc": "Windows, Office, Azure 등을 제공하는 세계 최대 소프트웨어 기업"},
    "Saudi Aramco": {"ticker": "2222.SR", "desc": "세계 최대의 석유 회사, 사우디아라비아 국영 기업"},
    "Alphabet (Google)": {"ticker": "GOOGL", "desc": "Google, YouTube 등을 소유한 글로벌 인터넷 서비스 기업"},
    "Amazon": {"ticker": "AMZN", "desc": "세계 최대의 전자상거래 및 클라우드 컴퓨팅 기업"},
    "NVIDIA": {"ticker": "NVDA", "desc": "GPU 및 AI 반도체를 설계하는 선도 기술 기업"},
    "Berkshire Hathaway": {"ticker": "BRK-B", "desc": "워런 버핏이 이끄는 미국의 대형 투자 지주회사"},
    "Meta Platforms": {"ticker": "META", "desc": "Facebook, Instagram, WhatsApp 등을 운영하는 소셜 미디어 기업"},
    "Tesla": {"ticker": "TSLA", "desc": "전기차 및 에너지 솔루션을 제공하는 혁신적인 기술 기업"},
    "TSMC": {"ticker": "TSM", "desc": "세계 최대의 반도체 파운드리 기업 (대만)"}
}

start_date = (datetime.today() - timedelta(days=3*365)).strftime('%Y-%m-%d')
end_date = datetime.today().strftime('%Y-%m-%d')

@st.cache_data
def load_data():
    data = {}
    latest_market_caps = {}
    for name, info in companies.items():
        ticker = info["ticker"]
        try:
            ticker_obj = yf.Ticker(ticker)
            df = ticker_obj.history(start=start_date, end=end_date)
            shares = ticker_obj.info['sharesOutstanding']
            df['Market Cap'] = df['Close'] * shares
            df = df[['Market Cap']].rename(columns={'Market Cap': name})
            data[name] = df
            latest_market_caps[name] = df[name].dropna().iloc[-1]
        except Exception as e:
            st.warning(f"{name} 데이터 수집 실
