import streamlit as st

# --- 設定（サイドバーなど） ---
with st.sidebar:
    st.title("⚙️ 初期設定")
    # 日報項目やAPIキーの設定

# --- メイン画面 ---
st.title("🎙️ AI日報 & 会議資料アシスタント")

# Step 1: 音声入力
audio_data = st.audio_input("今日の出来事を話してください")

if audio_data:
    # 1. Whisperで文字起こし
    # 2. GPTで日報用データを構造化
    st.session_state['transcript'] = "解析されたテキスト..."
    st.session_state['report_data'] = {"業務内容": "...", "課題": "..."}

# Step 2: 日報表示（データがあれば表示）
if 'report_data' in st.session_state:
    st.divider()
    st.subheader("📝 生成された日報")
    for key, value in st.session_state['report_data'].items():
        st.text_area(key, value)
    
    st.button("日報を提出/保存")

    # Step 3: 会議資料（オプション）
    st.divider()
    make_slides = st.checkbox("💡 この内容から会議資料の「種」を作成しますか？")
    
    if make_slides:
        col1, col2 = st.columns(2)
        with col1:
            tpl = st.selectbox("資料の目的", ["社内提案用", "社内協議用", "社外報告用"])
        with col2:
            tone = st.selectbox("トーン", ["コンサルフォーマル", "社内カジュアル"])
        
        if st.button("資料構成を生成"):
            # ここでテンプレートとトンマナを反映したプロンプトを投げる
            st.markdown("### 📄 スライド構成案（Markdown）")
            st.code("# スライド1: 結論...\n- ポイント1\n- ポイント2", language="markdown")
            st.button("🚀 スライド生成AIへ送る")