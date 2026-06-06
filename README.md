
# Two-Way Communication System - Client/Server Chat Application

A simple yet powerful demonstration of bidirectional communication between a client and server using Python sockets with **multi-threading** for simultaneous sending and receiving of messages.

## 🎯 Project Overview

This project implements a real-time two-way communication system where both the client and server can send and receive messages independently. Unlike traditional request-response models, this allows both parties to initiate conversations at any time.

## 📚 Key Concepts Applied

- **Sockets**: TCP/IP socket programming for network communication
- **Multi-threading**: Concurrent handling of sending and receiving operations
- **Port & IP Addressing**: Using localhost (127.0.0.1) and port 5555
- **Bidirectional Communication**: Simultaneous message exchange

## 🛠️ Prerequisites

- Python 3.x installed on your system
- Basic understanding of networking concepts
- Two terminal windows (or one terminal with background processes)

## 🚀 How to Run

### Step 1: Clone or Download the Files
Save the following files in the same directory:
- `server.py`
- `client.py`

### Step 2: Start the Server
Open **Terminal 1** and run:
```bash
python server.py
```
You should see:
```
[*] Server listening on port 5555...
```

### Step 3: Start the Client
Open **Terminal 2** and run:
```bash
python client.py
```
You should see:
```
[+] Connected to server. Type 'quit' to exit
```

### Step 4: Start Chatting!

**From Client Terminal:**
```
[You]: Hello Server!
```

**From Server Terminal:**
```
[Client]: Hello Server!
[You]: Hi Client! How are you?
```

**From Client Terminal:**
```
[Server]: Hi Client! How are you?
[You]: I'm doing great, thanks!
```

### Step 5: Exit the Program
Type `quit` in either terminal to close the connection.

## 📁 File Structure

```
├── server.py          # Server-side implementation
├── client.py          # Client-side implementation
└── README.md          # Project documentation
```

## 🔧 Code Explanation

### Server Side (server.py)

```python
def start_server():
    # 1. Create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Bind to IP and Port
    server_socket.bind(('127.0.0.1', 5555))
    
    # 3. Listen for connections
    server_socket.listen(1)
    
    # 4. Accept client connection
    client_socket, address = server_socket.accept()
    
    # 5. Create two threads:
    #    - One for receiving messages
    #    - One for sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
```

### Client Side (client.py)

Similar structure but connects to the server instead of binding.

### Thread Functions

**`receive_messages(socket)`**
- Continuously listens for incoming messages
- Displays received messages immediately
- Handles disconnection gracefully

**`send_messages(socket)`**
- Takes user input from terminal
- Sends messages through the socket
- Allows 'quit' command to exit

## 🧪 Testing Scenarios

| Test Case | Expected Result |
|-----------|----------------|
| Client sends message | Server displays it |
| Server sends message | Client displays it |
| Simultaneous messages | Both received correctly |
| Type 'quit' | Connection closes cleanly |
| Close one terminal | Other detects disconnection |

## 🎨 Sample Output

**Server Terminal:**
```
[*] Server listening on port 5555...
[+] Client connected from ('127.0.0.1', 54321)
[Client]: Hello Server!
[You]: Hey Client!
[Client]: What are you working on?
[You]: Building a chat application!
[!] Client disconnected
```

**Client Terminal:**
```
[+] Connected to server. Type 'quit' to exit
[You]: Hello Server!
[Server]: Hey Client!
[You]: What are you working on?
[Server]: Building a chat application!
[You]: quit
```

## 🔍 Technical Details

### Socket Configuration
- **Address Family**: AF_INET (IPv4)
- **Socket Type**: SOCK_STREAM (TCP)
- **Host**: 127.0.0.1 (localhost)
- **Port**: 5555 (can be changed)
- **Buffer Size**: 1024 bytes

### Threading Mechanism
- Two threads run concurrently
- No blocking operations
- Graceful shutdown handling

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Address already in use | Change port number or wait for socket to release |
| Connection refused | Ensure server is running before client |
| Messages not showing | Check if both threads are running properly |

## 🚧 Possible Enhancements

- [ ] Add GUI interface using tkinter or PyQt
- [ ] Implement message encryption
- [ ] Add multiple client support
- [ ] Create chat rooms
- [ ] Add file transfer capability
- [ ] Implement message history logging
- [ ] Add user authentication

## 📖 Learning Resources

- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)
- [Python Threading Documentation](https://docs.python.org/3/library/threading.html)
- [Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross)

## 👥 Contributors

- Assignment for Computer Networking Programming Course

## 📝 License

This project is for educational purposes as part of coursework.

## 🙏 Acknowledgments

- Instructor for teaching socket programming concepts
- Python documentation team

---

**Made with Python sockets and multi-threading** 🐍
```
