import streamlit as st
import math

# --- ページ設定 ---
st.set_page_config(page_title="dBm ⇄ dBμV 変換アシスト", layout="centered")

# --- 見た目の設定（CSS） ---
st.markdown("""
    <style>
    /* クレジット表示用のCSS */
    .credit {
        text-align: right;
        font-size: 14px;
        color: #666;
        margin-bottom: -20px;
    }
    /* 入力欄のラベルスタイル */
    .stNumberInput label, .stSelectbox label {
        font-size: 20px !important;
        color: #1E90FF !important; 
        font-weight: 800 !important;
    }
    /* 入力枠の強調 */
    div[data-baseweb="input"] {
        border: 2px solid #1E90FF !important;
        border-radius: 10px;
    }
    /* 計算結果ボックス */
    .result-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #1E90FF;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 右上にクレジットを表示
st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)

st.title('📡 dBm ⇄ dBμV 変換アシスト')
st.caption("※50Ω系・75Ω系のインピーダンス切り替え対応")
st.markdown("---")

# --- 1. インピーダンス設定 ---
col_opt1, col_opt2 = st.columns(2)
with col_opt1:
    impedance = st.selectbox("インピーダンス (Z) を選択", [50, 75], index=0, format_func=lambda x: f"{x} Ω")
with col_opt2:
    mode = st.radio("入力単位を選択", ["dBm を入力", "dBμV を入力"], horizontal=True)

# オフセット値の計算
offset = 120 + 10 * math.log10(impedance / 1000.0)

st.markdown("---")

# --- 2. 入力・計算セクション ---
dbm_val = 0.0
dbuv_val = 0.0

if mode == "dBm を入力":
    dbm_in = st.number_input(f"電力 (dBm)", value=0.0, format="%.2f", step=1.0)
    dbm_val = dbm_in
    dbuv_val = dbm_in + offset
else:
    dbuv_in = st.number_input(f"電圧レベル (dBμV)", value=offset, format="%.2f", step=1.0)
    dbuv_val = dbuv_in
    dbm_val = dbuv_in - offset

# 電力(W)および電圧(V)の計算
mw_val = 10 ** (dbm_val / 10)
w_val = mw_val / 1000.0
v_val = math.sqrt(w_val * impedance)

# --- 3. 結果表示 ---
st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.subheader(f"📊 変換結果 ({impedance}Ω系)")

c1, c2 = st.columns(2)
with c1:
    st.metric("電力 (dBm)", f"{dbm_val:.2f} dBm")
    # 電力をW単位で小数点以下3桁表示
    st.metric("電力 (W)", f"{w_val:.3f} W")
with c2:
    st.metric("電圧レベル (dBμV)", f"{dbuv_val:.2f} dBμV")
    # 電圧をV単位で小数点以下4桁表示
    st.metric("電圧 (V)", f"{v_val:.4f} V")

st.write(f"（参考）電力 (mW): **{mw_val:,.4f} mW**")
st.markdown('</div>', unsafe_allow_html=True)

# 補足情報
with st.expander("ℹ️ 換算式と定数について"):
    st.write(f"""
    インピーダンス **{impedance}Ω** における換算式：
    - **$dB\mu V = dBm + {offset:.1f}$**
    - **$dBm = dB\mu V - {offset:.1f}$**
    
    ※0dBm (1mW) 時の電圧レベル：
    - 50Ω系: 約 107.0 dBμV (0.224 V)
    - 75Ω系: 約 108.8 dBμV (0.274 V)
    """)

# --- 画面下部中央に「戻る」ボタンを配置 ---
st.markdown("---")  # 区切り線
col1, col2, col3 = st.columns([1, 1, 1])

with col2:  # 中央の列を使用
    # 水色のアイコン（🏠）と「戻る」を表示するボタン
    if st.link_button("🏠\n\n戻る", "https://menue3-pkwzfkwnoxnnuljkqg7mdt.streamlit.app/", use_container_width=True):
        pass

# ボタンの色（水色）を調整するカスタム設定
st.markdown("""
    <style>
    div.stLinkButton > a {
        background-color: #00BFFF !important; /* 水色（DeepSkyBlue） */
        color: white !important;
        border-radius: 10px;
        text-align: center;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)
