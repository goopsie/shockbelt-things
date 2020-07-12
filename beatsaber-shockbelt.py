from __future__ import print_function
import websocket
import json
import socket
import sys
import time

# punishments['eventName'] = duration_of_shock_in_seconds
# Copy event names from https://github.com/opl-/beatsaber-http-status/blob/master/protocol.md

punishments = {}
punishments['noteMissed'] = 0.5 # You're garbage at beat saber
punishments['pause']      = 0.5 # You can't escape, No matter how much you try.
punishments['failed']     = 2   # Good job loser
punishments['bombCut']    = 1   # Loser, you cut a bomb

serverport = 54027

def shock(connection, sleeptime):
    print('Miss')
    connection.sendall(b'shockon')  # Arduino code will fail, should add failsafe there to make sure relay isn't on for more than 5 seconds
    time.sleep(sleeptime)
    connection.sendall(b'shockoff') # Most likely user will get severe burns or die if this doesn't get recieved

def main():
    print('Started...')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', serverport)
    sock.bind(server_address)   
    sock.listen(1)
    print("Started TCP Server...")

    print("Connecting to Beat Saber...")
    ws = websocket.create_connection("ws://127.0.0.1:6557/socket") # Connect to beatsaber-http-status
    print('Connected!')
    
    print('Waiting For Shockbelt...')
    connection, client_address = sock.accept() # Will stop here until something is connected
    connectionSucceeded = False
    while connectionSucceeded == False:
        # Ugh, i'm too tired to know if i'm doing this well
        while client_address == "": # Will never be empty string unless sock.accept() is garbage
            pass

        connection.sendall(b'ping') # ShockBelt™ Will respond to "ping" with "pong"
        data = connection.recv(16)
        if data == b"pong":         # ShockBelt™ Will respond to "ping" with "pong"
            connectionSucceeded = True
        else:
            print('Invalid response to ping \"' + data.decode("utf-8") + '\"')
    
    shock(connection, 0.1)           # Kindly let user know that ShockBelt™ is connected
    print('Shockbelt Connected!') # ew terminal output

    while True:
        result = ws.recv()
        result_dict = json.loads(result)

        for k, v in punishments.items() : # i love this part
            if result_dict['event'] == k:
                shock(connection, v)
                continue

    ws.close()

if __name__ == "__main__":
    main()
