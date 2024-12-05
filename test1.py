from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import streamlit as st
import uvicorn
import threading
import queue
import time

# Define the ObservableQueue
class ObservableQueue(queue.Queue):
    def __init__(self, *args, on_change=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_change = on_change  # Callback to notify changes

    def put(self, item, *args, **kwargs):
        super().put(item, *args, **kwargs)
        if self.on_change:
            self.on_change("put", item)

    def get(self, *args, **kwargs):
        item = super().get(*args, **kwargs)
        if self.on_change:
            self.on_change("get", item)
        return item

# Callback to handle queue changes
def queue_change_listener(action, item):
    if action == "put":
        if "received_data" not in st.session_state:
            st.session_state["received_data"] = []
        st.session_state["received_data"].append(item)

# Create an ObservableQueue with the listener
message_queue = ObservableQueue(on_change=queue_change_listener)

# Create FastAPI app
api_app = FastAPI()

# List to store WebSocket connections
websocket_connections = []

# FastAPI WebSocket route
@api_app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_connections.append(websocket)
    try:
        while True:
            # Receive data from WebSocket
            data = await websocket.receive_text()
            message_queue.put(data)  # Add data to the ObservableQueue
            # Broadcast the received data to all connected WebSocket clients
            for connection in websocket_connections:
                await connection.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        print("WebSocket connection closed")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        websocket_connections.remove(websocket)

# Start FastAPI app with Uvicorn
def start_api():
    def run():
        uvicorn.run(api_app, host="0.0.0.0", port=8000)
    thread = threading.Thread(target=run, daemon=True)
    thread.start()

start_api()

# Streamlit UI
st.title("Streamlit with FastAPI")
st.write("Connect to WebSocket at `/ws` on port 8000.")

# Initialize session state
if "received_data" not in st.session_state:
    st.session_state["received_data"] = []

# Periodic polling to check the queue
def poll_queue():
    while not message_queue.empty():
        msg = message_queue.get()
        st.session_state["received_data"].append(msg)

# Poll the queue and update the UI
poll_queue()

# Display received messages
if st.session_state["received_data"]:
    st.write("Chat Messages:")
    for msg in st.session_state["received_data"]:
        st.write(msg)
else:
    st.write("Waiting for messages...")
