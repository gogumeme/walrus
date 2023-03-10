import streamlit as st
import json
import configparser

st.set_page_config(
    page_title="Walrus Coding Club",
    page_icon=":seal:",
)
st.write("#")
st.write("# ๐๏ธHello, Walrus!")

st.write(
    """
#    
### ๐2023๋ ํ์ฌ ์ธ์์์ 
### ๊ฐ์ฅ ์ธ๊ธฐ์๋ ํ๋ก๊ทธ๋๋ฐ ์ธ์ด
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

### ๐ฅณ์ ์ธ๊ธฐ์์ง?
๋ฐฐ์ฐ๊ธฐ ์ฌ์ โ ์ฌ์ฉํ๊ธฐ ์ฌ์ โ ๋์ ์์ฐ์ฑ
"""
)

with st.expander("Hello, World!"):
    st.image(
        "https://moe.work/data/file/free/thumb-2106009379_I60TmeLg_6ea9bebef988b09581938f136a257b30fce63f56_968x1723.png"
    )

with st.expander("Python - open source library"):
    """
    |์ฉ๋|๋ผ์ด๋ธ๋ฌ๋ฆฌ|
    |:-:|-|
    |์นํ๋ ์์ํฌ|[django](https://namu.wiki/w/Django#toc), [flask](https://namu.wiki/w/Flask#toc), [streamlit](https://streamlit.io/), [fastAPI](https://fastapi.tiangolo.com/ko/)|
    |๋ฐ์ดํฐ๋ถ์/์ํ|[pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [SciPy](https://scipy.org/), [SymPy](https://www.sympy.org/en/index.html), [matplotlib](https://matplotlib.org/stable/plot_types/index.html), [seaborn](https://seaborn.pydata.org/examples/index.html)|
    |๋จธ์ ๋ฌ๋|[TensorFlow](https://www.tensorflow.org/?hl=ko), PyTorch, keras|
    |ํ์คํธ๋ถ์|nltk, KoNLpy|
    |GUI|PyQt, tkinter|
    |์น์คํฌ๋ ์ดํ|beautifulSoup4, requests, selenium|
    |์ปดํจํฐ๋น์ |openCV|
    |์ด๋ฏธ์ง์ฒ๋ฆฌ|Pillow|
    |์๋ํ|pyautogui, pywinauto|
    |๊ธ์ต๊ณตํ|quantlib, zipline|
    """
    "- ๊ธฐํ ***42๋ง๊ฐ***์ ๊ฐ์ ธ๋ค ์ฐ๊ธฐ๋ง ํ๋ฉด ๋๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๊ฐ ์กด์ฌ"
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
st.write("### ๐ฏOPEN API: **OPEN DART**")


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
            "์ฌ์์ฐ๋",
            "์ฌ๋ฌด์ ํ๊ตฌ๋ถ",
            "๊ณ์ ID",
            "๊ณ์ ๋ช",
            "๋น๊ธฐ",
            "๋น๊ธฐ๊ธ์ก",
            "์ ๊ธฐ",
            "์ ๊ธฐ๊ธ์ก",
            "์ ์ ๊ธฐ",
            "์ ์ ๊ธฐ๊ธ์ก",
            "์๋ฒ",
            "ํตํ",
        ]

        df


with st.expander("์์ "):
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

fs_cat_dict = {"์ฐ๊ฒฐ": "CFS", "๊ฐ๋ณ": "OFS"}
col1, col2 = st.columns(2)

with col1:
    corp_code = st.selectbox("๊ธฐ์๋ช", options=corp_dict)
    fiscal_year = st.selectbox("์ฐ๋", options=[2021, 2020, 2019, 2018, 2017, 2016, 2015])
with col2:
    fs_cat = st.selectbox("์ฐ๊ฒฐ/๊ฐ๋ณ", options=fs_cat_dict)

