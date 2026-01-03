{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "55f5787c-a1ac-4163-bed9-d25c77515f05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing app.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile app.py \n",
    "import pandas as pd\n",
    "import ipywidgets as widgets\n",
    "from IPython.display import display, clear_output\n",
    "from datetime import datetime\n",
    "\n",
    "# Data storage (In-memory for this session, can be saved to CSV)\n",
    "trades_df = pd.DataFrame(columns=[\n",
    "    'Ticker', 'Entry Time', 'Exit Time', 'Entry', 'Exit', 'Status', 'PnL', 'Why'\n",
    "])\n",
    "\n",
    "# UI Elements\n",
    "ticker_input = widgets.Text(description='Ticker:')\n",
    "entry_p = widgets.FloatText(description='Entry Price:')\n",
    "exit_p = widgets.FloatText(description='Exit Price:')\n",
    "status_input = widgets.Dropdown(options=['Win', 'Loss', 'Break-even'], description='Status:')\n",
    "reason_input = widgets.Textarea(description='Why:')\n",
    "btn = widgets.Button(description='Log Trade', button_style='success')\n",
    "output = widgets.Output()\n",
    "\n",
    "def log_trade(b):\n",
    "    global trades_df\n",
    "    pnl = exit_p.value - entry_p.value\n",
    "    new_trade = {\n",
    "        'Ticker': ticker_input.value.upper(),\n",
    "        'Entry Time': datetime.now().strftime(\"%Y-%m-%d %H:%M\"),\n",
    "        'Entry': entry_p.value,\n",
    "        'Exit': exit_p.value,\n",
    "        'Status': status_input.value,\n",
    "        'PnL': pnl,\n",
    "        'Why': reason_input.value\n",
    "    }\n",
    "    trades_df = pd.concat([trades_df, pd.DataFrame([new_trade])], ignore_index=True)\n",
    "    with output:\n",
    "        clear_output()\n",
    "        display(trades_df)\n",
    "\n",
    "btn.on_click(log_trade)\n",
    "\n",
    "# Layout\n",
    "display(widgets.VBox([ticker_input, entry_p, exit_p, status_input, reason_input, btn]), output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61b33a3c-c289-4e4d-99e3-d6e5b874c024",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fd8b149-e3df-4251-b406-b40211cd6715",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "264f3995-4ce3-49c0-9658-75cf1014064b",
   "metadata": {},
   "outputs": [
    {
     "ename": "UnicodeEncodeError",
     "evalue": "'charmap' codec can't encode character '\\U0001f4c8' in position 494: character maps to <undefined>",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnicodeEncodeError\u001b[0m                        Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# 1. Write the code to a file\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtrade_journal.py\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mw\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[1;32m----> 3\u001b[0m     f\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\"\"\u001b[39m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;124mimport streamlit as st\u001b[39m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;124mimport pandas as pd\u001b[39m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;124mimport sqlite3\u001b[39m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;124mfrom datetime import datetime\u001b[39m\n\u001b[0;32m      8\u001b[0m \n\u001b[0;32m      9\u001b[0m \u001b[38;5;124m# Database Logic\u001b[39m\n\u001b[0;32m     10\u001b[0m \u001b[38;5;124mdef init_db():\u001b[39m\n\u001b[0;32m     11\u001b[0m \u001b[38;5;124m    conn = sqlite3.connect(\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtrade_journal.db\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     12\u001b[0m \u001b[38;5;124m    c = conn.cursor()\u001b[39m\n\u001b[0;32m     13\u001b[0m \u001b[38;5;124m    c.execute(\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mCREATE TABLE IF NOT EXISTS trades\u001b[39m\n\u001b[0;32m     14\u001b[0m \u001b[38;5;124m                 (ticker TEXT, entry_time TEXT, exit_time TEXT,\u001b[39m\n\u001b[0;32m     15\u001b[0m \u001b[38;5;124m                  entry_price REAL, exit_price REAL, \u001b[39m\n\u001b[0;32m     16\u001b[0m \u001b[38;5;124m                  status TEXT, pnl REAL, reason TEXT)\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     17\u001b[0m \u001b[38;5;124m    conn.commit()\u001b[39m\n\u001b[0;32m     18\u001b[0m \u001b[38;5;124m    conn.close()\u001b[39m\n\u001b[0;32m     19\u001b[0m \n\u001b[0;32m     20\u001b[0m \u001b[38;5;124minit_db()\u001b[39m\n\u001b[0;32m     21\u001b[0m \n\u001b[0;32m     22\u001b[0m \u001b[38;5;124mst.title(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m📈 Trader\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124ms Command Center\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     23\u001b[0m \n\u001b[0;32m     24\u001b[0m \u001b[38;5;124m# Sidebar Input\u001b[39m\n\u001b[0;32m     25\u001b[0m \u001b[38;5;124mwith st.sidebar:\u001b[39m\n\u001b[0;32m     26\u001b[0m \u001b[38;5;124m    st.header(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLog Trade\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     27\u001b[0m \u001b[38;5;124m    t = st.text_input(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTicker\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     28\u001b[0m \u001b[38;5;124m    en_p = st.number_input(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEntry Price\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     29\u001b[0m \u001b[38;5;124m    ex_p = st.number_input(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mExit Price\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     30\u001b[0m \u001b[38;5;124m    stat = st.selectbox(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mResult\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m, [\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWin\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m, \u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLoss\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m, \u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mBreak-even\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m])\u001b[39m\n\u001b[0;32m     31\u001b[0m \u001b[38;5;124m    res = st.text_area(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWhy?\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     32\u001b[0m \u001b[38;5;124m    if st.button(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSave\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m):\u001b[39m\n\u001b[0;32m     33\u001b[0m \u001b[38;5;124m        conn = sqlite3.connect(\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtrade_journal.db\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     34\u001b[0m \u001b[38;5;124m        c = conn.cursor()\u001b[39m\n\u001b[0;32m     35\u001b[0m \u001b[38;5;124m        c.execute(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mINSERT INTO trades VALUES (?,?,?,?,?,?,?,?)\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m, \u001b[39m\n\u001b[0;32m     36\u001b[0m \u001b[38;5;124m                  (t, str(datetime.now()), str(datetime.now()), en_p, ex_p, stat, ex_p-en_p, res))\u001b[39m\n\u001b[0;32m     37\u001b[0m \u001b[38;5;124m        conn.commit()\u001b[39m\n\u001b[0;32m     38\u001b[0m \u001b[38;5;124m        conn.close()\u001b[39m\n\u001b[0;32m     39\u001b[0m \u001b[38;5;124m        st.success(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrade Logged!\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     40\u001b[0m \n\u001b[0;32m     41\u001b[0m \u001b[38;5;124m# Display Data\u001b[39m\n\u001b[0;32m     42\u001b[0m \u001b[38;5;124mconn = sqlite3.connect(\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtrade_journal.db\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m)\u001b[39m\n\u001b[0;32m     43\u001b[0m \u001b[38;5;124mdf = pd.read_sql_query(\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSELECT * FROM trades\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m, conn)\u001b[39m\n\u001b[0;32m     44\u001b[0m \u001b[38;5;124mst.dataframe(df)\u001b[39m\n\u001b[0;32m     45\u001b[0m \u001b[38;5;124m    \u001b[39m\u001b[38;5;124m\"\"\"\u001b[39m)\n\u001b[0;32m     47\u001b[0m \u001b[38;5;66;03m# 2. Run the terminal command FROM the notebook\u001b[39;00m\n\u001b[0;32m     48\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01msubprocess\u001b[39;00m\n",
      "File \u001b[1;32mD:\\Anaconda\\Lib\\encodings\\cp1252.py:19\u001b[0m, in \u001b[0;36mIncrementalEncoder.encode\u001b[1;34m(self, input, final)\u001b[0m\n\u001b[0;32m     18\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mencode\u001b[39m(\u001b[38;5;28mself\u001b[39m, \u001b[38;5;28minput\u001b[39m, final\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m):\n\u001b[1;32m---> 19\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m codecs\u001b[38;5;241m.\u001b[39mcharmap_encode(\u001b[38;5;28minput\u001b[39m,\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39merrors,encoding_table)[\u001b[38;5;241m0\u001b[39m]\n",
      "\u001b[1;31mUnicodeEncodeError\u001b[0m: 'charmap' codec can't encode character '\\U0001f4c8' in position 494: character maps to <undefined>"
     ]
    }
   ],
   "source": [
    "# 1. Write the code to a file\n",
    "with open(\"trade_journal.py\", \"w\") as f:\n",
    "    f.write(\"\"\"\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import sqlite3\n",
    "from datetime import datetime\n",
    "\n",
    "# Database Logic\n",
    "def init_db():\n",
    "    conn = sqlite3.connect('trade_journal.db')\n",
    "    c = conn.cursor()\n",
    "    c.execute('''CREATE TABLE IF NOT EXISTS trades\n",
    "                 (ticker TEXT, entry_time TEXT, exit_time TEXT,\n",
    "                  entry_price REAL, exit_price REAL, \n",
    "                  status TEXT, pnl REAL, reason TEXT)''')\n",
    "    conn.commit()\n",
    "    conn.close()\n",
    "\n",
    "init_db()\n",
    "\n",
    "st.title(\"📈 Trader's Command Center\")\n",
    "\n",
    "# Sidebar Input\n",
    "with st.sidebar:\n",
    "    st.header(\"Log Trade\")\n",
    "    t = st.text_input(\"Ticker\")\n",
    "    en_p = st.number_input(\"Entry Price\")\n",
    "    ex_p = st.number_input(\"Exit Price\")\n",
    "    stat = st.selectbox(\"Result\", [\"Win\", \"Loss\", \"Break-even\"])\n",
    "    res = st.text_area(\"Why?\")\n",
    "    if st.button(\"Save\"):\n",
    "        conn = sqlite3.connect('trade_journal.db')\n",
    "        c = conn.cursor()\n",
    "        c.execute(\"INSERT INTO trades VALUES (?,?,?,?,?,?,?,?)\", \n",
    "                  (t, str(datetime.now()), str(datetime.now()), en_p, ex_p, stat, ex_p-en_p, res))\n",
    "        conn.commit()\n",
    "        conn.close()\n",
    "        st.success(\"Trade Logged!\")\n",
    "\n",
    "# Display Data\n",
    "conn = sqlite3.connect('trade_journal.db')\n",
    "df = pd.read_sql_query(\"SELECT * FROM trades\", conn)\n",
    "st.dataframe(df)\n",
    "    \"\"\")\n",
    "\n",
    "# 2. Run the terminal command FROM the notebook\n",
    "import subprocess\n",
    "import sys\n",
    "\n",
    "# This command opens the terminal process for you\n",
    "subprocess.Popen([sys.executable, \"-m\", \"streamlit\", \"run\", \"trade_journal.py\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9e49f882-1542-4684-8abc-7e44a0f5d924",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Attempting to launch Streamlit...\n",
      "If a browser didn't open, go to: http://localhost:8501\n"
     ]
    }
   ],
   "source": [
    "# 1. Write the code to a file WITH UTF-8 ENCODING\n",
    "with open(\"trade_journal.py\", \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(\"\"\"\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import sqlite3\n",
    "from datetime import datetime\n",
    "\n",
    "# Database Logic\n",
    "def init_db():\n",
    "    conn = sqlite3.connect('trade_journal.db')\n",
    "    c = conn.cursor()\n",
    "    c.execute('''CREATE TABLE IF NOT EXISTS trades\n",
    "                 (ticker TEXT, entry_time TEXT, exit_time TEXT,\n",
    "                  entry_price REAL, exit_price REAL, \n",
    "                  status TEXT, pnl REAL, reason TEXT)''')\n",
    "    conn.commit()\n",
    "    conn.close()\n",
    "\n",
    "init_db()\n",
    "\n",
    "st.title(\"📈 Trader's Command Center\")\n",
    "\n",
    "# Sidebar Input\n",
    "with st.sidebar:\n",
    "    st.header(\"Log Trade\")\n",
    "    t = st.text_input(\"Ticker\")\n",
    "    en_p = st.number_input(\"Entry Price\", format=\"%.2f\")\n",
    "    ex_p = st.number_input(\"Exit Price\", format=\"%.2f\")\n",
    "    stat = st.selectbox(\"Result\", [\"Win\", \"Loss\", \"Break-even\"])\n",
    "    res = st.text_area(\"Why was this trade taken?\")\n",
    "    \n",
    "    if st.button(\"Save Trade\"):\n",
    "        if t:\n",
    "            conn = sqlite3.connect('trade_journal.db')\n",
    "            c = conn.cursor()\n",
    "            c.execute(\"INSERT INTO trades (ticker, entry_time, exit_time, entry_price, exit_price, status, pnl, reason) VALUES (?,?,?,?,?,?,?,?)\", \n",
    "                      (t, str(datetime.now()), str(datetime.now()), en_p, ex_p, stat, ex_p-en_p, res))\n",
    "            conn.commit()\n",
    "            conn.close()\n",
    "            st.success(\"Trade Logged Successfully!\")\n",
    "        else:\n",
    "            st.error(\"Please enter a Ticker symbol.\")\n",
    "\n",
    "# Display Data & Analytics\n",
    "conn = sqlite3.connect('trade_journal.db')\n",
    "df = pd.read_sql_query(\"SELECT * FROM trades\", conn)\n",
    "conn.close()\n",
    "\n",
    "if not df.empty:\n",
    "    st.subheader(\"Your Performance\")\n",
    "    st.dataframe(df, use_container_width=True)\n",
    "    \n",
    "    # Simple Equity Curve\n",
    "    df['Cumulative PnL'] = df['pnl'].cumsum()\n",
    "    st.line_chart(df['Cumulative PnL'])\n",
    "else:\n",
    "    st.info(\"No trades found. Add your first trade in the sidebar!\")\n",
    "    \"\"\")\n",
    "\n",
    "# 2. Launch the app\n",
    "import subprocess\n",
    "import sys\n",
    "import time\n",
    "\n",
    "print(\"Attempting to launch Streamlit...\")\n",
    "process = subprocess.Popen([sys.executable, \"-m\", \"streamlit\", \"run\", \"trade_journal.py\"])\n",
    "time.sleep(2)\n",
    "print(\"If a browser didn't open, go to: http://localhost:8501\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3397c80f-dc03-4f50-8c7b-11cdbab4ad7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Starting the server using: D:\\Anaconda\\python.exe\n",
      "\n",
      "✅ SUCCESS!\n",
      "Go to this link in your browser: http://localhost:8501\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "import subprocess\n",
    "\n",
    "# This tells Python to use its own 'hidden' path to run Streamlit\n",
    "executable = sys.executable\n",
    "cmd = [executable, \"-m\", \"streamlit\", \"run\", \"trade_journal.py\"]\n",
    "\n",
    "print(f\"Starting the server using: {executable}\")\n",
    "process = subprocess.Popen(cmd)\n",
    "\n",
    "print(\"\\n✅ SUCCESS!\")\n",
    "print(\"Go to this link in your browser: http://localhost:8501\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f47fc341-0ecb-47cd-909b-90b96b51fd68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: streamlit in d:\\anaconda\\lib\\site-packages (1.45.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.5.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (5.5.1)\n",
      "Requirement already satisfied: click<9,>=7.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (8.1.8)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in d:\\anaconda\\lib\\site-packages (from streamlit) (2.1.3)\n",
      "Requirement already satisfied: packaging<25,>=20 in d:\\anaconda\\lib\\site-packages (from streamlit) (24.2)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (2.2.3)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (11.1.0)\n",
      "Requirement already satisfied: protobuf<7,>=3.20 in d:\\anaconda\\lib\\site-packages (from streamlit) (5.29.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (19.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in d:\\anaconda\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (9.0.0)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in d:\\anaconda\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in d:\\anaconda\\lib\\site-packages (from streamlit) (4.0.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in d:\\anaconda\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in d:\\anaconda\\lib\\site-packages (from streamlit) (6.5.1)\n",
      "Requirement already satisfied: jinja2 in d:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.6)\n",
      "Requirement already satisfied: jsonschema>=3.0 in d:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in d:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.31.0)\n",
      "Requirement already satisfied: colorama in d:\\anaconda\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in d:\\anaconda\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in d:\\anaconda\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in d:\\anaconda\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in d:\\anaconda\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in d:\\anaconda\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in d:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in d:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in d:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in d:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2025.4.26)\n",
      "Requirement already satisfied: attrs>=22.2.0 in d:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.3.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in d:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in d:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in d:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
      "Requirement already satisfied: six>=1.5 in d:\\anaconda\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in d:\\anaconda\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2f397c16-e4f2-489d-afc9-d8af422a3f08",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (906672099.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[7], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    hello streamlit\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "hello streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4ef3b823-74b9-40dd-a9d8-57692765c9c2",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3031887691.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[8], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit hello\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit hello\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "745fe69d-3e8b-41a6-8ed6-1c60162e713c",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
