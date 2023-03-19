import requests
import sqlite3
import streamlit as st
import pandas as pd
import json


def data_update():
    response = requests.get("https://dt.miet.ru/ppo_it_final",
                            headers={"X-Auth-Token": "xutgb523"})

    if response.status_code == 200:
        data = json.loads(response.text)



def main():
    st.set_page_config(
        page_title="Дни",
        layout="wide")

    resbtn = st.button("Обновить данные")
    if resbtn:
        st.experimental_rerun()

    st.title("Данные с датчиков температуры и влажности")

main()