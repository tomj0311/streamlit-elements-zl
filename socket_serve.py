# Create FastAPI app
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn


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
            print(data)
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
if __name__ == "__main__":
    uvicorn.run(api_app, host="0.0.0.0", port=8000)