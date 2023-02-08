import streamlit as st
import json
import configparser
import requests

try:
    c = configparser.ConfigParser()
    c.read("config.ini")
    APIKEY = c["A"]["APIKEY"]
except:
    APIKEY = st.secrets["APIKEY"]

def get_url(code):
    ENDPOINT = "https://opendart.fss.or.kr/api/company.json"
    params = {
        "crtfc_key": APIKEY,
        "corp_code": code
    }
    response = requests.get(ENDPOINT, params=params, verify=False)
    response.json()['hm_url']
    

with open("corpcode.json", "r", encoding="utf-8") as f:
    corp_dict = json.load(f)

corp_code = st.selectbox("기업명", options=corp_dict)

if st.button(f"{corp_code} 홈페이지!"):
    get_url(corp_dict[corp_code])