import json
from psonic import *
from threading import Thread
import requests
import serial
from time import sleep
import random
from pythonosc import udp_client


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

    song = "live_loop :slow do\nuse_bpm " + str(
        bpm) + "\nnotes = (ring :E4, :Fs4, :B4, :Cs5, :D5, :Fs4, :E4, :Cs5, :B4, :Fs4, :D5, :Cs5)\nplay notes.tick, release: 0.1\nsleep 0.3\nend"

    print(song)

    sender = udp_client.SimpleUDPClient('127.0.0.1',
                                        51235)  # alterar para o port que aparece no ficheiro server-output.txt em <HOME>/.sonic-pi/log/server-output.txt linha ~~22 "Opening UDP Server to listen to GUI on port: ..."
    sender.send_message('/run-code', ["MY_PYTHON_GUI", song])
    # sender.send_message('/stop-all-jobs',[])
    sleep(2)

"""

# funcao generica de alteracao de intervalos
def remap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def synth():
    
    # flags que fazem funcionar os diferentes sensores
    is_online = False # temperatura
    is_connected_arduino = False # sensor de proximidade: amp
    is_connected_pulse_sensor = False #detectar pulsação - arduino envia por wifi

    # CALIBRACAO DE AMPLITUDE
    # variaveis de calibracao de amplitude - min, max e actual vindos do sensor
    amp_sensor = 0
    amp_sensor_max = 0
    amp_sensor_min = 0
    
    if is_connected_arduino:
        ser = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(5)
        print("calibrate amp, please")
        print(ser.readline().decode("utf-8").replace("\'", "\""))
        sensor_data = 0
        try:
            sensor_data = json.loads(ser.readline().decode("utf-8").replace("\'", "\""))
            amp_sensor_min = sensor_data['esq']
            amp_sensor_max = sensor_data['esq']
        except Exception as e:
            print(e)

        for i in range(50):
            print("calibrating loop " + str(i) + " from 50")
            try:
                sensor_data = json.loads(ser.readline().decode("utf-8").replace("\'", "\""))
                if sensor_data['esq'] > amp_sensor_max:
                    amp_sensor_max = sensor_data['esq']
                if sensor_data['esq'] < amp_sensor_min:
                    amp_sensor_min = sensor_data['esq']
                
            except Exception as e:
                print(e)
                continue
            
            print("max_amp: " + str(amp_sensor_max))
            print("min_amp: " + str(amp_sensor_min))
        print("amp calibrated")





    # CALIBRACAO DE NOTA
    # variaveis de calibracao de nota - min, max e actual vindos do sensor
    note_sensor = 0
    note_sensor_max = 0
    note_sensor_min = 0
    
    if is_connected_arduino:
        ser = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(5)
        print("calibrate note, please")
        print(ser.readline().decode("utf-8").replace("\'", "\""))
        sensor_data = 0
        try:
            sensor_data = json.loads(ser.readline().decode("utf-8").replace("\'", "\""))
            note_sensor_min = sensor_data['dir']
            note_sensor_max = sensor_data['dir']
        except Exception as e:
            print(e)

        for i in range(50):
            print("calibrating loop " + str(i) + " from 50")
            try:
                sensor_data = json.loads(ser.readline().decode("utf-8").replace("\'", "\""))
                if sensor_data['dir'] > note_sensor_max:
                    note_sensor_max = sensor_data['dir']
                if sensor_data['dir'] < note_sensor_min:
                    note_sensor_min = sensor_data['dir']
                
            except Exception as e:
                print(e)
                continue
            
            print("max_note: " + str(note_sensor_max))
            print("min_note: " + str(note_sensor_min))
        print("note calibrated")

    """





    # MAIN LOOP
        
    while True:
        print("-----NEW-LOOP----")
        
        # busca temperatura se verdadeiro
        if is_online:
            print("using online temp data")
            payload = {'q':'evora','appid':'69e7458fb9e53236d04fdc768d8fdb5b','units':'metric'}
            j = requests.get('http://api.openweathermap.org/data/2.5/weather',params=payload)
            json_object = json.loads(j.text)
            exterior_temp = json_object['main']['temp']
            print("temp data: " + str(exterior_temp))
        else:
            print("using default temp data")
            exterior_temp = 14 # temperatura por omissao
            
        #busca sensor de amplitude se verdadeiro
        if is_connected_arduino:
            print("reading proximity sensors for amp and note")
            try:
                sensor_data = json.loads(ser.readline().decode("utf-8").replace("\'", "\""))
                amp = remap(int(sensor_data['esq']), int(amp_sensor_min), int(amp_sensor_max), 0.0, 1.0)
                note = remap(int(sensor_data['dir']), int(note_sensor_min), int(note_sensor_max), 50, 100)
            except Exception as e:
                print(e)
                continue
        else:
            print("using default note and amp")
            amp = 1.0
            note = 69

        #busca sensor de pulsacao se verdadeiro
        if is_connected_pulse_sensor:
            print("getting data from pulse sensor")
            pass
        else:
            print("using default for pulse sensor")
            pass

        lista_sintetizadores =  ((BEEP, 10, 40), (BLADE,10, 40), (CHIPBASS,30, 40), (CHIPLEAD,5, 20), (DARK_AMBIENCE,10, 40), (DPULSE,6, 38), (DSAW,5, 20), (DTRI,20, 35), (DULL_BELL,21, 46), (FM,25, 45), (GROWL,11, 36), (HOLLOW,25, 35), (HOOVER,11, 26), (PLUCK,15, 35), (PRETTY_BELL,11, 26), (PROPHET,5, 15), (PULSE,1, 26), (SAW,5, 25), (SINE,1, 16), (SQUARE,5, 25), (SUBPULSE,1, 26), (TB303,15, 25), (TRI,5, 15) )

        synth_in_loop = []
        playlist = []
        
        for i in range(0,5):
            synth_in_loop.append(lista_sintetizadores[random.randrange(0,len(lista_sintetizadores))])
            
        print("play synth list") 


        loop_no = 1
        for i in synth_in_loop:
            use_synth(i[0])
            duration = random.randrange(i[1],i[2])
            play(note, amp=amp ,release=duration)
            print("synth no:" + str(loop_no) + " note: "+ str(note) +" duration:" + str(duration) + " amp:" + str(amp))
            sleep(duration)
            loop_no +=1

synth = Thread(name='synth', target=synth)
synth.start()