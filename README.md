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
    "title": "Silent Hill PS2",
    "price": 25,
    "url": "https://example.com/item",
    "category": "Games"
})

messages = notifier.get_messages()
print(messages)
```
