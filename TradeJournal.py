import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="AlphaLog Pro", layout="centered")

DATA_FILE = "trades.csv"

def load_data():
    cols = ["Ticker", "Margin", "Leverage", "Account", "Entry Time", "Exit Time", 
            "Duration", "Direction", "Entry Price", "Exit Price", 
            "TP1", "TP2", "SL", "Result", "$$", "Why"]
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=cols)

# --- COLOR LOGIC: RED TEXT FOR LOSS/SHORT, COLORED BOX FOR PNL ---
def style_df(df):
    def color_text_only(val):
        if val in ["Loss", "Short"]: 
            return 'color: #dc3545; font-weight: bold;'
        if val in ["Win", "Long"]: 
            return 'color: #28a745; font-weight: bold;'
        return ''

    def color_pnl_box(val):
        if val < 0: return 'background-color: #f8d7da; color: #721c24;'
        if val > 0: return 'background-color: #d4edda; color: #155724;'
        return ''

    return df.style.applymap(color_text_only, subset=['Result', 'Direction'])\
                   .applymap(color_pnl_box, subset=['$$'])

st.title("📈 AlphaLog Pro")

# --- 1. LOG NEW TRADE ---
with st.expander("📝 Log New Trade", expanded=True):
    with st.form("trade_form", clear_on_submit=True):
        ticker = st.text_input("TICKER").upper()
        
        c1, c2, c3 = st.columns(3)
        margin = c1.number_input("Margin ($)", min_value=0.0, step=1.0)
        lev_val = c2.number_input("Leverage (x)", min_value=1.0, value=10.0, step=1.0)
        account = c3.selectbox("Taken", ["Real", "Demo"])
        
        c4, c5 = st.columns(2)
        entry_time = c4.text_input("Entry Time", value=datetime.now().strftime("%Y-%m-%d %H:%M"))
        exit_time = c5.text_input("Exit Time", value=datetime.now().strftime("%Y-%m-%d %H:%M"))
        
        direction = st.radio("Direction", ["Long", "Short"], horizontal=True)
        
        c6, c7 = st.columns(2)
        en_p = c6.number_input("Entry Price", format="%.5f")
        ex_p = c7.number_input("Exit Price", format="%.5f")
        
        c8, c9, c10 = st.columns(3)
        tp1, tp2, sl = c8.number_input("TP1", format="%.5f"), c9.number_input("TP2", format="%.5f"), c10.number_input("SL", format="%.5f")
        
        result = st.selectbox("Result", ["Win", "Loss", "BE", "Open"])
        why = st.text_area("Why?")
        
        if st.form_submit_button("💾 SAVE TRADE"):
            if en_p > 0:
                # --- LEVERAGED CALCULATION ---
                position_size = margin * lev_val
                price_change_pct = (ex_p - en_p) / en_p if direction == "Long" else (en_p - ex_p) / en_p
                final_pnl = position_size * price_change_pct
                
                try:
                    t1 = datetime.strptime(entry_time, "%Y-%m-%d %H:%M")
                    t2 = datetime.strptime(exit_time, "%Y-%m-%d %H:%M")
                    dur = str(t2 - t1)
                except: dur = "Error"

                new_row = {
                    "Ticker": ticker, "Margin": margin, "Leverage": f"{int(lev_val)}x", "Account": account,
                    "Entry Time": entry_time, "Exit Time": exit_time, "Duration": dur,
                    "Direction": direction, "Entry Price": en_p, "Exit Price": ex_p,
                    "TP1": tp1, "TP2": tp2, "SL": sl, "Result": result, "$$": round(final_pnl, 2), "Why": why
                }
                df = load_data()
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df.to_csv(DATA_FILE, index=False)
                st.success(f"Trade Logged! PnL: ${round(final_pnl, 2)}")
                st.rerun()

# --- 2. VIEW & DELETE ---
st.markdown("---")
df = load_data()

if not df.empty:
    st.metric("Total PnL", f"${df['$$'].sum():,.2f}")
    
    with st.expander("🗑️ Manage / Delete Logs"):
        df['Delete_Label'] = df['Ticker'] + " (" + df['Entry Time'] + ")"
        row_to_delete = st.selectbox("Select Trade to Remove", df['Delete_Label'].tolist())
        if st.button("❌ Permanently Delete"):
            df = df[df['Delete_Label'] != row_to_delete].drop(columns=['Delete_Label'])
            df.to_csv(DATA_FILE, index=False)
            st.rerun()

    st.subheader("Recent History")
    disp_df = df.drop(columns=['Delete_Label'] if 'Delete_Label' in df.columns else [])
    st.dataframe(style_df(disp_df), use_container_width=True)