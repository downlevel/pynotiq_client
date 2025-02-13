import json
import os
import uuid
from datetime import datetime

# Default queue file path
QUEUE_FILE = os.getenv("QUEUE_FILE_PATH", "queue.json")

class PyNotiQ:
    def __init__(self, queue_file=QUEUE_FILE):
        self.queue_file = queue_file
        # Ensure queue file exists
        if not os.path.exists(self.queue_file):
            with open(self.queue_file, "w") as f:
                json.dump([], f)

    def add_message(self, message):
        """Adds a message to the queue"""
        if "id" not in message:
            message["id"] = message.get("id", str(uuid.uuid4()))  # Unique ID
        
        message["timestamp"] = datetime.utcnow().isoformat()  # Add timestamp

        # Read existing queue
        with open(self.queue_file, "r") as f:
            queue = json.load(f)

        # Check if message already exists
        item_id = message["id"]
        if any(item["id"] == item_id for item in queue):
            return

        queue.append(message)  # Add new message

        # Write back to queue
        with open(self.queue_file, "w") as f:
            json.dump(queue, f, indent=4)

        print(f"✅ Message added: {message['title']}")

    def get_messages(self):
        """Returns all messages from the queue"""
        with open(self.queue_file, "r") as f:
            return json.load(f)

    def clear_queue(self):
        """Clears the queue"""
        with open(self.queue_file, "w") as f:
            json.dump([], f)
        print("🚀 Queue cleared!")
