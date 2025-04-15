import os
import streamlit as st
from streamlit_option_menu import option_menu
from gemini_utility import load_gemini_pro_model
from gemini_utility import gemini_pro_vision_response, gemma_response
# from gemini_utility import generate_image_with_gemini
from PIL import Image

# getting the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# setting up the page configuration
st.set_page_config(
    page_title = "Google Gemini AI",
    layout = "centered"
    # page_icon = ""
)

with st.sidebar:
    selected = option_menu("Gemini AI",
                options=["ChatBot",
                         "Image Detection",
                         # "Embed Text",
                         "Ask me Anything"],
                           menu_icon='robot', icons=["chat-fill", "image-fill",
                                                     "textarea-t", "patch-question-fill"],
                           default_index=0)

# function to translate role between gemini-pro and streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistance"
    else:
        return user_role

# ChatBot page
if selected == "ChatBot":
    model = load_gemini_pro_model()

    # Initialize the chat session in streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # streamlit page title
    st.title("Google ChatBot")
    st.text("What can I help you with ?")

    # display in chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # input field for chat history
    user_prompt = st.chat_input("Ask Gemini Pro...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # display gemini pro response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

# Image Detection Page
if selected == "Image Detection":

    # streamlit title page
    st.title("Image Detection")
    st.text("Upload any Image for Generated Content")

    # upload an image
    uploaded_image = st.file_uploader("Upload an image.....", type=["jpg", "jpeg", "png"])

    # click a button to upload
    if st.button("Generate Content"):
        image = Image.open(uploaded_image)

        col1, col2 = st.columns([2,3])

        # col1 = st.columns(1)

        with col1:
            resized_image = image.resize((600,500))
            st.image(resized_image)

        default_prompt = "Write a caption for this image"

        # getting response from gemini-pro-vision model
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)

# Embed Text Page
# if selected == "Embed Text":
#
#     st.title("Embed Title")
#
#     # Input Text box
#     input_text = st.text_area(label="", placeholder="Enter the text to get the embeddings")
#
#     if st.button("Get Embeddings"):
#         response = embedding_model_response(input_text)
#         st.markdown(response)

# Ask me anything page
if selected == "Ask me Anything":

    # title of the page
    st.title("? Ask me a question")

    # text box to enter a prompt
    user_prompt = st.text_area(label="", placeholder="Ask Gemini Pro")

    if st.button("Get an answer"):
        response = gemma_response(user_prompt)
        st.markdown(response)