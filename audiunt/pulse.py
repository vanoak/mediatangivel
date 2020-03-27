# correr com o sonic pi ligado

from time import sleep
import serial
from pythonosc import udp_client
import json

ser = serial.Serial('/dev/cu.usbmodem14201', 9600)

while True:
    j_raw = ser.readline()
    print(j_raw)
    
    try:
        j_obj = json.loads(j_raw)
    except ValueError as e:
        print(e)
        continue

    bpm = j_obj["bpm"]
    # song = "use_bpm "+ str(bpm) + "\nlive_loop :musica do\nplay 60\nsleep 1\nend"
    
    song = "live_loop :slow do\nuse_bpm " + str(bpm) + "\nnotes = (ring :E4, :Fs4, :B4, :Cs5, :D5, :Fs4, :E4, :Cs5, :B4, :Fs4, :D5, :Cs5)\nplay notes.tick, release: 0.1\nsleep 0.3\nend"
    
    print(song)
    
    sender = udp_client.SimpleUDPClient('127.0.0.1', 51235) # alterar para o port que aparece no ficheiro server-output.txt em <HOME>/.sonic-pi/log/server-output.txt linha ~~22 "Opening UDP Server to listen to GUI on port: ..."
    sender.send_message('/run-code',["MY_PYTHON_GUI",song])
    #sender.send_message('/stop-all-jobs',[])
    sleep(2)