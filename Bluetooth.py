import bluetooth

sockets : dict = {}
addresses : dict = {}

def bluetooth_discover_devices() -> None:
    return bluetooth.discover_devices(flush_cache = True, lookup_names = True)

def bluetooth_address_lookup_name(address : str) -> None:
    return bluetooth.lookup_name(address)

def bluetooth_socket_create(socketId : int) -> None:
    sockets[socketId] = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

def bluetooth_socket_get(socketId : int) -> None:
    if socketId in sockets:
        return sockets[socketId]
    else:
        return None

def bluetooth_socket_bind(socketId : int, port : int) -> None:
    socket : bluetooth.BluetoothSocket = bluetooth_socket_get(socketId)
    if socket:
        socket.bind(('', port))

def bluetooth_socket_listen(socketId : int) -> None:
    socket : bluetooth.BluetoothSocket = bluetooth_socket_get(socketId)
    if socket:
        socket.listen(1)

def bluetooth_socket_accept(socketId : int, clientSocketId : int) -> None:
    socket : bluetooth.BluetoothSocket = bluetooth_socket_get(socketId)
    if socket:
        clientSocket, address = socket.accept()

        sockets[clientSocketId] = clientSocket
        addresses[clientSocketId] = address[0]

def bluetooth_socket_get_address(socketId : int) -> None:
    socket : bluetooth.BluetoothSocket = bluetooth_socket_get(socketId)
    if socket and socketId in addresses:
        return addresses[socketId]
    else:
        return None

def bluetooth_socket_receive(socketId : int) -> None:
    socket : bluetooth.BluetoothSocket = bluetooth_socket_get(socketId)
    if socket:
        return str(socket.recv(1024))

def bluetooth_socket_close(socketId : int) -> None:
    socket : bluetooth.BluetoothSocket = bluetooth_socket_get(socketId)
    if socket:
        socket.close()

        del addresses[socketId]
        del sockets[socketId]

def bluetooth_socket_connect(socketId : int, address : str, port : int) -> None:
    socket : bluetooth.BluetoothSocket = bluetooth_socket_get(socketId)
    if socket:
        socket.connect((address, port))

def BluetoothSocketSend(socketId : int, data : str) -> None:
    socket : bluetooth.BluetoothSocket = bluetooth_socket_get(socketId)
    if socket:
        socket.send(data)
