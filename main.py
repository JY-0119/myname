import streamlit as st
import streamlit as st

# ✅ 페이지 설정 (가장 먼저)
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

# 🎯 MBTI 설명 및 추천지
recommendations = {
    "INTJ": {
        "type": "전략가형 🧠",
        "place": "📚 오슬로, 노르웨이",
        "reason": "혼자만의 시간과 지적인 탐구를 즐기는 INTJ는 북유럽의 차분한 분위기 속에서 역사, 예술, 기술이 조화를 이루는 오슬로에서 깊은 통찰과 평온함을 느낄 수 있어요."
    },
    "INTP": {
        "type": "논리적 사색가 🧩",
        "place": "🔭 도쿄, 일본",
        "reason": "끊임없이 지식을 탐구하는 INTP에게는 과학관, 미술관, 미래 기술이 집약된 도쿄가 제격! 독특한 문화도 이들의 호기심을 자극할 거예요."
    },
    "ENTJ": {
        "type": "대담한 통솔자 🧑‍💼",
        "place": "🌆 뉴욕, 미국",
        "reason": "목표지향적이고 야망 넘치는 ENTJ는 빠르게 변화하는 뉴욕의 도시 에너지와 완벽히 어울려요. 문화, 비즈니스, 리더십 감각까지 모두 충족!"
    },
    "ENTP": {
        "type": "뜨거운 발명가 💡",
        "place": "🎢 오사카, 일본",
        "reason": "새로움과 재미를 사랑하는 ENTP에겐 유쾌하고 창의적인 도시 오사카가 잘 맞아요! 유니버설 스튜디오에서 놀고, 신기한 음식에도 도전해보세요."
    },
    "INFJ": {
        "type": "통찰력 있는 조언자 🌸",
        "place": "🌸 교토, 일본",
        "reason": "조용한 자연, 전통적인 절과 정원에서 INFJ는 내면의 평화를 찾을 수 있어요. 사색과 휴식이 필요한 당신에게 딱 맞는 힐링 여행지!"
    },
    "INFP": {
        "type": "열정적인 중재자 🌷",
        "place": "🍀 아말피 해안, 이탈리아",
        "reason": "감성과 낭만을 사랑하는 INFP는 이탈리아의 동화 같은 바닷가 마을에서 자신만의 이야기를 만들어갈 수 있어요. 그림 같은 풍경과 고요한 감성의 조화!"
    },
    "ENFJ": {
        "type": "정의로운 외교관 🎭",
        "place": "🎭 파리, 프랑스",
        "reason": "사람과의 관계를 소중히 여기는 ENFJ는 예술과 역사, 로맨스가 흐르는 파리에서 진정한 영감을 받을 거예요. 박물관, 카페, 소셜 감성 가득!"
    },
    "ENFP": {
        "type": "재기발랄한 활동가 🎉",
        "place": "🎉 바르셀로나, 스페인",
        "reason": "열정 넘치고 창의적인 ENFP는 활기찬 거리 예술과 축제가 가득한 바르셀로나에서 에너지를 충전해요! 가우디의 작품도 당신의 영혼에 불을 지필지도!"
    },
    "ISTJ": {
        "type": "청렴한 관리자 🏛️",
        "place": "🏰 프라하, 체코",
        "reason": "전통과 질서를 중요시하는 ISTJ는 역사적인 건축물이 잘 보존된 프라하에서 만족감을 느낄 수 있어요. 계획적인 일정에도 완벽하게 어울리는 도시!"
    },
    "ISFJ": {
        "type": "헌신적인 수호자 💞",
        "place": "🧡 교토, 일본",
        "reason": "차분하고 정서적인 ISFJ는 따뜻한 일본 전통과 정원이 있는 교토에서 편안함과 감동을 받을 수 있어요. 조용히 나를 돌보는 시간이 될 거예요."
    },
    "ESTJ": {
        "type": "엄격한 관리자 📋",
        "place": "🏙️ 런던, 영국",
        "reason": "구조적이고 분석적인 ESTJ는 체계적이며 역사 깊은 런던에서 만족할 여행을 즐길 수 있어요. 시간표 짜기 좋아하는 당신에게 딱!"
    },
    "ESFJ": {
        "type": "사교적인 외교관 👗",
        "place": "👗 밀라노, 이탈리아",
        "reason": "사람과 어울리는 걸 즐기고, 감각도 뛰어난 ESFJ에게는 패션과 쇼핑, 음식이 다 있는 밀라노가 최고의 여행지예요!"
    },
    "ISTP": {
        "type": "만능 재주꾼 🛠️",
        "place": "🏔️ 캐나다 로키 산맥",
        "reason": "직접 경험하고 도전하는 걸 좋아하는 ISTP는 자연 속 활동이 많은 로키 산맥에서 진정한 자유와 재미를 느낄 수 있어요!"
    },
    "ISFP": {
        "type": "호기심 많은 예술가 🎨",
        "place": "🎨 피렌체, 이탈리아",
        "reason": "감성적이고 섬세한 ISFP는 예술과 미의 도시 피렌체에서 예술적 영감을 받을 수 있어요. 조용한 골목길, 해질녘의 감성에 딱!"
    },
    "ESTP": {
        "type": "에너지 넘치는 모험가 🌋",
        "place": "🌋 발리, 인도네시아",
        "reason": "활동적이고 사교적인 ESTP에게는 서핑, 스쿠버, 파티가 가득한 발리야말로 최고의 여행지! 액티브한 경험으로 충만해질 거예요."
    },
    "ESFP": {
        "type": "자유로운 영혼의 연예인 🌴",
        "place": "🌴 하와이, 미국",
        "reason": "즐거움과 사람을 사랑하는 ESFP는 아름다운 자연과 함께하는 하와이에서 행복 지수를 폭발시킬 수 있어요! 서핑, 하이킹, 바비큐까지 다 있어요!"
    },
}

# ✨ 결과 표시
if mbti:
    data = recommendations.get(mbti)
    if data:
        st.markdown("---")
        st.subheader(f"🎈 {mbti} - {data['type']}")
        st.markdown(f"### 여행 추천지: {data['place']}")
        st.write(data['reason'])

        # 애니메이션 효과
        if mbti in ["ENFP", "ESFP", "ENTP"]:
            st.balloons()
        elif mbti in ["INFJ", "ISFJ", "INFP"]:
            st.snow()
        else:
            st.success("🎒 멋진 여행이 될 거예요!")

# 🧸 하단
st.markdown("---")
st.markdown("Made with ❤️ by Streamlit")
