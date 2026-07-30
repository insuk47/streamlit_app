import streamlit as st
import random

st.set_page_config(
    page_title="MBTI 여행 추천",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background-color:#FFF8F2;
}

h1{
    color:#FF69B4;
    text-align:center;
}

.travel-box{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0 8px 20px rgba(0,0,0,0.1);
}

.reason{
    background:#FFF0F5;
    padding:15px;
    border-radius:15px;
}

.sidebar .sidebar-content{
    background:#FDE2E4;
}

button{
    border-radius:12px;
}

</style>
""",unsafe_allow_html=True)

st.title("✈️ MBTI 여행 추천 서비스")

st.write("### 당신의 성격에 맞는 최고의 여행지를 추천해드립니다 😊")

# ------------------------------------------
# 데이터
# ------------------------------------------

travel = {

"INTJ":[
{
"name":"아이슬란드",
"image":"https://images.unsplash.com/photo-1506744038136-46273834b3fb",
"reason":"조용한 자연과 깊은 사색을 즐길 수 있어요."
},
{
"name":"스위스",
"image":"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
"reason":"계획적인 여행을 좋아하는 INTJ에게 최고의 여행지입니다."
}
],

"INTP":[
{
"name":"일본 교토",
"image":"https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e",
"reason":"역사와 문화 탐험을 좋아하는 당신에게 딱!"
}
],

"ENTP":[
{
"name":"뉴욕",
"image":"https://images.unsplash.com/photo-1499092346589-b9b6be3e94b2",
"reason":"새로운 사람과 다양한 경험이 가득합니다."
}
],

"ENFP":[
{
"name":"발리",
"image":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
"reason":"감성 가득한 휴양지!"
}
],

"INFJ":[
{
"name":"프라하",
"image":"https://images.unsplash.com/photo-1519677100203-a0e668c92439",
"reason":"감성적인 골목과 아름다운 풍경."
}
],

"ISFJ":[
{
"name":"경주",
"image":"https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
"reason":"역사와 평화를 함께 느낄 수 있어요."
}
],

"ISTJ":[
{
"name":"독일",
"image":"https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
"reason":"계획적인 여행을 좋아하는 당신에게 추천!"
}
],

"ISTP":[
{
"name":"뉴질랜드",
"image":"https://images.unsplash.com/photo-1502784444185-1e7d0a5d8c4b",
"reason":"액티비티 천국!"
}
],

"ESTP":[
{
"name":"호주",
"image":"https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9",
"reason":"서핑과 액티비티!"
}
],

"ESFP":[
{
"name":"하와이",
"image":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
"reason":"신나는 휴양!"
}
],

"ESFJ":[
{
"name":"제주도",
"image":"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
"reason":"가족과 함께 최고의 여행."
}
],

"ESTJ":[
{
"name":"싱가포르",
"image":"https://images.unsplash.com/photo-1525625293386-3f8f99389edd",
"reason":"깔끔하고 효율적인 여행!"
}
],

"ISFP":[
{
"name":"산토리니",
"image":"https://images.unsplash.com/photo-1500375592092-40eb2168fd21",
"reason":"감성 폭발!"
}
],

"INFP":[
{
"name":"핀란드",
"image":"https://images.unsplash.com/photo-1517821365201-7734f463f1a5",
"reason":"동화 같은 풍경."
}
],

"ENTJ":[
{
"name":"두바이",
"image":"https://images.unsplash.com/photo-1512453979798-5ea266f8880c",
"reason":"도전과 성공을 좋아하는 당신!"
}
],

"ENFJ":[
{
"name":"파리",
"image":"https://images.unsplash.com/photo-1499856871958-5b9627545d1a",
"reason":"사람과 문화를 사랑하는 ENFJ!"
}
]

}

# ------------------------------------------
# Sidebar
# ------------------------------------------

st.sidebar.title("⚙️ 여행 설정")

mbti = st.sidebar.selectbox(
"MBTI",
list(travel.keys())
)

country = st.sidebar.radio(
"여행 종류",
["국내","해외"]
)

budget = st.sidebar.select_slider(
"예산",
options=["30만원","50만원","100만원","200만원 이상"]
)

style = st.sidebar.selectbox(
"여행 스타일",
["힐링","맛집","사진","액티비티","쇼핑"]
)

# ------------------------------------------
# 추천 버튼
# ------------------------------------------

if st.button("🎁 여행 추천받기"):

    place = random.choice(travel[mbti])

    st.balloons()

    col1,col2 = st.columns([1,1])

    with col1:

        st.image(place["image"])

    with col2:

        st.markdown(f"""
<div class="travel-box">

# 📍 {place["name"]}

### 💖 추천 이유

<div class="reason">

{place["reason"]}

</div>

### ✈️ 추천 여행 스타일

- {style}

### 💰 추천 예산

- {budget}

### 🌎 여행 형태

- {country}

</div>
""",unsafe_allow_html=True)

    st.divider()

    st.subheader("🧳 준비물 체크리스트")

    st.checkbox("여권")
    st.checkbox("충전기")
    st.checkbox("보조배터리")
    st.checkbox("카메라")
    st.checkbox("상비약")
    st.checkbox("모자")
    st.checkbox("선크림")

    st.success("즐거운 여행 되세요! 😊")
