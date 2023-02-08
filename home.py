import streamlit as st
import json
import configparser

st.set_page_config(
    page_title="Walrus Coding Club",
    page_icon=":seal:",
)
st.write("#")
st.write("# 🖐️Hello, Walrus!")

st.write(
    """
#    
### 🌏2023년 현재 세상에서 
### 가장 인기있는 프로그래밍 언어
#### [GitHut2.0](https://madnight.github.io/githut/#/pull_requests/2022/4)
#
#
#
#
#
#
#
#
#

### 🥳왜 인기있지?
배우기 쉬움 → 사용하기 쉬움 → 높은 생산성
"""
)

with st.expander("Hello, World!"):
    st.image(
        "https://moe.work/data/file/free/thumb-2106009379_I60TmeLg_6ea9bebef988b09581938f136a257b30fce63f56_968x1723.png"
    )

with st.expander("Python - open source library"):
    """
    |용도|라이브러리|
    |:-:|-|
    |웹프레임워크|[django](https://namu.wiki/w/Django#toc), [flask](https://namu.wiki/w/Flask#toc), [streamlit](https://streamlit.io/), [fastAPI](https://fastapi.tiangolo.com/ko/)|
    |데이터분석/수학|[pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [SciPy](https://scipy.org/), [SymPy](https://www.sympy.org/en/index.html), [matplotlib](https://matplotlib.org/stable/plot_types/index.html), [seaborn](https://seaborn.pydata.org/examples/index.html)|
    |머신러닝|[TensorFlow](https://www.tensorflow.org/?hl=ko), PyTorch, keras|
    |텍스트분석|nltk, KoNLpy|
    |GUI|PyQt, tkinter|
    |웹스크레이핑|beautifulSoup4, requests, selenium|
    |컴퓨터비전|openCV|
    |이미지처리|Pillow|
    |자동화|pyautogui, pywinauto|
    |금융공학|quantlib, zipline|
    """
    "- 기타 ***42만개***의 가져다 쓰기만 하면 되는 라이브러리가 존재"
    "- [pypi.org](https://pypi.org/)"

st.write(
    """
#
# 
# 
# 
# 
# 
# 
# 
# """
)
st.write("### 🎯OPEN API: **OPEN DART**")


def get_fs(code, year, cat):
    import requests
    import pandas as pd

    # https://opendart.fss.or.kr/
    ENDPOINT = "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json"
    try:
        c = configparser.ConfigParser()
        c.read("config.ini")
        APIKEY = c["A"]["APIKEY"]
    except:
        APIKEY = st.secrets["APIKEY"]
    params = {
        "crtfc_key": APIKEY,
        "corp_code": code,
        "bsns_year": year,
        "reprt_code": "11011",
        "fs_div": cat,
    }
    response = requests.get(ENDPOINT, params=params)
    fs_json = json.loads(response.text)
    msg = f"{fs_json['status']=!s}, {fs_json['message']=!s}"
    st.markdown(
        f"""
    ```py
    {msg}
    ```
    """
    )
    if fs_json["status"] == "000":
        df = pd.DataFrame(fs_json["list"])
        df = df[
            [
                "bsns_year",
                "sj_nm",
                "account_id",
                "account_nm",
                "thstrm_nm",
                "thstrm_amount",
                "frmtrm_nm",
                "frmtrm_amount",
                "bfefrmtrm_nm",
                "bfefrmtrm_amount",
                "ord",
                "currency",
            ]
        ]
        df.columns = [
            "사업연도",
            "재무제표구분",
            "계정ID",
            "계정명",
            "당기",
            "당기금액",
            "전기",
            "전기금액",
            "전전기",
            "전전기금액",
            "순번",
            "통화",
        ]

        df


with st.expander("예제"):
    st.write(
        """
    ```py
    import requests
    # https://opendart.fss.or.kr/
    ENDPOINT = 'https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json'
    APIKEY = 'xxxxxxxxxxxxxxxxxxxxxxxx'
    params = {
        'crtfc_key': APIKEY,
        'corp_code': '00126380',
        'bsns_year': '2021',
        'reprt_code': '11011',
        'fs_div': 'CFS',
    }
    response = requests.get(ENDPOINT, params=params)
    ```
    """
    )

with open("corpcode.json", "r", encoding="utf-8") as f:
    corp_dict = json.load(f)

fs_cat_dict = {"연결": "CFS", "개별": "OFS"}
col1, col2 = st.columns(2)

with col1:
    corp_code = st.selectbox("기업명", options=corp_dict)
    fiscal_year = st.selectbox("연도", options=[2021, 2020, 2019, 2018, 2017, 2016, 2015])
with col2:
    fs_cat = st.selectbox("연결/개별", options=fs_cat_dict)

if st.button(f"{corp_code} 재무제표 가져오기"):
    get_fs(corp_dict[corp_code], fiscal_year, fs_cat_dict[fs_cat])


