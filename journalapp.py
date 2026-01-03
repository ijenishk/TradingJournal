import streamlit as st
import pandas as pd
from datetime import datetime

# Mobile-friendly layout
st.set_page_config(page_title="AlphaLog Mobile", layout="centered")

# --- DATABASE SETUP (Local for now, see Step 2 for permanent) ---
# We will use a CSV file to store trades so it's easier to manage on GitHub
DATA_FILE = "trades.csv"

def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            "Ticker", "Leverage", "Account", "Direction", 
            "Entry", "Exit", "TP1", "TP2", "SL", 
            "Status", "PnL", "Why", "Date"
        ])

st.title("📱 AlphaLog Mobile")

# --- INPUT FORM ---
with st.expander("📝 Log New Trade", expanded=True):
    with st.form("trade_form", clear_on_submit=True):
        ticker = st.text_input("Ticker").upper()
        
        col1, col2 = st.columns(2)
        direction = col1.selectbox("Side", ["Long", "Short"])
        acc_type = col2.selectbox("Account", ["Real", "Demo"])
        
        leverage = st.text_input("Leverage", "10x")
        
        col3, col4 = st.columns(2)
        en = col3.number_input("Entry Price", format="%.5f")
        ex = col4.number_input("Exit Price", format="%.5f")
        
        col5, col6, col7 = st.columns(3)
        tp1_val = col5.number_input("TP 1", format="%.5f")
        tp2_val = col6.number_input("TP 2", format="%.5f")
        sl_val = col7.number_input("SL", format="%.5f")
        
        status = st.selectbox("Result", ["Win", "Loss", "BE", "Open"])
        why = st.text_area("Why?")
        
        submit = st.form_submit_button("💾 Save Trade")

        if submit:
            if ticker:
                # Calculation
                pnl = (ex - en) if direction == "Long" else (en - ex)
                
                # Create row
                new_data = {
                    "Ticker": ticker, "Leverage": leverage, "Account": acc_type,
                    "Direction": direction, "Entry": en, "Exit": ex,
                    "TP1": tp1_val, "TP2": tp2_val, "SL": sl_val,
                    "Status": status, "PnL": round(pnl, 2), "Why": why,
                    "Date": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                
                # Append and Save
                df = load_data()
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                df.to_csv(DATA_FILE, index=False)
                st.success("Trade Logged!")
            else:
                st.error("Please enter a Ticker")

# --- VIEW HISTORY ---
st.markdown("---")
df_display = load_data()
if not df_display.empty:
    st.metric("Total PnL", f"${df_display['PnL'].sum():,.2f}")
    st.subheader("Recent History")
    # Show key info only for mobile view
    st.dataframe(df_display[['Ticker', 'Direction', 'PnL', 'Status']].tail(10), use_container_width=True)
else:
    st.info("No trades logged yet.")
