(* ::Package:: *)

BeginPackage["bluetooth`"]


BluetoothDiscoverDevices::usage = "BluetoothDiscoverDevices[sessions] discovers all the Bluetooth devices near you"
BluetoothAddressLookupName::usage = "BluetoothAddressLookupName[session,address] finds the name of a device given an address"
BluetoothSocketCreate::usage = "BluetoothSocketCreate[session,socketId] creates a new socket"
BluetoothSocketBind::usage = "BluetoothSocketBind[session,socketId,port] binds the socket"
BluetoothSocketListen::usage = "BluetoothSocketListen[session,socketId] start listening on a socket"
BluetoothSocketAccept::usage = "BluetoothSocketAccept[session,socketId,clientSocketId] accept a connection on the socket"
BluetoothSocketGetAddress::usage = "BluetoothSocketGetAddress[session,socketId] returns the address of the socket"
BluetoothSocketReceive::usage = "BluetoothSocketRecive[session,socketId] recives data on the socket"
BluetoothSocketClose::usage = "BluetoothSocketClose[session,socketId] closes a connection on the socket"
BluetoothSocketConnect::usage = "BluetoothSocketConnect[session,socketId,address,port] connects the socket"
BluetoothSocketSend::usage = "BluetoothSocketSend[session,socketId,data] sends a message through a socket"


Begin["`Private`"]


BluetoothDiscoverDevices[session_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothDiscoverDevices",
	"Arguments"->{}|>])


BluetoothAddressLookupName[session_, address_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothAddressLookupName",
	"Arguments"->{address}|>])


BluetoothSocketCreate[session_, socketId_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothSocketCreate",
	"Arguments"->{socketId}|>])


BluetoothSocketBind[session_, socketId_, port_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothSocketBind",
	"Arguments"->{socketId, port}|>])


BluetoothSocketListen[session_, socketId_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothSocketListen",
	"Arguments"->{socketId}|>])


BluetoothSocketAccept[session_, socketId_, clientSocketId_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothSocketAccept",
	"Arguments"->{socketId, clientSocketId}|>])


BluetoothSocketGetAddress[session_, socketId_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothSocketGetAddress",
	"Arguments"->{socketId}|>])


BluetoothSocketReceive[session_, socketId_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothSocketReceive",
	"Arguments"->{socketId}|>])


BluetoothSocketClose[session_, socketId_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothSocketClose",
	"Arguments"->{socketId}|>])


BluetoothSocketConnect[session_, socketId_, address_, port_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothSocketConnect",
	"Arguments"->{socketId, address, port}|>])


BluetoothSocketSend[session_, socketId_, data_] := (ExternalEvaluate[session,
	<|"Command"->"BluetoothSocketSend",
	"Arguments"->{socketId, data}|>])


End[]


EndPackage[]
