import socket
import threading

def receive_messages(server_socket):
    """Thread function to continuously receive messages from server"""
    while True:
        try:
            message = server_socket.recv(1024).decode('utf-8')
            if not message:
                print("\n[!] Server disconnected")
                break
            print(f"\n[Server]: {message}")
            print("[You]: ", end="", flush=True)
        except:
            print("\n[!] Connection lost")
            break

def send_messages(server_socket):
    """Thread function to send messages to server"""
    while True:
        message = input("[You]: ")
        if message.lower() == 'quit':
            server_socket.close()
            break
        server_socket.send(message.encode('utf-8'))

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))
    
    print("[+] Connected to server. Type 'quit' to exit")
    
    # Create threads for sending and receiving
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    
    receive_thread.start()
    send_thread.start()
    
    receive_thread.join()
    send_thread.join()
    
    client_socket.close()

if __name__ == "__main__":
    start_client()