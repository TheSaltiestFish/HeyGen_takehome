## Usage
````
# install dependencies
pip install fastapi websockets uvicorn

./test.sh
````

## Idea

Here I decide to change from pulling to pushing. Instead of client side querying for updates, client and server keep a 
connection, server took the initiative to push update and notice to client side, so client can avoid extra calls and get
update faster. Here I used WebSocket to maintain such connection, but it can also be done with plain socket connection.

The other idea is for client to keep doing pulling and querying, but with an exponential backoff like Aloha and Ethernet
protocol but with an upper limit to make sure it don't get update too late. Here I didn't implement it.