import streamlit as st

# 🎉 페이지 설정
st.set_page_config(page_title="MBTI 여행 추천기 ✈️", page_icon="🌍", layout="centered")

# 🌟 제목 및 설명
st.title("🧳 MBTI로 알아보는 여행지 추천 ✈️")
st.markdown("당신의 성격에 딱 맞는 여행지를 알려줄게요! 😊")

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

# 여행지 추천 딕셔너리
recommendations = {
    "INTJ": ("📚 오슬로, 노르웨이", "조용하고 지적인 분위기의 북유럽 여행 ✨"),
    "INTP": ("🔭 도쿄, 일본", "호기심을 자극하는 테크 & 과학 박물관 투어 🚀"),
    "ENTJ": ("🌆 뉴욕, 미국", "도전 정신 가득한 대도시의 에너지 💼"),
    "ENTP": ("🎢 오사카, 일본", "아이디어 넘치는 놀이공원과 거리 음식 탐방 😋"),

    "INFJ": ("🌸 교토, 일본", "차분하고 영적인 절과 자연 속 힐링 🧘‍♀️"),
    "INFP": ("🍀 아말피 해안, 이탈리아", "감성을 자극하는 동화 같은 해변 마을 🏖️"),
    "ENFJ": ("🎭 파리, 프랑스", "문화와 예술을 사랑하는 리더의 도시 🎨"),
    "ENFP": ("🎉 바르셀로나, 스페인", "열정 가득한 예술과 축제의 도시 💃"),

    "ISTJ": ("🏰 프라하, 체코", "계획적인 일정에 딱 맞는 유서 깊은 도시 🗺️"),
    "ISFJ": ("🧡 교토, 일본", "전통과 정서가 조화로운 힐링 장소 🍵"),
    "ESTJ": ("🏙️ 런던, 영국", "체계적인 여행과 역사 탐방에 최적 💼"),
    "ESFJ": ("👗 밀라노, 이탈리아", "사교적인 패션 여행 ✨"),

    "ISTP": ("🏔️ 캐나다 로키 산맥", "액티비티 넘치는 모험 여행 ⛷️"),
    "ISFP": ("🎨 피렌체, 이탈리아", "감성을 자극하는 예술 도시 🌅"),
    "ESTP": ("🌋 발리, 인도네시아", "자극과 모험이 가득한 액티브 여행 🏄"),
    "ESFP": ("🌴 하와이, 미국", "파티와 휴식이 조화로운 핫한 여행 🌺"),
}

# ✨ 추천 결과 표시
if mbti:
    place, description = recommendations.get(mbti, ("🌍 지구 어딘가", "세상 어디든 당신의 여행지가 될 수 있어요!"))
    
    st.markdown("---")
    st.subheader(f"🎈 {mbti} 유형에게 추천하는 여행지는...")
    st.markdown(f"### {place}")
    st.markdown(f"_{description}_")

    # Streamlit 애니메이션 효과
    if mbti in ["ENFP", "ESFP", "ENTP"]:
        st.balloons()
    elif mbti in ["INFJ", "ISFJ", "INFP"]:
        st.snow()
    else:
        st.success("🎒 멋진 여행이 될 거예요!")

# 🧸 하단 메시지
st.markdown("---")
st.markdown("Made with ❤️ by Streamlit")
