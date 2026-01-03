import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Essential for mobile view
st.set_page_config(page_title="AlphaLog", layout="centered")

# This creates the CSV on the server if it doesn't exist
if not os.path.exists("trades.csv"):
    pd.DataFrame(columns=["Ticker", "Side", "Account", "Entry", "Exit", "PnL", "Date"]).to_csv("trades.csv", index=False)

st.title("📱 AlphaLog Mobile")

# Entry Form
with st.form("trade_form", clear_on_submit=True):
    ticker = st.text_input("Ticker").upper()
    side = st.selectbox("Side", ["Long", "Short"])
    acc = st.selectbox("Account", ["Real", "Demo"])
    en = st.number_input("Entry", format="%.5f")
    ex = st.number_input("Exit", format="%.5f")
    stat = st.selectbox("Status", ["Win", "Loss", "BE", "Open"])
    
    if st.form_submit_button("Save Trade"):
        pnl = (ex - en) if side == "Long" else (en - ex)
        new_row = [ticker, side, acc, en, ex, round(pnl, 2), datetime.now().strftime("%Y-%m-%d")]
        df = pd.read_csv("trades.csv")
        df.loc[len(df)] = new_row
        df.to_csv("trades.csv", index=False)
        st.success("Saved!")
        st.rerun()

# History
st.subheader("Recent Trades")
df_view = pd.read_csv("trades.csv")
if not df_view.empty:
    st.dataframe(df_view.tail(5), use_container_width=True)