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
            st.warning(f"{name} 데이터 수집 실패: {e}")
    return data, latest_market_caps

data, latest_market_caps = load_data()

# 병합
merged_df = pd.concat(data.values(), axis=1)
merged_df.index = pd.to_datetime(merged_df.index)
merged_df = merged_df.fillna(method="ffill")

# 📈 시계열 그래프
fig = px.line(merged_df, x=merged_df.index, y=merged_df.columns,
              labels={'value': '시가총액 (USD)', 'index': '날짜'},
              title="Top 10 기업 시가총액 추이 (최근 3년)")
fig.update_layout(legend_title_text='기업명')
st.plotly_chart(fig, use_container_width=True)

# 📊 현재 시가총액 순위
st.markdown("### 📊 현재 시가총액 순위 (USD 기준)")
ranking_df = pd.DataFrame.from_dict(latest_market_caps, orient='index', columns=['Market Cap'])
ranking_df = ranking_df.sort_values(by='Market Cap', ascending=False)
ranking_df['Rank'] = range(1, len(ranking_df)+1)
ranking_df.index = ranking_df.index.astype(str)

rank_fig = px.bar(ranking_df, x=ranking_df.index, y='Market Cap',
                  color='Market Cap', color_continuous_scale='blues',
                  title="기업별 최신 시가총액 (순위 기준)")
rank_fig.update_layout(xaxis_title="기업명", yaxis_title="시가총액 (USD)", coloraxis_showscale=False)
st.plotly_chart(rank_fig, use_container_width=True)

# 🏢 기업 설명 선택 박스
st.markdown("### 🏢 기업 설명 보기")
selected_company = st.selectbox("기업을 선택하세요", list(companies.keys()))

selected_rank = ranking_df.get("Rank", pd.Series()).get(selected_company)

# 명확한 순위 표현 (예: 1위, 2위 ...)
rank_label = f"{int(selected_rank)}위" if selected_rank else "순위 정보 없음"

desc = companies[selected_company]["desc"]
st.info(f"**{selected_company}** ({rank_label}): {desc}")
