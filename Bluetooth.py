import bluetooth

sockets : dict = {}
addresses : dict = {}

def BluetoothDiscoverDevices() -> None:
    return bluetooth.discover_devices(flush_cache = True, lookup_names = True)

def BluetoothAddressLookupName(address : str) -> None:
    return bluetooth.lookup_name(address)

def BluetoothSocketCreate(socketId : int) -> None:
    sockets[socketId] = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

def BluetoothSocketGet(socketId : int) -> None:
    if socketId in sockets:
        return sockets[socketId]
    else:
        return None

def BluetoothSocketBind(socketId : int, port : int) -> None:
    socket : bluetooth.BluetoothSocket = BluetoothSocketGet(socketId)
    if socket:
        socket.bind(('', port))

def BluetoothSocketListen(socketId : int) -> None:
    socket : bluetooth.BluetoothSocket = BluetoothSocketGet(socketId)
    if socket:
        socket.listen(1)

def BluetoothSocketAccept(socketId : int, clientSocketId : int) -> None:
    socket : bluetooth.BluetoothSocket = BluetoothSocketGet(socketId)
    if socket:
        clientSocket, address = socket.accept()

        sockets[clientSocketId] = clientSocket
        addresses[clientSocketId] = address[0]

def BluetoothSocketGetAddress(socketId : int) -> None:
    socket : bluetooth.BluetoothSocket = BluetoothSocketGet(socketId)
    if socket and socketId in addresses:
        return addresses[socketId]
    else:
        return None

def BluetoothSocketReceive(socketId : int) -> None:
    socket : bluetooth.BluetoothSocket = BluetoothSocketGet(socketId)
    if socket:
        return str(socket.recv(1024))

def BluetoothSocketClose(socketId : int) -> None:
    socket : bluetooth.BluetoothSocket = BluetoothSocketGet(socketId)
    if socket:
        socket.close()

        del addresses[socketId]
        del sockets[socketId]

def BluetoothSocketConnect(socketId : int, address : str, port : int) -> None:
    socket : bluetooth.BluetoothSocket = BluetoothSocketGet(socketId)
    if socket:
        socket.connect((address, port))

def BluetoothSocketSend(socketId : int, data : str) -> None:
    socket : bluetooth.BluetoothSocket = BluetoothSocketGet(socketId)
    if socket:
        socket.send(data)