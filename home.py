import streamlit as st
import json

st.set_page_config(
    page_title="Walrus Coding Club",
    page_icon="🦭",
)

st.write("# 🖐️Hello, Walrus!")

st.write(
    """
#    
### 2023년 현재 세상에서 
### 가장 인기있는 프로그래밍 언어
#### [GitHut2.0](https://madnight.github.io/githut/#/pull_requests/2022/4)
#
### 왜 인기있지?
배우기 쉬움 → 사용하기 쉬움 → 높은 생산성
"""
)

with st.expander("Hello, World!"):
    st.image(
        "https://moe.work/data/file/free/thumb-2106009379_I60TmeLg_6ea9bebef988b09581938f136a257b30fce63f56_968x1723.png"
    )

with st.expander("open source library"):
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

st.write("#")
st.write("### OPEN API: **OPEN DART**")


def get_fs(code, year, cat):
    import requests
    import pandas as pd

    # https://opendart.fss.or.kr/
    ENDPOINT = "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json"
    APIKEY = "7491258925ffb7eeeb591110651f67100e3f7125"
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


# with col3:
