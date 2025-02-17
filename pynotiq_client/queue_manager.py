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

    def add_message(self, item_id, message):
        item_queue = {}  # Initialize message queue
        """Adds a message to the queue"""
        if item_id is None:
            item_queue["id"] = message.get("id", str(uuid.uuid4()))  # Unique ID
        
        item_queue["timestamp"] = datetime.utcnow().isoformat()  # Add timestamp

        # Read existing queue
        with open(self.queue_file, "r") as f:
            queue = json.load(f)

        # Check if message already exists
        item_id = item_queue["id"]
        if any(item["id"] == item_id for item in queue):
            return

        item_queue["message"] = message  
        queue.append(item_queue)  # Add new message

        # Write back to queue
        with open(self.queue_file, "w") as f:
            json.dump(queue, f, indent=4)

        print(f"✅ Message added: {item_queue['id']}")

    def get_messages(self):
        """Returns all messages from the queue"""
        with open(self.queue_file, "r") as f:
            return json.load(f)

    def clear_queue(self):
        """Clears the queue"""
        with open(self.queue_file, "w") as f:
            json.dump([], f)
        print("🚀 Queue cleared!")

    def remove_message(self, item_id):
        """Removes a message from the queue"""
        with open(self.queue_file, "r") as f:
            queue = json.load(f)

        new_queue = [item for item in queue if item["id"] != item_id]

        with open(self.queue_file, "w") as f:
            json.dump(new_queue, f, indent=4)
        print(f"🗑 Message removed: {item_id}")

    def update_message(self, new_message):
        """Updates a message in the queue"""
        with open(self.queue_file, "r") as f:
            queue = json.load(f)

        for item in queue:
            if item["id"] == new_message["id"]:
                item.update(new_message)
                break

        with open(self.queue_file, "w") as f:
            json.dump(queue, f, indent=4)
        print(f"🔄 Message updated: {new_message}")