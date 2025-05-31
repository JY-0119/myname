import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("🌍 전 세계 시가총액 Top 10 기업의 3년간 변화")

# 시가총액 설명
st.markdown("""
**💡 시가총액이란?**  
시가총액은 기업의 전체 가치를 나타내는 지표로, _주가 × 발행주식 수_로 계산됩니다. 일반적으로 기업의 규모를 판단하는 데 사용됩니다.
""")

# 시가총액 상위 10개 기업 및 설명
companies = {
    "Apple": {
        "ticker": "AAPL",
        "desc": "아이폰과 맥북 등 하드웨어 중심의 글로벌 기술 기업"
    },
    "Microsoft": {
        "ticker": "MSFT",
        "desc": "Windows, Office, Azure 등을 제공하는 세계 최대 소프트웨어 기업"
    },
    "Saudi Aramco": {
        "ticker": "2222.SR",
        "desc": "세계 최대의 석유 회사, 사우디아라비아 국영 기업"
    },
    "Alphabet (Google)": {
        "ticker": "GOOGL",
        "desc": "Google, YouTube 등을 소유한 글로벌 인터넷 서비스 기업"
    },
    "Amazon": {
        "ticker": "AMZN",
        "desc": "세계 최대의 전자상거래 및 클라우드 컴퓨팅 기업"
    },
    "NVIDIA": {
        "ticker": "NVDA",
        "desc": "GPU 및 AI 반도체를 설계하는 선도 기술 기업"
    },
    "Berkshire Hathaway": {
        "ticker": "BRK-B",
        "desc": "워런 버핏이 이끄는 미국의 대형 투자 지주회사"
    },
    "Meta Platforms": {
        "ticker": "META",
        "desc": "Facebook, Instagram, WhatsApp 등을 운영하는 소셜 미디어 기업"
    },
    "Tesla": {
        "ticker": "TSLA",
        "desc": "전기차 및 에너지 솔루션을 제공하는 혁신적인 기술 기업"
    },
    "TSMC": {
        "ticker": "TSM",
        "desc": "세계 최대의 반도체 파운드리 기업 (대만)"
    }
}

start_date = (datetime.today() - timedelta(days=3*365)).strftime('%Y-%m-%d')
end_date = datetime.today().strftime('%Y-%m-%d')

@st.cache_data
def load_data():
    data = {}
    for name, info in companies.items():
        ticker = info["ticker"]
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

# 그래프 먼저 출력
fig = px.line(merged_df, x=merged_df.index, y=merged_df.columns,
              labels={'value': '시가총액 (USD)', 'index': '날짜'},
              title="Top 10 기업 시가총액 추이 (최근 3년)")
fig.update_layout(legend_title_text='기업명')

st.plotly_chart(fig, use_container_width=True)

# 기업 선택 시 설명 출력
st.markdown("### 🏢 기업 설명 보기")
selected_company = st.selectbox("기업을 선택하세요", list(companies.keys()))
st.info(f"**{selected_company}**: {companies[selected_company]['desc']}")
