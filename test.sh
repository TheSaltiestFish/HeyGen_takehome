#!/bin/bash
echo "Starting server..."
uvicorn server:app --host 0.0.0.0 --port 8888 &
SERVER_PID=$!

sleep 1
echo "Starting client..."
python3 client.py

echo "Stopping server..."
kill $SERVER_PID
