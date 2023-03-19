import requests
import sqlite3
import streamlit as st
import pandas as pd

def main():
    response = requests.get("https://dt.miet.ru/ppo_it_final",
                            headers={"X-Auth-Token": "xutgb523"})
    print(response.text)

main()