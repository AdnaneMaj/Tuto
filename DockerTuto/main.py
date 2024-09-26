import json
from dataclasses import dataclass,field
"""
dataclass:
    This a class decorator that rovides some calss functions like __init__,__repr__ etc 

field:
    This is a function that specificy some propertits of and instance of the dataclass
"""

from fastapi import FastAPI,HTTPException,Response
"""

FastAPI is a modern, fast (high-performance) web framework for building APIs 
with Python 3.7+ based on standard Python type hints. It is designed to be 
easy to use, scalable, and efficient, making it ideal for building RESTful 
APIs and asynchronous web applications.
"""

app = FastAPI()

@dataclass
class Channel:
    id: str
    name: str
    tags: list[str] = field(default_factory=list) #The correct way to create mutable default values
    description: str = ""


channels: dict[str,Channel] = {}

with open("channels.json", encoding="utf8") as file:
    channels_raw = json.load(file)
    for channel_raw in channels_raw:
        channel = Channel(**channel_raw)
        channels[channel.id] = channel


@app.get("/")
def read_root() -> Response: #Return type is Response
    return Response("The server is running.")

@app.get("/channels/{channel_id}", response_model=Channel)
def read_item(channel_id: str) -> Channel:
    if channel_id not in channels:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channels[channel_id]