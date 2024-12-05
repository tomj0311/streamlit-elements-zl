import streamlit as st
import websocket
import threading
import queue
import time

# Thread-safe queue for WebSocket messages
message_queue = queue.Queue()

# WebSocket message handler
def on_message(ws, message):
    message_queue.put(("message", message))

def on_error(ws, error):
    message_queue.put(("error", f"WebSocket error: {error}"))

def on_close(ws, close_status_code, close_msg):
    message_queue.put(("close", "WebSocket connection closed."))

def on_open(ws):
    message_queue.put(("open", "WebSocket connection established."))

# Start WebSocket connection in a separate thread
def start_websocket(url):
    ws = websocket.WebSocketApp(
        url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open
    thread = threading.Thread(target=ws.run_forever, daemon=True)
    thread.start()
    return ws

# Streamlit UI
st.title("WebSocket Client in Streamlit")

# Initialize session state variables
if "connected" not in st.session_state:
    st.session_state.connected = False
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input for WebSocket URL
url = st.text_input("WebSocket URL", value="ws://localhost:8000/ws")

# Button to connect to WebSocket
if st.button("Connect to WebSocket") and not st.session_state.connected:
    st.session_state.ws = start_websocket(url)
    st.session_state.connected = True

# Button to send a message
if st.session_state.connected:
    message = st.text_input("Message to Send")
    if st.button("Send Message") and message:
        st.session_state.ws.send(message)

# Continuously poll the queue for new messages
while True:
    while not message_queue.empty():
        msg_type, content = message_queue.get()
        if msg_type == "message":
            st.session_state.messages.append(content)
        elif msg_type == "error":
            st.error(content)
        elif msg_type == "close":
            st.session_state.connected = False
            st.info(content)
        elif msg_type == "open":
            st.success(content)
    time.sleep(0.1)

# Display messages dynamically
if st.session_state.messages:
    st.write("Messages received:")
    st.write("\n".join(st.session_state.messages))

# Continuously poll the queue for new messages
while True:
    while not message_queue.empty():
        msg_type, content = message_queue.get()
        print(msg_type)
        if msg_type == "message":
            st.session_state.messages.append(content)
            print(content)
        elif msg_type == "error":
            st.error(content)
        elif msg_type == "close":
            st.session_state.connected = False
            st.info(content)
        elif msg_type == "open":
            st.success(content)
    time.sleep(0.1)
