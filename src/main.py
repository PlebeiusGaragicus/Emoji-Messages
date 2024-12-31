import os
import pathlib
from PIL import Image

import streamlit as st

from src.common import (
    cprint,
    Colors,
)


APP_NAME = "Template"
STATIC_PATH = pathlib.Path(__file__).parent.parent / "static"



def cmp_header():
    favicon = Image.open(os.path.join(STATIC_PATH, "favicon.ico"))
    st.set_page_config(
        # page_title="DEBUG!" if os.getenv("DEBUG", False) else "NOS4A2",
        page_title=APP_NAME,
        page_icon=favicon,
        layout="wide",
        initial_sidebar_state="auto",
    )

    # column_fix()
    # center_text("p", "🗣️🤖💬", size=60) # or h1, whichever
    # st.sidebar.header("", divider="rainbow")



def log_rerun():
    ip_addr = st.context.headers.get('X-Forwarded-For', "?")
    user_agent = st.context.headers.get('User-Agent', "?")
    lang = st.context.headers.get('Accept-Language', "?")

    # print(f"RUNNING for IP address: {ip_addr}")
    cprint(f"RUNNING for: {ip_addr} - {lang} - {user_agent}", Colors.YELLOW)






# Define a mapping from ASCII characters to emojis
emoji_mapping = {
    'a': '😀', 'b': '😁', 'c': '😂', 'd': '🤣', 'e': '😃', 
    'f': '😄', 'g': '😅', 'h': '😆', 'i': '😉', 'j': '😊',
    'k': '😋', 'l': '😎', 'm': '😍', 'n': '😘', 'o': '😗',
    'p': '😙', 'q': '😚', 'r': '😇', 's': '🙂', 't': '🙃',
    'u': '☹️', 'v': '😡', 'w': '😠', 'x': '😶', 'y': '😐', 
    'z': '😑', ' ': ' ', '.': '✨', ',': '🌈', '!': '🎉', '?': '❓'
}

def convert_to_emoji(text):
    """Convert the given text to emoji using the defined mapping."""
    result = []
    for char in text.lower():
        if char in emoji_mapping:
            result.append(emoji_mapping[char])
        else:
            result.append(char)  # Keep original character if no mapping found
    return ''.join(result)






def main_page():
    log_rerun()

    cmp_header()

    st.write("hi")

    if os.getenv("DEBUG"):
        with st.sidebar:
            st.write(":orange[DEBUG]")
            st.write( st.context.cookies )
            st.write( st.context.headers )





    st.title("ASCII to Emoji Converter")
    st.write("Enter text to convert to emojis:")


    input_text = st.text_area("Input text", height=200)

    if st.button("Convert"):
        emoji_text = convert_to_emoji(input_text)
        st.subheader("Converted to emoji:")
        st.write(emoji_text)