if st.button(f"{corp_code} ์ฌ๋ฌด์ ํ ๊ฐ์ ธ์ค๊ธฐ"):
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
### ๐งโ๐study materials
"""
)
with st.expander("๐๋ฌด๋ฃ"):
    st.write(
        """
    - ํ์ด์ฌ ๋ฌธ๋ฒ: [ํ์ด์ฌ ์ฝ๋ฉ๋์ฅ](https://dojang.io/course/view.php?id=7)
    - WEB์๋ฌธ: [์ํ์ฝ๋ฉ](https://opentutorials.org/course/3083)
        - [HTML](https://developer.mozilla.org/ko/docs/Learn/HTML/Introduction_to_HTML/Getting_started), [CSS](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/CSS_basics), [javascript](https://developer.mozilla.org/ko/docs/Web/JavaScript), python([django](https://www.djangoproject.com/), [flask](https://flask.palletsprojects.com/en/2.2.x/))...
        - ์ถ์์ ์ธ ํ๋ก๊ทธ๋๋ฐ ๊ฐ๋์ ๋ค์ํ ์์๋ก ์๊ธฐ์ฝ๊ฒ ์ค๋ช
    - ๋ค์ํ ํ๋ก๊ทธ๋๋ฐ ์ฃผ์ ๋ค: [์ํค๋์ค](https://wikidocs.net/)
        - [์ ํ ํฌ ํ์ด์ฌ](https://wikidocs.net/book/1)
        - [์ด๋ณด์๋ฅผ ์ํ ํ์ด์ฌ 300์ ](https://wikidocs.net/book/922)
        - [์ ํ ํฌ ์ฅ๊ณ ](https://wikidocs.net/book/4223)
        - [pandas dataframe ์์ ์ ๋ณต](https://wikidocs.net/book/7188)
        - [PyTorch๋ก ์์ํ๋ ๋ฅ๋ฌ๋ ์๋ฌธ](https://wikidocs.net/book/2788)
        - [์์ด๋ณด๋ฅผ ์ํ Python: ์ฝ๊ฒ ํ์ด ์ด ๊ธฐ์ด๋ฌธ๋ฒ๊ณผ ์ค์ต](https://wikidocs.net/book/2)
        - [์ฌ์ฅ๋ ๋ชฐ๋ ํ๋ ํ์ด์ฌ ์๋ฌด์๋ํ(๋ถ์ : ๋คํค๋ฉด ์ผ ๋ง์์ง)](https://wikidocs.net/book/6353)
    - ์๊ณ ๋ฆฌ์ฆ ์ฐ์ต: [ํ๋ก๊ทธ๋๋จธ์ค ์ฝ๋ฉํ์คํธ ์ฐ์ต](https://school.programmers.co.kr/learn/challenges?order=recent&page=1)
    """
    )
with st.expander("๐ธ์ ๋ฃ"):
    st.write(
        """
    - ๋ฌด๋ฃ๋ก ๊ณต๋ถํ๋ค๊ฐ ๊ด์ฌ ๊ฐ๋ ์ฃผ์ ๋ฅผ ์ฐพ์๋ณด์!
    - [ํจ์คํธ์บ ํผ์ค](https://fastcampus.co.kr/)
        - ๋ชจ๋ฐ์ผ ์ฑ, ์์/VBA, ์๋ฌด์๋ํ...
    - [์ธํ๋ฐ](https://www.inflearn.com/)
        - ํจ์คํธ์บ ํผ์ค์ ๋น์ทํ๋ฉด์ ๊ฐ์ฑ๋น ์ข์ ๊ฐ์๋ค์ด ๋ง์
    - [๋ธ๋ง๋์ฝ๋](https://nomadcoders.co/)
        - ๋ค์ํ ๊ธฐ์ ์ ํ์ฉํ ์น๊ฐ๋ฐ ๊ฐ์ข
        - Python ๊ฐ์๋ ์์ง๋ง ์ฃผ๋ก javascript ์์ฃผ
    """
    )
with st.expander("๐์ ํ๋ธ"):
    st.write(
        """
    - [๋ธ๋ง๋์ฝ๋](https://www.youtube.com/@nomadcoders)
    - [์กฐ์ฝ๋ฉ](https://www.youtube.com/@jocoding)
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
st.write("### ๐ค์ฝ๋ฉ ๊ณต๋ถ๋ฒ")
st.write("___~~๋ด ์๊ฐ์ ๊ฐ์ํ๋ค~~___")
st.write(
    """
|X|O|
|:-:|:-:|
|์ฑ/๊ฐ์๋ก๋ง ๊ณต๋ถํ๋ค|๋ฐฐ์ด ๋ด์ฉ์ ํ์ฉํด ๋ญ๊ฐ ๋ง๋ค์ด๋ณธ๋ค|
|๊ณต๋ถํ ๋ด์ฉ์ ์ ๋ถ ์๊ธฐํ๋ค(์๊ฐ๋ญ๋น)|๊ธฐ์ต ์๋๋ฉด ๊ตฌ๊ธ ๊ฒ์(ctrl+c/ctrl+v)|
|๋ก๋๋งต์ ์ฐพ์ ์ฐฉ์คํ ๊ณต๋ถํ๋ค|์ผ๋จ ๋ง๋ค๋ค๊ฐ ๋งํ๋ ๋ถ๋ถ์ ์ตํ๋ค|
|๋ฐ๋๋ผ์ธ ์์ด ๊ณต๋ถํ๋ค|๋ฐ๋๋ผ์ธ์ ์ ํด๋๊ณ  ๊ณต๋ถํ๋ค|
  
#
- ํผ์ ๊ณต๋ถํ๋ฉด ๋งํ๋ ๋ถ๋ถ์ด ๋ง์์
- ์๋ฌ๊ฐ ๋๊ฑฐ๋ ์ํ๋ ๊ฒฐ๊ณผ๊ฐ ์๋์ฌ๋
    - ๊ตฌ๊ธ ๊ฒ์๐ / ๊ฐ์ด ๊ณ ๋ฏผํด๋ด์๐ค
- ๋ฐฐ์ฐ๋ ์ธ์ด์ [์ฝ๋ฉ ์ปจ๋ฒค์](https://yoonpunk.tistory.com/1)์ ๋ฐ๋ฅด์.
    - [naming conventions](https://realpython.com/python-pep8/#naming-conventions)์ด ๊ฐ์ฅ ์ค์
    - ๋๋จธ์ง๋ IDE(vscode)์์ ์์์ ๊ต์ ํด์ค
"""
)
if st.button("๋น ๋ฅด๊ฒ ๋ฐฐ์ฐ๋ ๋ฐฉ๋ฒ"):
    st.exception(RuntimeError("๊ทธ๋ฐ ๋ฐฉ๋ฒ์ ์์ ์๊ฐ ์์ด์(๋จํธ)"))


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
### ๐Python ๊ฐ๋ฐํ๊ฒฝ ๊ตฌ์ถ
"""
)
with st.expander("Python ์ค์น"):
    st.write(
        """
    - [Python.org](https://www.python.org/)
    - Downloads
    - ์ต์ ๋ฒ์ ์ด๋ผ๊ณ  ๋ค ์ข์ง๋ ์์
        - ๋ผ์ด๋ธ๋ฌ๋ฆฌ์ ๋ฐ๋ผ ์ต์ ๋ฒ์ ์ ์ง์ํ์ง ์๋ ๊ฒฝ์ฐ๋ ์์
        - ํ์ง๋ง ์ฐ๋ฆฌ๋ ๋ฌด์ํ๊ณ  3.11.2 ๋ฒ์ ์ผ๋ก!
    - **์ค์**
        - ์ค์น ํ์ผ ์คํ ํ ํ๋จ์ `Add python.exe to Path`๋ฅผ ๋ฐ๋์ โ
    """
    )

with st.expander("Visual Studio Code ์ค์น"):
    st.write(
        """
    - [Visual Studio Code](https://code.visualstudio.com/download)
    - vscode: ํ๋ก๊ทธ๋๋ฐ๊ณ์ ms word/ํ๊ธ
    - ๋ณธ์ธ์ ์ด์์ฒด์ ์ ๋ง๋ ๋ฒ์ ์ผ๋ก ์ค์น
    """
    )

st.write("[Python & vscode ์ค์น ๋ฐฉ๋ฒ ์ฐธ๊ณ ](https://kgokapc.tistory.com/199)")


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
### ๐ฆญWalrus := coding club
"""
)
with st.expander("๐๋ชฉ์ "):
    st.write(
        """
    - [์ปดํจํ ์ฌ๊ณ ](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=aporia25&logNo=221171778914)
        - ๋ฌธ์ ๋ถํด, ์ถ์ํ, ํจํด์ธ์, ์๊ณ ๋ฆฌ์ฆ, ์๋ํ
    - ์ฐฝ์์  ๋ฌธ์ ํด๊ฒฐ
    - ๊ณต์ฌ์ ์๋ฌด ํ์ ์ ์ด๋ฐ์ง๋ ๋ค
    """
    )
with st.expander("๐งญ๋์๊ฐ ๋ฐฉํฅ"):
    st.write(
        """
    - **Phase 1**: ๊ธฐ์ด ๋ฌธ๋ฒ ํ์ต
        - ~~์ด๋ ต์ง ์์์.~~
    - **Phase 2**: ์์ฉ ๋ฌธ์  + ์๋ํ
        - ๊ธฐ์ด ๋ฌธ๋ฒ์ ํ์ฉํด์ ์์ ๋ฌธ์ ๋ค์ ํด๊ฒฐํด์.
    - **Phase 3**: ํ ์ด ํ๋ก์ ํธ
        - ์์คํ๊ตฌ์ถ์ ํ๊ธฐ์ ์๊ฑฐ๋ ๊ฐ๊ณ  ๊ฐ์ธ์ด ํด๊ฒฐํ๊ธฐ์๋ ๋ง์ ์๊ฐ์ด ์์๋๋ ์๋ฌด๋ฅผ ํด๊ฒฐํด์.
    - ๋ถ๋ด๋ธ๋ธ! ๋ฌธ์ ํด๊ฒฐ์ ์ฆ๊ฒจ๋ณด์์!
    """
    )

with st.expander("๐ ์ด์ ๋ฐฉ์"):
    st.write(
        """
    - ์ 1~2ํ ์ ์ฌ ์๊ฐ์ ๋ชจ์ฌ์!
    - ์์  ์์จ(์ด์ง๋ง ์ด์ฌํ ํด์ฃผ์ธ์)
    - ์ง๋ฌธ ํ์
    """
    )
