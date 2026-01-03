import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Mobile optimized layout
st.set_page_config(page_title="AlphaLog Pro", layout="centered")

DATA_FILE = "trades.csv"

# Initialize CSV with all your specific columns
def load_data():
    cols = ["Ticker", "Leverage", "Account", "Entry Time", "Exit Time", 
            "Duration", "Direction", "Entry Price", "Exit Price", 
            "TP1", "TP2", "SL", "Result", "$$", "Why"]
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=cols)

st.title("📈 AlphaLog Pro")

# --- INPUT FORM ---
with st.expander("📝 Log New Trade", expanded=True):
    with st.form("trade_form", clear_on_submit=True):
        # Row 1: Basics
        ticker = st.text_input("TICKER").upper()
        
        c1, c2 = st.columns(2)
        leverage = c1.text_input("Leverage", value="10x")
        account = c2.selectbox("Taken", ["Real", "Demo"])
        
        # Row 2: Times
        c3, c4 = st.columns(2)
        # Default to now, but user can edit
        entry_time = c3.text_input("Entry Time", value=datetime.now().strftime("%Y-%m-%d %H:%M"))
        exit_time = c4.text_input("Exit Time", value=datetime.now().strftime("%Y-%m-%d %H:%M"))
        
        # Row 3: Direction & Prices
        direction = st.radio("Direction", ["Long", "Short"], horizontal=True)
        
        c5, c6 = st.columns(2)
        en_p = c5.number_input("Entry Price", format="%.5f")
        ex_p = c6.number_input("Exit Price", format="%.5f")
        
        # Row 4: Targets
        c7, c8, c9 = st.columns(3)
        tp1 = c7.number_input("TP1", format="%.5f")
        tp2 = c8.number_input("TP2", format="%.5f")
        sl = c9.number_input("SL", format="%.5f")
        
        # Row 5: Outcome
        result = st.selectbox("Result", ["Win", "Loss", "BE", "Open"])
        why = st.text_area("Why?")
        
        if st.form_submit_button("💾 SAVE TRADE"):
            # 1. Calculate PnL ($$)
            pnl = (ex_p - en_p) if direction == "Long" else (en_p - ex_p)
            
            # 2. Calculate Duration
            try:
                t1 = datetime.strptime(entry_time, "%Y-%m-%d %H:%M")
                t2 = datetime.strptime(exit_time, "%Y-%m-%d %H:%M")
                duration = str(t2 - t1)
            except:
                duration = "Format Error"

            # 3. Create Data Row
            new_row = {
                "Ticker": ticker, "Leverage": leverage, "Account": account,
                "Entry Time": entry_time, "Exit Time": exit_time,
                "Duration": duration, "Direction": direction,
                "Entry Price": en_p, "Exit Price": ex_p,
                "TP1": tp1, "TP2": tp2, "SL": sl,
                "Result": result, "$$": round(pnl, 2), "Why": why
            }
            
            df = load_data()
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success(f"Successfully Logged {ticker}!")
            st.rerun()

# --- RECENT TRADES ---
st.markdown("---")
df_display = load_data()
if not df_display.empty:
    st.metric("Total PnL", f"${df_display['$$'].sum():,.2f}")
    st.subheader("Last 5 Trades")
    # Horizontal scroll for mobile
    st.dataframe(df_display.tail(5), use_container_width=True)