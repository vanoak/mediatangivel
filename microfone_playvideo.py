# detecta intensidade de som no microfone e corre video

import pyaudio
import wave
import math
import audioop
import time
from omxplayer.player import OMXPlayer
from pathlib import Path
 
p = pyaudio.PyAudio() 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 512 

alpha = 0
 
def audio_int(num_samples=50):
    """ Gets average audio intensity of your mic sound. You can use it to get
        average intensities while you're talking and/or silent. The average
        is the avg of the 20% largest intensities recorded.
    """

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,input_device_index=2,
                    frames_per_buffer=CHUNK)
    cur_data = stream.read(CHUNK)
    values = [math.sqrt(abs(audioop.avg(cur_data, 4)))
                for x in range(num_samples)]
    values = sorted(values, reverse=True)
    r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
    #print (' Average audio intensity is r', int(r))
    time.sleep(.1)

    stream.close()
    p.terminate()
    return r


if(__name__ == '__main__'):
	
	VIDEO_PATH = "/home/pi/Desktop/rasto.mp4"
	player = OMXPlayer(VIDEO_PATH, args =['--no-osd','--loop','-b'])
	player.set_aspect_mode('fill')
	player.set_alpha(0)
	
	while(True):
		r = audio_int()  # To measure your  mic levels
		if r > 5000:
			alpha = alpha + 10
			if alpha > 255:
				alpha = 255
		else:
			alpha = alpha - 10
			if alpha < 0:
				alpha = 0
	  
		print(alpha)
		player.set_alpha(alpha)
