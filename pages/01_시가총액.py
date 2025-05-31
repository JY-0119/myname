import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("🌍 전 세계 시가총액 Top 10 기업의 3년간 변화")

# 시가총액 상위 10개 기업 (2024 기준 예시)
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "NVIDIA": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta Platforms": "META",
    "Tesla": "TSLA",
    "TSMC": "TSM"
}

start_date = (datetime.today() - timedelta(days=3*365)).strftime('%Y-%m-%d')
end_date = datetime.today().strftime('%Y-%m-%d')

@st.cache_data
def load_data():
    data = {}
    for name, ticker in companies.items():
        try:
            df = yf.Ticker(ticker).history(start=start_date, end=end_date)
            df['Market Cap'] = df['Close'] * yf.Ticker(ticker).info['sharesOutstanding']
            df = df[['Market Cap']].rename(columns={'Market Cap': name})
            data[name] = df
        except Exception as e:
            st.warning(f"{name} 데이터 수집 실패: {e}")
    return data

data = load_data()

# 병합
merged_df = pd.concat(data.values(), axis=1)
merged_df.index = pd.to_datetime(merged_df.index)
merged_df = merged_df.fillna(method="ffill")

# 그래프 그리기
fig = px.line(merged_df, x=merged_df.index, y=merged_df.columns,
              labels={'value': '시가총액 (USD)', 'index': '날짜'},
              title="Top 10 기업 시가총액 추이 (최근 3년)")
fig.update_layout(legend_title_text='기업명')

st.plotly_chart(fig, use_container_width=True)
