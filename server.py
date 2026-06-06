import socket
import threading

def receive_messages(client_socket):
    """Thread function to continuously receive messages from client"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("\n[!] Client disconnected")
                break
            print(f"\n[Client]: {message}")
            print("[You]: ", end="", flush=True)
        except:
            print("\n[!] Connection lost")
            break

def send_messages(client_socket):
    """Thread function to send messages to client"""
    while True:
        message = input("[You]: ")
        if message.lower() == 'quit':
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen(3)
    
    print("[*] Server listening on port 5555...")
    client_socket, address = server_socket.accept()
    print(f"[+] Client connected from {address}")
    
    # Create threads for sending and receiving
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    
    receive_thread.start()
    send_thread.start()
    
    receive_thread.join()
    send_thread.join()
    
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()