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

# 기업 정보
companies = {
    "Apple": {
        "ticker": "AAPL",
        "desc": "아이폰과 맥북 등 하드웨어 중심의 글로벌 기술 기업",
        "details": "- 아이폰, 아이패드, 맥북 등 소비자 전자제품을 주력으로 함\n- iOS 운영체제와 자체 칩(M 시리즈)으로 생태계 형성\n- 1976년 스티브 잡스에 의해 창립\n- 2007년 아이폰 출시로 스마트폰 혁신 주도\n- 매년 9월 신제품 공개로 주가에 큰 영향 미침"
    },
    "Microsoft": {
        "ticker": "MSFT",
        "desc": "Windows, Office, Azure 등을 제공하는 세계 최대 소프트웨어 기업",
        "details": "- Windows OS와 MS Office로 오랜 기간 독점적 지위 유지\n- 클라우드 플랫폼 Azure가 큰 성장 주도\n- 1975년 빌 게이츠에 의해 창립\n- 2016년 LinkedIn, 2022년 Activision Blizzard 인수\n- GitHub 인수 및 Copilot 등 AI 분야에도 적극 투자"
    },
    "Saudi Aramco": {
        "ticker": "2222.SR",
        "desc": "세계 최대의 석유 회사, 사우디아라비아 국영 기업",
        "details": "- 석유 생산량, 매장량 모두 세계 최고 수준\n- 사우디아라비아 정부 소유, 2019년 IPO\n- 석유화학 및 정제 사업도 확장\n- 에너지 전환과 ESG 투자 확대 중\n- 수익 대부분을 국가 재정에 기여"
    },
    "Alphabet (Google)": {
        "ticker": "GOOGL",
        "desc": "Google, YouTube 등을 소유한 글로벌 인터넷 서비스 기업",
        "details": "- 검색엔진 Google과 광고 사업이 주 수익원\n- YouTube, Android OS, Google Cloud 등 서비스 다양\n- 1998년 래리 페이지와 세르게이 브린이 창업\n- AI 연구에서 DeepMind 보유\n- 2015년 지주회사 Alphabet으로 재편"
    },
    "Amazon": {
        "ticker": "AMZN",
        "desc": "세계 최대의 전자상거래 및 클라우드 컴퓨팅 기업",
        "details": "- 온라인 쇼핑, 물류 시스템에서 독보적 영향력\n- AWS(클라우드 사업) 수익성 매우 높음\n- 제프 베조스가 1994년 설립\n- 자율 배송, AI, 우주 사업(Blue Origin) 진출\n- 프라임 회원 기반 충성도 높은 사용자 확보"
    },
    "NVIDIA": {
        "ticker": "NVDA",
        "desc": "GPU 및 AI 반도체를 설계하는 선도 기술 기업",
        "details": "- 그래픽카드 분야에서 압도적 시장 점유율\n- AI, 데이터센터용 고성능 칩 H100으로 성장 주도\n- 1993년 젠슨 황 CEO에 의해 창립\n- 게이밍 외에도 자율주행, 의료 등 확장\n- CUDA 플랫폼으로 AI 생태계 영향력 확대"
    },
    "Berkshire Hathaway": {
        "ticker": "BRK-B",
        "desc": "워런 버핏이 이끄는 미국의 대형 투자 지주회사",
        "details": "- 보험, 철도, 에너지, 소비재 등 다양한 산업 보유\n- 애플, 코카콜라 등 장기 보유 가치주 투자\n- 1965년 워런 버핏이 경영권 인수\n- 분기별 주주 서한이 투자자들에게 영향력 큼\n- 보수적 경영으로 안정적 자산 성장 추구"
    },
    "Meta Platforms": {
        "ticker": "META",
        "desc": "Facebook, Instagram, WhatsApp 등을 운영하는 소셜 미디어 기업",
        "details": "- SNS 기반 광고 수익이 핵심 비즈니스 모델\n- 2021년 사명을 Meta로 변경하며 메타버스 투자 선언\n- 리얼리티 랩스 통해 VR/AR 기술 개발\n- Threads, Reels 등 콘텐츠 다양화\n- AI와 사용자 추천 시스템 고도화 중"
    },
    "Tesla": {
        "ticker": "TSLA",
        "desc": "전기차 및 에너지 솔루션을 제공하는 혁신적인 기술 기업",
        "details": "- 전기차 모델 S, 3, X, Y로 시장 선도\n- 에너지 저장장치 및 태양광 패널 등 에너지 사업도 전개\n- 일론 머스크가 CEO로 브랜드 이미지 상징\n- 오토파일럿 등 자율주행 기술 개발\n- 글로벌 공장(Gigafactory) 확대 중"
    },
    "TSMC": {
        "ticker": "TSM",
        "desc": "세계 최대의 반도체 파운드리 기업 (대만)",
        "details": "- 고성능 반도체 위탁 생산 전문 기업\n- 애플, AMD, NVIDIA 등 주요 고객사 보유\n- 1987년 설립, 대만의 전략적 산업\n- 5nm, 3nm 공정 기술 선도\n- 미국, 일본 등에 생산 공장 확장 중"
    }
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

merged_df = pd.concat(data.values(), axis=1)
merged_df.index = pd.to_datetime(merged_df.index)
merged_df = merged_df.fillna(method="ffill")

# 📈 시가총액 추이 그래프
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
rank_fig.update_layout(
    xaxis_title="기업명",
    yaxis_title="시가총액 (USD)",
    coloraxis_showscale=False,
    height=300
)
st.plotly_chart(rank_fig, use_container_width=True)

# 🏢 기업 설명 및 추가 설명 토글
st.markdown("### 🏢 기업 설명 보기")

selected_company = st.selectbox("기업을 선택하세요", ["원하는 기업을 선택하십시오"] + list(companies.keys()))

if selected_company != "원하는 기업을 선택하십시오":
    selected_rank = ranking_df.get("Rank", pd.Series()).get(selected_company)
    rank_label = f"{int(selected_rank)}위" if selected_rank else "순위 정보 없음"
    desc = companies[selected_company]["desc"]
    st.info(f"**{selected_company}** ({rank_label}): {desc}")

    # 토글 상태 저장
    if f"show_details_{selected_company}" not in st.session_state:
        st.session_state[f"show_details_{selected_company}"] = False

    if st.session_state[f"show_details_{selected_company}"]:
        st.markdown(companies[selected_company]['details'])

    toggle_label = "추가설명 줄이기" if st.session_state[f"show_details_{selected_company}"] else "추가설명 더보기"
    if st.button(toggle_label, key=selected_company):
        st.session_state[f"show_details_{selected_company}"] = not st.session_state[f"show_details_{selected_company}"]
