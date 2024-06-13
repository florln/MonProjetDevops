import os
print("Hello, DevOps World!")
message = os.getenv("MESSAGE", "Hello, DevOps World!")
print(message)