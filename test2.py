import queue
import streamlit as st

class ObservableQueue(queue.Queue):
    def __init__(self, *args, on_change=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_change = on_change  # Callback to notify changes

    def put(self, item, *args, **kwargs):
        super().put(item, *args, **kwargs)
        if self.on_change:
            self.on_change("put", item)

    def get(self, *args, **kwargs):
        item = super().get(*args, **kwargs)
        if self.on_change:
            self.on_change("get", item)
        return item

# Example usage
def queue_change_listener(action, item):
    print(f"Queue action: {action}, Item: {item}")

# Create an ObservableQueue with the listener
q = ObservableQueue(on_change=queue_change_listener)

# Test the queue
q.put("A")
q.put("B")

st.write(q.get())