import streamlit as st
import folium
from streamlit.components.v1 import components

# 여행지 데이터
locations = [
    {"name": "서울", "lat": 37.5665, "lon": 126.9780, "desc": "역사와 현대가 어우러진 도시, 쇼핑과 맛집의 천국"},
    {"name": "부산", "lat": 35.1796, "lon": 129.0756, "desc": "해운대 해변과 야경이 아름다운 항구 도시"},
    {"name": "제주도", "lat": 33.4996, "lon": 126.5312, "desc": "자연이 살아 숨쉬는 섬, 힐링 여행의 대표주자"},
    {"name": "경주", "lat": 35.8562, "lon": 129.2247, "desc": "천년고도, 신라의 숨결을 느낄 수 있는 역사 도시"},
    {"name": "강릉", "lat": 37.7519, "lon": 128.8761, "desc": "동해안의 푸른 바다와 커피향 가득한 도시"},
    {"name": "속초", "lat": 38.2044, "lon": 128.5911, "desc": "설악산과 속초항이 어우러진 자연 명소"},
    {"name": "인천", "lat": 37.4563, "lon": 126.7052, "desc": "공항과 월미도, 차이나타운 등 매력적인 관광지"},
    {"name": "전주", "lat": 35.8242, "lon": 127.1479, "desc": "한옥마을과 한식의 본고장, 전통문화 체험지"},
    {"name": "여수", "lat": 34.7604, "lon": 127.6622, "desc": "밤바다와 낭만 가득한 남해안 도시"},
    {"name": "춘천", "lat": 37.8813, "lon": 127.7298, "desc": "호반의 도시, 닭갈비와 남이섬으로 유명"}
]

# Streamlit 제목
st.title("🇰🇷 한국인이 사랑하는 TOP 10 여행지")
st.markdown("가장 인기 있는 국내 여행지를 지도와 함께 소개합니다. 원하는 마커를 클릭해보세요!")

# Folium 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7, tiles="CartoDB Positron")

# 마커 추가
for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=f"<b>{loc['name']}</b><br>{loc['desc']}",
        tooltip=loc["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Folium 지도 HTML로 변환
map_html = m._repr_html_()

# 지도 출력
components.html(map_html, height=600, scrolling=False)
