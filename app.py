
import streamlit as st
import math

# --- 見た目の設定（CSS） ---
st.markdown("""
    <style>
    /* 入力欄のラベル（dBmを入力してください）を大きく、太く、青くする */
    .stNumberInput label {
        font-size: 32px !important; /* さらに大きくしました */
        color: #1E90FF !important;
        font-weight: 800 !important; /* より太くしました */
        line-height: 1.5;
    }
    /* 入力枠内の数字そのものを大きくする */
    div[data-baseweb="input"] {
        height: 60px !important; /* 枠自体を少し高くしました */
        font-size: 28px !important;
        border: 3px solid #1E90FF !important; /* 枠線を少し太くしました */
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('📡 デシベル計算アプリ')
st.markdown("---")

# 入力
dbm_in = st.number_input("dBmを入力してください", value=33.0)

# 計算
mw_val = 10 ** (dbm_in / 10)
w_val = mw_val / 1000
v_val = math.sqrt(mw_val * 50 / 1000)
dbuv_50 = 20 * math.log10(v_val * 10**6)

# 表示
st.subheader("変換結果")
c1, c2 = st.columns(2)
with c1:
    st.metric("電力 (mW)", f"{mw_val:,.2f}")
    st.metric("電力 (W)", f"{w_val:,.4f}")
with c2:
    st.metric("電圧 (V)", f"{v_val:,.4f}")
    st.metric("dBμV (50Ω)", f"{dbuv_50:.2f}")
