import asyncio
import websockets

async def client_task():
    uri = "ws://localhost:8888/status"
    async with websockets.connect(uri) as websocket:
        print("Connected to server.")

        # start the task
        await websocket.send("start")
        print("Task started.")

        while True:
            try:
                # wait server to notify for update
                message = await websocket.recv()
                print(f"Received from server: {message}")

                # server updated
                if "updated" in message:
                    await asyncio.sleep(1)
                    await websocket.send("status")
                    status = await websocket.recv()
                    print(f"Current status: {status}")
                    break

            except websockets.ConnectionClosed:
                print("Server disconnected.")
                break

if __name__ == "__main__":
    asyncio.run(client_task())
