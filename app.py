import streamlit as st

# --- 1. アプリ全体のセッション状態の初期化 ---
if 'daily_report_fields' not in st.session_state:
    # デフォルトの項目を設定
    st.session_state['daily_report_fields'] = ["業務内容", "成果と課題", "明日の予定"]

# --- 2. サイドバー：初期設定セクション ---
with st.sidebar:
    st.title("⚙️ アプリ初期設定")
    
    st.subheader("1. 日報の項目設定")
    # カンマ区切りで入力を受け取り、リストに変換
    fields_input = st.text_area(
        "必要な項目をカンマで区切って入力してください",
        value=",".join(st.session_state['daily_report_fields'])
    )
    if st.button("項目を更新"):
        st.session_state['daily_report_fields'] = [f.strip() for f in fields_input.split(",")]
        st.success("項目を更新しました！")

    st.divider()
    
    st.subheader("2. API設定")
    openai_key = st.text_input("OpenAI API Key", type="password")
    if openai_key:
        st.info("APIキーが入力されました。解析が可能です。")

# --- 3. メイン画面：入力と出力 ---
st.title("🎙️ AI日報 & 会議資料作成")

# 音声入力（録音）
audio_data = st.audio_input("今日一日の出来事を自由に話してください")

if audio_data and openai_key:
    # 【ここにWhisperとGPTの処理が入る】
    # AIへのプロンプトに st.session_state['daily_report_fields'] を渡すことで、
    # ユーザーが指定した通りの項目で回答を生成させます。
    
    st.success("解析が完了しました！")
    
    # ユーザーが設定した項目に基づいて、動的に入力エリアを作成
    st.subheader("📝 生成された日報（修正可能）")
    for field in st.session_state['daily_report_fields']:
        # AIからの回答をここに入れる（現在は仮の文字）
        st.text_area(field, value=f"{field}に関するAIの推論結果...", height=100)

    # スライド作成オプション（前述の通り）
    # ...
