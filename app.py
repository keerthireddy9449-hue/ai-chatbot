import streamlit as st
from openai import OpenAI
#============================================
#page configuration
st.set_page_config(
       page_title="Mini ChatGPT - Mistral",
       page_icon="🤖",
       layout="centered")
#=======================================
st.title("🤖 Mini ChatGPT (Mistral AI)")
api_key = ("LyixJ46VyOuuPdWkex2XfGwl5o5tloWp")

if "messages" not in st.session_state:
    st.session_state.messages=[{"role":"system","content":"you are a helpful AI assistant"}]

#show precious messages
for message in st.session_state.messages:
    if message["role"]!="system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
#chat input
prompt = st.chat_input("type your message............")
if prompt:
    if not api_key:
        st.error("please enter API key")
        st.stop()
    client = OpenAI(api_key=api_key,base_url="https://api.mistral.ai/v1")
    #display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("Assistant"):
       with st.spinner("Thinking..."):
           response=client.chat.completions.create(model="mistral-small-latest",messages=st.session_state.messages)
           reply=response.choices[0].message.content
           st.markdown(reply)
    st.session_state.messages.append({"role":"assistant","content":reply})
#========================================================================
#silde bar
with st.sidebar:
    st.header("Options")
    if st.button("Clear Chat"):
       st.session_state.messages=[{"role":"system","content":"you are a helpful AI"}]
       st.rerun()
    st.markdown("---")
    st.write("**Model:** mistral-small-latest")
   