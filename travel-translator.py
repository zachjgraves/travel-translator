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
    prompt="Act as a helpful translation assistant.\
            Format response in markdown headers H2.\
            Translate the following statement into {}. \
            Add two additional options with translations. \
            Add two common responses with translations. \
            Add short paragraph adding context about the \
            translation, to aid in understanding. \
            Example input: 'Can I buy a coffee?'\n\
            Example output: \n\
            Translation: ¿Puedo comprar un café? \n\
            Or try: ¿Puedo obtener un café? - Can I get a coffee? \n\
            Another Option: ¿Puedo tomar un café? - Can I have a coffee? \n\
            Common Responses: Sí, por supuesto. - Yes, of course. \n\
            Common Response 2: Lo siento, estamos cerrados. - Sorry, we're closed. \n\
            Statement: {}".format(language, input_phrase)

    response=openai.Completion.create(
        model=MODEL,
        prompt=prompt,
        max_tokens=2000,
        temperature=0.3,
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
