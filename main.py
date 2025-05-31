import streamlit as st
# ✅ 페이지 설정
st.set_page_config(page_title="MBTI 여행 추천기 ✈️", page_icon="🌍", layout="centered")

# 🌟 제목 및 설명
st.title("🧳 MBTI로 알아보는 여행지 추천 ✈️")
st.markdown("당신의 성격에 딱 맞는 여행지를 찾아볼까요? 😊")

# 🧠 MBTI 선택
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요!",
    options=[
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]
)

# 🎯 추천 정보
recommendations = {
    "INTJ": {
        "type": "전략가형 🧠",
        "place": "📚 오슬로, 노르웨이",
        "reason": "혼자만의 시간과 지적인 탐구를 즐기는 INTJ는 북유럽의 차분한 분위기 속에서 역사, 예술, 기술이 조화를 이루는 오슬로에서 깊은 통찰과 평온함을 느낄 수 있어요.",
        "spots": ["📖 노르웨이 국립도서관", "🏛️ 뭉크 미술관", "🌊 오슬로 피오르드"]
    },
    "INFP": {
        "type": "열정적인 중재자 🌷",
        "place": "🍀 아말피 해안, 이탈리아",
        "reason": "감성과 낭만을 사랑하는 INFP는 이탈리아의 동화 같은 바닷가 마을에서 자신만의 이야기를 만들어갈 수 있어요. 그림 같은 풍경과 고요한 감성의 조화!",
        "spots": ["🌅 포지타노 마을", "⛪ 아말피 대성당", "🚤 카프리섬 보트 투어"]
    },
    "ENFP": {
        "type": "재기발랄한 활동가 🎉",
        "place": "🎉 바르셀로나, 스페인",
        "reason": "열정 넘치고 창의적인 ENFP는 활기찬 거리 예술과 축제가 가득한 바르셀로나에서 에너지를 충전해요! 가우디의 작품도 당신의 영혼에 불을 지필지도!",
        "spots": ["🎨 사그라다 파밀리아", "🌳 구엘 공원", "🏖️ 바르셀로네타 해변"]
    },
    "ISFJ": {
        "type": "헌신적인 수호자 💞",
        "place": "🧡 교토, 일본",
        "reason": "차분하고 정서적인 ISFJ는 따뜻한 일본 전통과 정원이 있는 교토에서 편안함과 감동을 받을 수 있어요. 조용히 나를 돌보는 시간이 될 거예요.",
        "spots": ["⛩️ 후시미 이나리 신사", "🍵 기온 거리", "🌸 아라시야마 대나무 숲"]
    },
    "ENTP": {
        "type": "뜨거운 발명가 💡",
        "place": "🎢 오사카, 일본",
        "reason": "새로움과 재미를 사랑하는 ENTP에겐 유쾌하고 창의적인 도시 오사카가 잘 맞아요! 유니버설 스튜디오에서 놀고, 신기한 음식에도 도전해보세요.",
        "spots": ["🎡 유니버설 스튜디오 재팬", "🍜 도톤보리", "🏯 오사카성"]
    },
    "ISTJ": {
        "type": "청렴한 관리자 🏛️",
        "place": "🏰 프라하, 체코",
        "reason": "전통과 질서를 중요시하는 ISTJ는 역사적인 건축물이 잘 보존된 프라하에서 만족감을 느낄 수 있어요. 계획적인 일정에도 완벽하게 어울리는 도시!",
        "spots": ["🏰 프라하성", "🌉 카를교", "🕍 구시가지 광장"]
    },
    "ESFP": {
        "type": "자유로운 연예인 🌴",
        "place": "🌴 하와이, 미국",
        "reason": "즐거움과 사람을 사랑하는 ESFP는 아름다운 자연과 함께하는 하와이에서 행복 지수를 폭발시킬 수 있어요! 서핑, 하이킹, 바비큐까지 다 있어요!",
        "spots": ["🏄 와이키키 비치", "🌋 다이아몬드 헤드", "🌺 하나우마 베이"]
    },
    # 👉 다른 유형도 원하시면 계속 추가해드릴 수 있어요!
}

# ✨ 결과 표시
if mbti:
    data = recommendations.get(mbti)
    if data:
        st.markdown("---")
        st.subheader(f"🎈 {mbti} - {data['type']}")
        st.markdown(f"### 여행 추천지: {data['place']}")
        st.write(data['reason'])

        # 🎯 추천 명소 리스트
        st.markdown("#### ✨ 꼭 가봐야 할 명소:")
        for spot in data["spots"]:
            st.markdown(f"- {spot}")

        # 애니메이션 효과
        if mbti in ["ENFP", "ESFP", "ENTP"]:
            st.balloons()
        elif mbti in ["INFJ", "ISFJ", "INFP"]:
            st.snow()
        else:
            st.success("🎒 멋진 여행이 될 거예요!")

# 🧸 하단
st.markdown("---

