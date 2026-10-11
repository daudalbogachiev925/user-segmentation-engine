import os
import requests
import pandas as pd
import plotly.express as px
import streamlit as st

API = os.getenv("API_URL", "http://api:8000")
st.set_page_config(page_title="Segmentation", layout="wide")
st.title("User Segmentation Engine")

@st.cache_data(ttl=15)
def fetch(path):
    return requests.get(f"{API}{path}").json()

users = pd.DataFrame(fetch("/api/users"))
if users.empty:
    st.warning("Нет пользователей")
    st.stop()

c1, c2, c3 = st.columns(3)
c1.metric("Пользователей", len(users))
c2.metric("Общий revenue", f"{users.monetary.sum():,.0f}")
c3.metric("Средний чек", f"{users.monetary.mean():,.0f}")

if st.button("Пересчитать сегменты"):
    st.json(requests.post(f"{API}/api/segments/recompute").json())
    st.cache_data.clear()

rfm = pd.DataFrame(fetch("/api/segments/rfm"))
if not rfm.empty:
    st.subheader("RFM сегменты")
    st.plotly_chart(px.bar(rfm, x="segment", y="total_monetary"))
    st.dataframe(rfm)

abc = pd.DataFrame(fetch("/api/segments/abc"))
if not abc.empty:
    st.subheader("ABC анализ")
    st.plotly_chart(px.pie(abc, names="class", values="revenue"))
