import streamlit as st 
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

MODEL="text-davinci-003"

st.title("Travel Helper")
st.subheader("A Language Guide")

input_phrase=st.text_area("What do you want to say?")

language=st.selectbox("Select Language", ["Spanish", "French", \
    "Italian", "Chinese", "Japonese", "Custom"])

if language=="Custom":
    language=st.text_input("Input Language")

if st.button("Submit"):
    prompt="Translate the following statement into the {} langauge. \
            Add two additional options in the input language with English translations. \
            Add two common responses in the input with English translations. \
            Add short paragraph in English explaining the translation, to aid in understanding. \
            Statement: {}".format(language, input_phrase)

    response=openai.Completion.create(
        model=MODEL,
        prompt=prompt,
        max_tokens=1000,
        temperature=0,
        stream=True
    )

    with st.empty():
        collected_events = []
        completion_text = ''
        for event in response:
            collected_events.append(event)
            event_text = event['choices'][0]['text']
            completion_text += event_text
            st.write(completion_text)
