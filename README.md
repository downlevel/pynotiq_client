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
    "id" : 1,
    "message" : {
        "message_field_1" : "mesage field 1 value",
        "message_field_2" : "mesage field 2 value"
    }
})

messages = notifier.get_messages()
print(messages)
```

## Features
Add messages to the queue
Retrieve messages from the queue
Clear the queue
