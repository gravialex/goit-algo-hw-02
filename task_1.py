import queue
import time
import random
import uuid

# Create a queue
request_queue = queue.Queue()

def generate_request():
    # Generate a unique identifier
    request_id = f"REQ-{uuid.uuid4().hex[:8].upper()}"
    
    print(f"\n -> New request generated and added to queue: {request_id}")
    request_queue.put(request_id)

def process_request():
    if not request_queue.empty():
        # Remove the request from the queue
        request_id = request_queue.get()
        print(f" ->  Processing request: {request_id}...")
        
        # Simulate time spent processing the request
        time.sleep(1)
        print(f" ->  Request {request_id} has been successfully processed.")
    else:
        print("[!] The queue is empty. No requests to process at the moment.")

def main():
    print("Press Ctrl+C to exit the program at any time.\n")
    # An example of empty queue processing
    process_request()

    # Simulate generating and processing requests in a loop
    try:
        while True:
            generate_request()
            process_request()
            
            # Wait a bit before the next cycle to make output readable
            print(f"Current queue size: {request_queue.qsize()}")
            print("--------------------------------------------")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\nProgram stopped by user. Exiting...")

if __name__ == "__main__":
    main()