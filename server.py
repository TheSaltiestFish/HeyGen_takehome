from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import random

app = FastAPI()

task_status = "pending"

# WebSocket connection
active_websocket = None

async def update_task_status():
    """simulate task processing and status update"""
    global task_status, active_websocket
    await asyncio.sleep(random.randint(5, 10))  # update statues after some time
    task_status = random.choice(["completed", "error"])

    # updated status, notify client
    if active_websocket:
        await active_websocket.send_text(f"Task status updated: {task_status}")

    # reset status
    await asyncio.sleep(5)
    task_status = "pending"
    print("Task reset to pending.")

@app.websocket("/status")
async def websocket_endpoint(websocket: WebSocket):
    global active_websocket
    await websocket.accept()
    active_websocket = websocket
    print("Client connected.")

    try:
        while True:
            # wait client to start
            data = await websocket.receive_text()
            if data == "start":
                print("Task started by client.")
                asyncio.create_task(update_task_status())  # start coroutine to update status
            elif data == "status":
                await websocket.send_text(f"Current task status: {task_status}")

    except WebSocketDisconnect:
        print("Client disconnected.")
        active_websocket = None
