#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Reference: https://github.com/pythonone/MS17-010/blob/master/scanners/smb_ms17_010.py

class SMB_HEADER(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
    ("server_component", ctypes.c_uint32),
    ("smb_command", ctypes.c_uint8),
    ("error_class", ctypes.c_uint8),
    ("reserved1", ctypes.c_uint8),
    ("error_code", ctypes.c_uint16),
    ("flags", ctypes.c_uint8),
    ("flags2", ctypes.c_uint16),
    ("process_id_high", ctypes.c_uint16),
    ("signature", ctypes.c_uint64),
    ("reserved2", ctypes.c_uint16),
    ("tree_id", ctypes.c_uint16),
    ("process_id", ctypes.c_uint16),
    ("user_id", ctypes.c_uint16),
    ("multiplex_id", ctypes.c_uint16)
    ]

    def __new__(self, buffer=None):
        return self.from_buffer_copy(buffer)

    def __init__(self, buffer):
        pass

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'new_ms17_010'
        self.info = "Check the MS17-010 RCE (new version)"
        self.keyword = ['all', 'ms17-010', 'ms17010', 'rce', 'intranet', 'netbios', 'smb', 'danger', '445']
        self.default_ports_list = [445,]
        VulnCheck.__init__(self, ip_and_port_list)

    def generate_smb_proto_payload(self, *protos):
        """Generate SMB Protocol. Pakcet protos in order.
        """
        hexdata = []
        for proto in protos:
            hexdata.extend(proto)
        return "".join(hexdata)

    def peeknamedpipe_request(self, treeid, processid, userid, multiplex_id):
        """Generate tran2 request
        """
        netbios = [
          '\x00',              # 'Message_Type'
          '\x00\x00\x4a'       # 'Length'
        ]

        smb_header = [
          '\xFF\x53\x4D\x42',  # 'server_component': .SMB
          '\x25',              # 'smb_command': Trans2
          '\x00\x00\x00\x00',  # 'nt_status'
          '\x18',              # 'flags'
          '\x01\x28',          # 'flags2'
          '\x00\x00',          # 'process_id_high'
          '\x00\x00\x00\x00\x00\x00\x00\x00',  # 'signature'
          '\x00\x00',          # 'reserved'
          treeid,
          processid,
          userid,
          multiplex_id
        ]

        tran_request = [
          '\x10',              # Word Count
          '\x00\x00',          # Total Parameter Count
          '\x00\x00',          # Total Data Count
          '\xff\xff',          # Max Parameter Count
          '\xff\xff',          # Max Data Count
          '\x00',              # Max Setup Count
          '\x00',              # Reserved
          '\x00\x00',          # Flags
          '\x00\x00\x00\x00',  # Timeout: Return immediately
          '\x00\x00',          # Reversed
          '\x00\x00',          # Parameter Count
          '\x4a\x00',          # Parameter Offset
          '\x00\x00',          # Data Count
          '\x4a\x00',          # Data Offset
          '\x02',              # Setup Count
          '\x00',              # Reversed
          '\x23\x00',          # SMB Pipe Protocol: Function: PeekNamedPipe (0x0023)
          '\x00\x00',          # SMB Pipe Protocol: FID
          '\x07\x00',
          '\x5c\x50\x49\x50\x45\x5c\x00'  # \PIPE\
        ]

        return self.generate_smb_proto_payload(netbios, smb_header, tran_request)

    def _check(self, ip, port):
        try:
            buffersize = 1024

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(timeout)
            client.connect((ip, port))

            raw_proto = '\x00\x00\x00\x85\xff\x53\x4d\x42\x72\x00\x00\x00\x00\x18\x53\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x00\x00\x40\x00\x00\x62\x00\x02\x50\x43\x20\x4e\x45\x54\x57\x4f\x52\x4b\x20\x50\x52\x4f\x47\x52\x41\x4d\x20\x31\x2e\x30\x00\x02\x4c\x41\x4e\x4d\x41\x4e\x31\x2e\x30\x00\x02\x57\x69\x6e\x64\x6f\x77\x73\x20\x66\x6f\x72\x20\x57\x6f\x72\x6b\x67\x72\x6f\x75\x70\x73\x20\x33\x2e\x31\x61\x00\x02\x4c\x4d\x31\x2e\x32\x58\x30\x30\x32\x00\x02\x4c\x41\x4e\x4d\x41\x4e\x32\x2e\x31\x00\x02\x4e\x54\x20\x4c\x4d\x20\x30\x2e\x31\x32\x00'
            client.send(raw_proto)

            tcp_response = client.recv(buffersize)

            raw_proto = '\x00\x00\x00\x88\xff\x53\x4d\x42\x73\x00\x00\x00\x00\x18\x07\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x00\x00\x40\x00\x0d\xff\x00\x88\x00\x04\x11\x0a\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xd4\x00\x00\x00\x4b\x00\x00\x00\x00\x00\x00\x57\x00\x69\x00\x6e\x00\x64\x00\x6f\x00\x77\x00\x73\x00\x20\x00\x32\x00\x30\x00\x30\x00\x30\x00\x20\x00\x32\x00\x31\x00\x39\x00\x35\x00\x00\x00\x57\x00\x69\x00\x6e\x00\x64\x00\x6f\x00\x77\x00\x73\x00\x20\x00\x32\x00\x30\x00\x30\x00\x30\x00\x20\x00\x35\x00\x2e\x00\x30\x00\x00\x00'
            client.send(raw_proto)
            tcp_response = client.recv(buffersize)

            netbios = tcp_response[:4]
            smb_header = tcp_response[4:36]

            smb = SMB_HEADER(smb_header)

            user_id = struct.pack('<H', smb.user_id)

            session_setup_andx_response = tcp_response[36:]
            
            native_os = session_setup_andx_response[9:].split('\x00')[0]
            
            raw_proto = '\x00\x00\x00\x58\xff\x53\x4d\x42\x75\x00\x00\x00\x00\x18\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe' + user_id + '\x40\x00\x04\xff\x00\x58\x00\x08\x00\x01\x00\x2d\x00\x00\x5c\x00\x5c\x00\x31\x00\x37\x00\x32\x00\x2e\x00\x31\x00\x36\x00\x2e\x00\x39\x00\x39\x00\x2e\x00\x35\x00\x5c\x00\x49\x00\x50\x00\x43\x00\x24\x00\x00\x00\x3f\x3f\x3f\x3f\x3f\x00'
            
            client.send(raw_proto)
            tcp_response = client.recv(buffersize)

            netbios = tcp_response[:4]
            smb_header = tcp_response[4:36]

            smb = SMB_HEADER(smb_header)

            tree_id = struct.pack('<H', smb.tree_id)
            process_id = struct.pack('<H', smb.process_id)
            user_id = struct.pack('<H', smb.user_id)
            multiplex_id = struct.pack('<H', smb.multiplex_id)

            raw_proto = self.peeknamedpipe_request(tree_id, process_id, user_id, multiplex_id)
            client.send(raw_proto)
            tcp_response = client.recv(buffersize)

            netbios = tcp_response[:4]
            smb_header = tcp_response[4:36]
            smb = SMB_HEADER(smb_header)

            nt_status = struct.pack('BBH', smb.error_class, smb.reserved1, smb.error_code)

            # 0xC0000205 - STATUS_INSUFF_SERVER_RESOURCES - vulnerable
            # 0xC0000008 - STATUS_INVALID_HANDLE
            # 0xC0000022 - STATUS_ACCESS_DENIED

            if nt_status == '\x05\x02\x00\xc0':
                result =  "exists MS17-010 RCE vuln, (%s)"%(native_os)
                self._output(ip, port, result)
        
            elif nt_status in ('\x08\x00\x00\xc0', '\x22\x00\x00\xc0'):
                pass
            else:
                pass
            client.close()
        except:
            pass          

globals()['SMB_HEADER'] = SMB_HEADER
globals()['VulnChecker'] = VulnChecker