import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("📊 Career Guidance Admin Dashboard")

conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT * FROM students", conn)

st.metric("Total Students", len(df))
st.dataframe(df)

st.download_button(
    "⬇️ Download CSV",
    df.to_csv(index=False),
    "career_leads.csv"
)
