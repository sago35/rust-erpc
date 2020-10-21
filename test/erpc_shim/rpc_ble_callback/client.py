#
# Generated by erpcgen 1.8.0 on Thu Oct 22 01:33:52 2020.
#
# AUTOGENERATED - DO NOT EDIT
#

import erpc
from . import common, interface
# import callbacks declaration from other groups
from ..rpc_ble_api import interface as interface_ble_api

# Client for rpc_ble_callback
class rpc_ble_callbackClient(interface.Irpc_ble_callback):
    def __init__(self, manager):
        super(rpc_ble_callbackClient, self).__init__()
        self._clientManager = manager

    def rpc_ble_handle_gap_msg(self, gap_msg):
        # Build remote function invocation message.
        request = self._clientManager.create_request()
        codec = request.codec
        codec.start_write_message(erpc.codec.MessageInfo(
                type=erpc.codec.MessageType.kInvocationMessage,
                service=self.SERVICE_ID,
                request=self.RPC_BLE_HANDLE_GAP_MSG_ID,
                sequence=request.sequence))
        if gap_msg is None:
            raise ValueError("gap_msg is None")
        codec.write_binary(gap_msg)

        # Send request and process reply.
        self._clientManager.perform_request(request)
        _result = codec.read_uint32()
        return _result

    def rpc_ble_gap_callback(self, cb_type, cb_data):
        # Build remote function invocation message.
        request = self._clientManager.create_request()
        codec = request.codec
        codec.start_write_message(erpc.codec.MessageInfo(
                type=erpc.codec.MessageType.kInvocationMessage,
                service=self.SERVICE_ID,
                request=self.RPC_BLE_GAP_CALLBACK_ID,
                sequence=request.sequence))
        if cb_type is None:
            raise ValueError("cb_type is None")
        codec.write_uint8(cb_type)
        if cb_data is None:
            raise ValueError("cb_data is None")
        codec.write_binary(cb_data)

        # Send request and process reply.
        self._clientManager.perform_request(request)
        _result = codec.read_uint32()
        return _result

    def rpc_ble_gattc_callback(self, gatt_if, conn_id, cb_data, extra_data):
        # Build remote function invocation message.
        request = self._clientManager.create_request()
        codec = request.codec
        codec.start_write_message(erpc.codec.MessageInfo(
                type=erpc.codec.MessageType.kInvocationMessage,
                service=self.SERVICE_ID,
                request=self.RPC_BLE_GATTC_CALLBACK_ID,
                sequence=request.sequence))
        if gatt_if is None:
            raise ValueError("gatt_if is None")
        codec.write_uint8(gatt_if)
        if conn_id is None:
            raise ValueError("conn_id is None")
        codec.write_uint8(conn_id)
        if cb_data is None:
            raise ValueError("cb_data is None")
        codec.write_binary(cb_data)
        if extra_data is None:
            raise ValueError("extra_data is None")
        codec.write_binary(extra_data)

        # Send request and process reply.
        self._clientManager.perform_request(request)
        _result = codec.read_uint32()
        return _result

    def rpc_ble_gatts_callback(self, gatt_if, conn_id, attrib_index, event, property, read_cb_data, write_cb_data, app_cb_data):
        assert type(read_cb_data) is erpc.Reference, "out parameter must be a Reference object"

        # Build remote function invocation message.
        request = self._clientManager.create_request()
        codec = request.codec
        codec.start_write_message(erpc.codec.MessageInfo(
                type=erpc.codec.MessageType.kInvocationMessage,
                service=self.SERVICE_ID,
                request=self.RPC_BLE_GATTS_CALLBACK_ID,
                sequence=request.sequence))
        if gatt_if is None:
            raise ValueError("gatt_if is None")
        codec.write_uint8(gatt_if)
        if conn_id is None:
            raise ValueError("conn_id is None")
        codec.write_uint8(conn_id)
        if attrib_index is None:
            raise ValueError("attrib_index is None")
        codec.write_uint16(attrib_index)
        if event is None:
            raise ValueError("event is None")
        codec.write_uint32(event)
        if property is None:
            raise ValueError("property is None")
        codec.write_uint16(property)
        if write_cb_data is None:
            raise ValueError("write_cb_data is None")
        codec.write_binary(write_cb_data)
        if app_cb_data is None:
            raise ValueError("app_cb_data is None")
        codec.write_binary(app_cb_data)

        # Send request and process reply.
        self._clientManager.perform_request(request)
        read_cb_data.value = codec.read_binary()
        _result = codec.read_uint32()
        return _result



