import streamlit as st
import streamlit.components.v1 as components

# Define the custom component
def custom_iframe():
    component = components.declare_component(
        "custom_component", path="./newfe"  # Path to the frontend folder
    )
    return component()

# Use the component and display the message
st.title("Service Worker Message Listener")
message = custom_iframe()

if message:
    st.write("Message from service worker:", message)

st.write("Application started")
