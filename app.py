import streamlit as st

print("page reloaded")
st.set_page_config(
     page_title="웹툰 백과사전",
     page_icon="./images/webtoon.png"
)
st.markdown("""
<style>
img { 
    max-height: 300px; 
}
.streamlit-expanderContent div {
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
.streamlit-expanderHeader {
    pointer-events: none;
}
[data-testid="StyledFullScreenButton"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
st.title("streamlit 웹툰 도감")
#st.text("포켓몬을 하나씩 추가해서 도감을 채워보세요!")
#st.subheader("포켓몬을 하나씩 추가해서 도감을 채워보세요!")
#subheader: 소제목 같은 걸 표현할 때 많이 사용
st.markdown("**웹툰**을 하나씩 추가해서 도감을 채워보세요!")

type_webtoon_dict = {
    "일요일":"日",
    "월요일":"月",
    "화요일":"火",
    "수요일":"水",
    "목요일":"木",
    "금요일":"金",
    "토요일":"土",  
    "매일":"매일"
}
initial_webtoon = [
    {
        "name": "신의탑",
        "types": ["월요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F183559%2Fthumbnail%2Fthumbnail_IMAG21_5f3fec31-5c95-4afe-a73f-3046288edb47.jpg"
    },
    {
        "name": "칼가는 소녀",
        "types": ["월요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F730174%2Fthumbnail%2Fthumbnail_IMAG21_5bfd08ed-6ca8-4a27-9fab-d9fb15588d3a.jpg",
    },
    {
        "name": "퀘스트 지상주의",
        "types": ["월요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F783052%2Fthumbnail%2Fthumbnail_IMAG21_800f4c56-26ac-419e-9ed0-baf322311dea.jpg",
    },
    {
        "name": "1331",
        "types": ["화요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F796618%2Fthumbnail%2Fthumbnail_IMAG21_82cd76ac-f250-40b9-b143-7a1cd467efa1.jpg"
    },
    {
        "name": "마루는 강쥐",
        "types": ["화요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F796152%2Fthumbnail%2Fthumbnail_IMAG21_26b9c1d8-ca2d-4fc7-87ea-a3334634236a.jpg"
    },
    {
        "name": "마음의 소리2",
        "types": ["화요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F814543%2Fthumbnail%2Fthumbnail_IMAG21_df84a681-b7ef-4dda-8cef-25b219d35e3e.jpg"
    },
    {
        "name": "조조코믹스",
        "types": ["수요일","토요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F774862%2Fthumbnail%2Fthumbnail_IMAG21_39b7c327-7234-4636-b608-401478abede3.jpg"
    },
    {
        "name": "수요웹툰의 나강림",
        "types": ["수요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F771718%2Fthumbnail%2Fthumbnail_IMAG21_8d86de3e-15d5-464e-b448-cbd73b1bd71c.jpg"
    },
    {
        "name": "급식아빠",
        "types": ["수요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F758662%2Fthumbnail%2Fthumbnail_IMAG21_0c8a2c9e-b2de-4346-8ac6-c8e2c0a5bfe5.jpg"
    },
    {
        "name": "아인슈폐너",
        "types": ["목요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F792280%2Fthumbnail%2Fthumbnail_IMAG21_ed25f3e6-0834-4b13-8d29-34d78037b8c5.jpg"
    },
    {
        "name": "재벌집 막내아들",
        "types": ["목요일"],
        "image_url": "https://search.pstatic.net/common?type=n&size=276x276&quality=95&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F800770%2Fthumbnail%2Fthumbnail_IMAG19_ea7caaf9-3531-46e3-bf54-4ead64ec28e8.jpg"
    },
    {
        "name": "외모지상주의",
        "types": ["금요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F641253%2Fthumbnail%2Fthumbnail_IMAG21_01672165-03c8-44b1-ba0e-ef82c9cfcd10.jpg"
    },
    {
        "name": "재혼 황후",
        "types": ["금요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F735661%2Fthumbnail%2Fthumbnail_IMAG21_4b3c44a0-f286-4878-bac3-84c3ec9dc0a1.jpg"
    },
    {
        "name": "A.I 닥터",
        "types": ["금요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F765804%2Fthumbnail%2Fthumbnail_IMAG21_011afdde-cc86-418b-94ed-7baa9e11f094.jpg"
    },
    {
        "name": "세레나",
        "types": ["토요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F801475%2Fthumbnail%2Fthumbnail_IMAG21_63818a49-407c-4d1d-8f9a-e541285abdd9.jpg"
    },
    {
        "name": "아홉수 우리들",
        "types": ["토요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F724815%2Fthumbnail%2Fthumbnail_IMAG21_4bdd52f2-bbc9-4524-b44b-adc1e7208f93.jpg"
    },
    {
        "name": "기기기괴2",
        "types": ["일요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F821851%2Fthumbnail%2Fthumbnail_IMAG21_d67261bc-0aea-495c-b92e-07dc2c1785cd.jpg"
    },
    {
        "name": "내일",
        "types": ["일요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F695796%2Fthumbnail%2Fthumbnail_IMAG21_332bb25b-c77d-477f-9979-5a8607ebd7a5.jpg"
    },
    {
        "name": "수희0",
        "types": ["일요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F774831%2Fthumbnail%2Fthumbnail_IMAG21_b4644a73-ecfb-4532-a96c-575b02accfd0.jpg"
    },
    {
        "name": "휴재일기",
        "types": ["일요일"],
        "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F807071%2Fthumbnail%2Fthumbnail_IMAG21_3bf72b83-7975-4409-8104-d4cdb8003752.jpg"
    }
]


example_webtoon = {
    "name": "1331",
    "types": ["화요일"],
    "image_url": "https://search.pstatic.net/common?type=f&size=174x226&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F796618%2Fthumbnail%2Fthumbnail_IMAG21_82cd76ac-f250-40b9-b143-7a1cd467efa1.jpg"
}


if "webtoon" not in st.session_state:
    st.session_state.webtoon=initial_webtoon


auto_complete=st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete",auto_complete)
#toggle: 자동완성
with st.form(key="form"):
    col1,col2 =st.columns(2)
    with col1:
        name=st.text_input(label="웹툰 이름",
        value=example_webtoon["name"] if auto_complete  else"")
    with col2:
         types=st.multiselect(label="웹툰 요일 입력",
                         options=list(type_webtoon_dict.keys()),
                         max_selections=2,
                         default=example_webtoon["types"] if auto_complete else [])
    image_url= st.text_input(label="웹툰 이미지 입력",
                              value=example_webtoon["image_url"] if auto_complete else "")

    submit=st.form_submit_button(label="submit")
    if submit:
        if not name:
                st.error("웹툰의 이름을 입력해주세요.")
        elif len(types)==0:
                st.error("웹툰 요일을 적어도 한개 선택해주세요.")
        else:
                st.success("웹툰을 추가할 수 있습니다.")
                st.session_state.webtoon.append({
                    "name":name,
                    "types":types,
                    "image_url":image_url if image_url else "./images/default.png"
                })


for i in range(0,len(st.session_state.webtoon),4): #pokemons의 배열의 크기까지 반복이고 간격은 3만큼 지정
    row_webtoon = st.session_state.webtoon[i:i+4]
    cols = st.columns(4)
    for j in range(len(row_webtoon)):
        with cols[j]:
           webtoon= row_webtoon[j]
           with st.expander(label=f"**{i + j + 1}. {webtoon['name']}**", expanded=True):
                st.image(webtoon["image_url"])
                emoji_types = [f"{type_webtoon_dict[x]} {x}" for x in webtoon["types"]]
                st.text(" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i + j, use_container_width=True)
                if delete_button:
                    del st.session_state.webtoon[i + j]
                    st.rerun() #session_state가 화면에 반영되기 위해서는 rerun을 이용
                #페이지가 리로드 되면서 delete_button이라는 변수에다가 true값을 할당하고 아래의 조건문이 실행되도록 하는 구조
# streamlit은 ui의 변경 요소가 추가될 경우:전체 페이지를 리로딩하는 특징을 가지고 있음
#sessoin state:페이지가 살아있는 동안에 데이터를 저장할 수있는 공간




