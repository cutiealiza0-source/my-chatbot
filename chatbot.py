import streamlit as st
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))# Page config
st.set_page_config(
    page_title="ZaraBot - AI Marketing Expert",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .stButton > button {
        background: linear-gradient(135deg, #7F77DD, #534AB7);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #534AB7, #7F77DD);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(127,119,221,0.4);
    }

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style='text-align:center; padding:20px;'>
    <h1 style='color:#7F77DD; font-size:2.5em;'>🤖 ZaraBot</h1>
    <p style='color:#9FE1CB; font-size:1.1em;'>AI Marketing Expert — Powered by Groq</p>
    <hr style='border-color:#7F77DD; opacity:0.3;'>
</div>
""", unsafe_allow_html=True)

# Quick buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("✍️ Write Ad"):
        st.session_state.quick = "Write a Facebook ad for my business"
with col2:
    if st.button("🎯 Find Leads"):
        st.session_state.quick = "Help me find leads for my business"
with col3:
    if st.button("📊 Analyze"):
        st.session_state.quick = "Analyze my marketing campaign"

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
prompt = st.chat_input("Ask ZaraBot anything...")

if "quick" in st.session_state:
    prompt = st.session_state.quick
    del st.session_state.quick

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are ZaraBot, a professional AI marketing expert. Help with ads, leads, campaigns and content."},
            {"role": "user", "content": prompt}
        ]
    )
    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)