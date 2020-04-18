import socket
import threading
import time
import sys

tello_address = ('192.168.10.1',8889)
local_address = ('', 9000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(local_address)

def send(message, delay):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  time.sleep(delay)

def receive():
  while True:
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      sock.close()
      print("Error receiving: " + str(e))
      break

receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()
print('Type in a Tello SDK command and press the enter key. Enter "quit" to exit this program.')

send("command", 4)
send("takeoff", 10)
send("forward 215", 4)
send("right 71", 4)
send("down 20", 4)
send("forward 195", 4)
send("flip r", 4)
send("land",4)
sock.close()
