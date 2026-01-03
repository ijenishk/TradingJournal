import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="AlphaLog Visual", layout="centered")

DATA_FILE = "trades.csv"

def load_data():
    cols = ["Ticker", "Leverage", "Account", "Entry Time", "Exit Time", 
            "Duration", "Direction", "Entry Price", "Exit Price", 
            "TP1", "TP2", "SL", "Result", "$$", "Why"]
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=cols)

# --- COLOR LOGIC FUNCTION ---
def style_df(df):
    def color_result(val):
        if val == "Win": return 'background-color: #d4edda; color: #155724'
        if val == "Loss": return 'background-color: #f8d7da; color: #721c24'
        if val == "BE": return 'background-color: #fff3cd; color: #856404'
        return ''

    def color_pnl(val):
        color = '#d4edda' if val > 0 else '#f8d7da' if val < 0 else 'white'
        return f'background-color: {color}'

    def color_direction(val):
        if val == "Long": return 'color: #28a745; font-weight: bold'
        if val == "Short": return 'color: #dc3545; font-weight: bold'
        return ''

    return df.style.applymap(color_result, subset=['Result'])\
                   .applymap(color_pnl, subset=['$$'])\
                   .applymap(color_direction, subset=['Direction'])

st.title("📈 AlphaLog Visual")

# --- 1. LOG NEW TRADE ---
with st.expander("📝 Log New Trade", expanded=True):
    with st.form("trade_form", clear_on_submit=True):
        ticker = st.text_input("TICKER").upper()
        c1, c2 = st.columns(2)
        leverage = c1.text_input("Leverage", value="10x")
        account = c2.selectbox("Taken", ["Real", "Demo"])
        
        c3, c4 = st.columns(2)
        entry_time = c3.text_input("Entry Time", value=datetime.now().strftime("%Y-%m-%d %H:%M"))
        exit_time = c4.text_input("Exit Time", value=datetime.now().strftime("%Y-%m-%d %H:%M"))
        
        direction = st.radio("Direction", ["Long", "Short"], horizontal=True)
        
        c5, c6 = st.columns(2)
        en_p = c5.number_input("Entry Price", format="%.5f")
        ex_p = c6.number_input("Exit Price", format="%.5f")
        
        c7, c8, c9 = st.columns(3)
        tp1, tp2, sl = c7.number_input("TP1"), c8.number_input("TP2"), c9.number_input("SL")
        
        result = st.selectbox("Result", ["Win", "Loss", "BE", "Open"])
        why = st.text_area("Why?")
        
        if st.form_submit_button("💾 SAVE"):
            pnl = (ex_p - en_p) if direction == "Long" else (en_p - ex_p)
            try:
                t1, t2 = datetime.strptime(entry_time, "%Y-%m-%d %H:%M"), datetime.strptime(exit_time, "%Y-%m-%d %H:%M")
                dur = str(t2 - t1)
            except: dur = "Error"

            new_row = {
                "Ticker": ticker, "Leverage": leverage, "Account": account,
                "Entry Time": entry_time, "Exit Time": exit_time, "Duration": dur,
                "Direction": direction, "Entry Price": en_p, "Exit Price": ex_p,
                "TP1": tp1, "TP2": tp2, "SL": sl, "Result": result, "$$": round(pnl, 2), "Why": why
            }
            df = load_data()
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success("Logged!")
            st.rerun()

# --- 2. VIEW & DELETE LOGS ---
st.markdown("---")
df = load_data()

if not df.empty:
    total_pnl = df['$$'].sum()
    color = "normal" if total_pnl >= 0 else "inverse"
    st.metric("Total PnL", f"${total_pnl:,.2f}", delta=f"{total_pnl:,.2f}", delta_color=color)
    
    with st.expander("🗑️ Manage / Delete Logs"):
        df['Delete_Label'] = df['Ticker'] + " (" + df['Entry Time'] + ")"
        row_to_delete = st.selectbox("Select Trade to Remove", df['Delete_Label'].tolist())
        if st.button("❌ Permanently Delete"):
            df = df[df['Delete_Label'] != row_to_delete].drop(columns=['Delete_Label'])
            df.to_csv(DATA_FILE, index=False)
            st.rerun()

    st.subheader("Recent History")
    # Apply the styling
    styled_df = style_df(df.drop(columns=['Delete_Label'] if 'Delete_Label' in df.columns else []))
    st.dataframe(styled_df, use_container_width=True)