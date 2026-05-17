import threading

def start_websocket_threads():
    # Create and start the websocket client threads here
    websocket_thread_1 = threading.Thread(target=websocket_client_func_1)
    websocket_thread_2 = threading.Thread(target=websocket_client_func_2)
    
    websocket_thread_1.start()
    websocket_thread_2.start()
    
    # Return appropriately
    return
