# PyNotiQ Client

A simple Python library to add messages to the PyNotiQ JSON queue.

## Installation

```sh
pip install git+https://github.com/downlevel/pynotiq_client.git
```

## Usage

```python
from pynotiq_client import PyNotiQ

notifier = PyNotiQ(queue_file="queue.json")

notifier.add_message({
    "Id": "bab0cff9-637b-425f-98a2-fe1eb94426ee",
    "Timestamp": "2025-02-17T22:59:39.750319",
    "MessageBody": {
        "message_field_1": "Message Field Value 1",
        "message_field_2": "Message Field Value 2",
    }
})

messages = notifier.get_messages()
print(messages)
```

## Features
Add messages to the queue
Retrieve messages from the queue
Clear the queue
