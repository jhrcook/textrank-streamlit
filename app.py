from summa import summarizer
import streamlit as st

# Add title on the page
st.title("Text summarization")

# Ask user for input text
input_sent = st.text_area("Input Text", "", height=400)

ratio = st.slider(
    "Summarization fraction", min_value=0.0, max_value=1.0, value=0.2, step=0.01
)

# Display named entities
summarized_text = summarizer.summarize(
    input_sent, ratio=ratio, language="english", split=True, scores=True
)

for sentence, score in summarized_text:
    st.write(sentence)
