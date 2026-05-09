import streamlit as st
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.set_page_config(
    page_title="ZaraBot",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #0d0d0d; color: #ececec; }
    [data-testid="stSidebar"] { background-color: #111111; border-right: 1px solid #222; }
    .stButton > button {
        background: linear-gradient(135deg, #7F77DD, #534AB7);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 16px;
        font-size: 13px;
        font-weight: 600;
        width: 100%;
        margin: 3px 0;
        transition: all 0.2s;
        text-align: left;
    }
    .stButton > button:hover {
        transform: translateX(5px);
        box-shadow: 0 5px 20px rgba(127,119,221,0.4);
    }
    [data-testid="stChatInput"] textarea {
    background-color: #1a1a1a !important;
    color: white !important;
    border-radius: 16px !important;
    border: 1px solid #7F77DD !important;
}
section[data-testid="stBottom"] {
    background-color: #0d0d0d !important;
    border-top: 1px solid #222 !important;
    padding: 10px 20px !important;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding:25px 0 15px;'>
        <div style='
            width:75px; height:75px; margin:0 auto;
            background: linear-gradient(135deg, #7F77DD, #9B59B6);
            border-radius:22px;
            display:flex; align-items:center; justify-content:center;
            box-shadow: 0 8px 25px rgba(127,119,221,0.6);
            font-size:38px; line-height:75px; text-align:center;
        '>⚡</div>
        <h2 style='color:white; margin:12px 0 2px; font-size:1.4em; font-weight:800; letter-spacing:2px;'>ZARABOT</h2>
        <p style='color:#7F77DD; font-size:10px; letter-spacing:3px; text-transform:uppercase; margin:0;'>AI MARKETING EXPERT</p>
    </div>
    <hr style='border-color:#222; margin:10px 0 20px;'>
    """, unsafe_allow_html=True)

    st.markdown("<p style='color:#888; font-size:11px; letter-spacing:2px; text-transform:uppercase; margin-bottom:10px;'>⚡ Quick Actions</p>", unsafe_allow_html=True)

    if st.button("✍️  Write Facebook Ad"):
        st.session_state.quick = "Write a professional Facebook ad for my business"
    if st.button("🎯  Find Leads"):
        st.session_state.quick = "Help me find 5 potential leads for my business"
    if st.button("📊  Analyze Campaign"):
        st.session_state.quick = "Analyze my marketing campaign and give improvement tips"
    if st.button("📧  Write Email"):
        st.session_state.quick = "Write a professional marketing email for my business"
    if st.button("📱  Instagram Caption"):
        st.session_state.quick = "Write 5 engaging Instagram captions for my business"
    if st.button("💰  Sales Script"):
        st.session_state.quick = "Write a sales script to convince customers to buy my product"
    if st.button("🔍  SEO Keywords"):
        st.session_state.quick = "Give me 10 best SEO keywords for my marketing business"

    st.markdown("<hr style='border-color:#222; margin:20px 0 10px;'>", unsafe_allow_html=True)
    if st.button("🗑️  Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# MAIN AREA
if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    st.markdown("""
    <div style='text-align:center; padding:80px 0 40px;'>
        <div style='
            width:100px; height:100px; margin:0 auto 20px;
            background: linear-gradient(135deg, #7F77DD, #9B59B6);
            border-radius:28px;
            box-shadow: 0 15px 40px rgba(127,119,221,0.5);
            font-size:50px; line-height:100px; text-align:center;
        '>⚡</div>
        <h1 style='color:white; font-size:2.5em; font-weight:800; letter-spacing:3px; margin:0 0 10px;'>ZARABOT</h1>
        <p style='color:#666; font-size:15px; letter-spacing:1px;'>Your Personal AI Marketing Expert</p>
        <div style='display:flex; gap:10px; justify-content:center; margin-top:30px; flex-wrap:wrap;'>
            <span style='background:#1a1a1a; border:1px solid #333; padding:8px 16px; border-radius:20px; color:#888; font-size:12px;'>✍️ Write Ads</span>
            <span style='background:#1a1a1a; border:1px solid #333; padding:8px 16px; border-radius:20px; color:#888; font-size:12px;'>🎯 Find Leads</span>
            <span style='background:#1a1a1a; border:1px solid #333; padding:8px 16px; border-radius:20px; color:#888; font-size:12px;'>📊 Analyze Campaigns</span>
            <span style='background:#1a1a1a; border:1px solid #333; padding:8px 16px; border-radius:20px; color:#888; font-size:12px;'>📧 Write Emails</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Message ZaraBot...")

if "quick" in st.session_state:
    prompt = st.session_state.quick
    del st.session_state.quick

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner(""):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are ZaraBot, a world-class AI marketing expert. Help with ads, leads, campaigns, emails, social media and sales. Be professional, detailed and helpful."},
                ] + st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