st.write(
    """
#
#
#
#
#
#
#
#
#
### 🧑‍🎓study materials
"""
)
with st.expander("🆓무료"):
    st.write(
        """
    - 파이썬 문법: [파이썬 코딩도장](https://dojang.io/course/view.php?id=7)
    - WEB입문: [생활코딩](https://opentutorials.org/course/3083)
        - [HTML](https://developer.mozilla.org/ko/docs/Learn/HTML/Introduction_to_HTML/Getting_started), [CSS](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/CSS_basics), [javascript](https://developer.mozilla.org/ko/docs/Web/JavaScript), python([django](https://www.djangoproject.com/), [flask](https://flask.palletsprojects.com/en/2.2.x/))...
        - 추상적인 프로그래밍 개념을 다양한 예시로 알기쉽게 설명
    - 다양한 프로그래밍 주제들: [위키독스](https://wikidocs.net/)
        - [점프 투 파이썬](https://wikidocs.net/book/1)
        - [초보자를 위한 파이썬 300제](https://wikidocs.net/book/922)
        - [점프 투 장고](https://wikidocs.net/book/4223)
        - [pandas dataframe 완전정복](https://wikidocs.net/book/7188)
        - [PyTorch로 시작하는 딥러닝 입문](https://wikidocs.net/book/2788)
        - [왕초보를 위한 Python: 쉽게 풀어 쓴 기초문법과 실습](https://wikidocs.net/book/2)
        - [사장님 몰래 하는 파이썬 업무자동화(부제: 들키면 일 많아짐)](https://wikidocs.net/book/6353)
    - 알고리즘 연습: [프로그래머스 코딩테스트 연습](https://school.programmers.co.kr/learn/challenges?order=recent&page=1)
    """
    )
with st.expander("💸유료"):
    st.write(
        """
    - 무료로 공부하다가 관심 가는 주제를 찾아보자!
    - [패스트캠퍼스](https://fastcampus.co.kr/)
        - 모바일 앱, 엑셀/VBA, 업무자동화...
    - [인프런](https://www.inflearn.com/)
        - 패스트캠퍼스와 비슷하면서 가성비 좋은 강의들이 많음
    - [노마드코더](https://nomadcoders.co/)
        - 다양한 기술을 활용한 웹개발 강좌
        - Python 강의도 있지만 주로 javascript 위주
    """
    )
with st.expander("🎞유튜브"):
    st.write(
        """
    - [노마드코더](https://www.youtube.com/@nomadcoders)
    - [조코딩](https://www.youtube.com/@jocoding)
    """
    )

st.write(
    """
#
# 
# 
# 
# 
# 
# 
# 
# """
)
st.write("### 🤓코딩 공부법")
st.write("___~~내 생각을 강요한다~~___")
st.write(
    """
|X|O|
|:-:|:-:|
|책/강의로만 공부한다|배운 내용을 활용해 뭔가 만들어본다|
|공부한 내용을 전부 암기한다(시간낭비)|기억 안나면 구글 검색(ctrl+c/ctrl+v)|
|로드맵을 찾아 착실히 공부한다|일단 만들다가 막히는 부분을 익힌다|
|데드라인 없이 공부한다|데드라인을 정해두고 공부한다|
  
#
- 혼자 공부하면 막히는 부분이 많아요
- 에러가 나거나 원하는 결과가 안나올때
  - 구글 검색👍 / 같이 고민해봐요🤔
- 배우는 언어의 [코딩 컨벤션](https://yoonpunk.tistory.com/1)을 따르자.
"""
)
if st.button("빠르게 배우는 방법"):
    st.exception(RuntimeError("그런 방법은 있을 수가 없어요(단호)"))


st.write(
    """
#
#
#
#
#
#
#
#
#
### 🐍Python 개발환경 구축
"""
)
with st.expander("Python 설치"):
    st.write(
        """
    - [Python.org](https://www.python.org/)
    - Downloads
    - 최신버전이라고 다 좋지는 않음
        - 라이브러리에 따라 최신버전을 지원하지 않는 경우도 있음
        - 하지만 우리는 무시하고 3.11.2 버전으로!
    - **중요**
        - 설치 파일 실행 후 하단에 `Add python.exe to Path`를 반드시 ✅
    """
    )

with st.expander("Visual Studio Code 설치"):
    st.write(
        """
    - [Visual Studio Code](https://code.visualstudio.com/download)
    - vscode: 프로그래밍계의 ms word/한글
    - 본인의 운영체제에 맞는 버전으로 설치
    """
    )

st.write(
    """
#
#
#
#
#
#
#
#
#
### 🦭Walrus := coding club
"""
)
with st.expander("😎목적"):
    st.write(
        """
    - [컴퓨팅 사고](https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%93%A8%ED%8C%85_%EC%82%AC%EA%B3%A0)
    - 문제분해, 패턴인식, 자료표현, 일반화/추상화, 알고리즘
    - 창의적 문제해결
    - 공사의 업무 혁신에 이바지는 덤
    """
    )
with st.expander("🧭나아갈 방향"):
    st.write(
        """
    - **Phase 1**: 기초 문법 학습
        - ~~어렵지 않아요.~~
    - **Phase 2**: 응용 문제 + 자동화
        - 기초 문법을 활용해서 작은 문제들을 해결해요.
    - **Phase 3**: 토이 프로젝트
        - 시스템구축을 하기엔 작거나 같고 개인이 해결하기에는 많은 시간이 소요되는 업무를 해결해요.
    - 부담노노!
    - 프로그래밍은 문제해결 과정의 연속, 문제해결을 즐겨보아요!
    """
    )

with st.expander("🎠운영 방식"):
    st.write(
        """
    - 월 1~2회 점심 시간에 모여요!
    - 완전 자율(이지만 열심히 해주세요)
    - 질문 환영
    """
    )
