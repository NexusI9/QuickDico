import os
import pocketsphinx as ps
import speech_recognition  as sr
import pyaudio

#Languages Data Path: 
#/Users/elkhantour/.local/share/virtualenvs/QuickDico-di7jp7lL/lib/python3.9/site-packages/speech_recognition/pocketsphinx-data/

input_source_index = 0;

def listen(source_index=0):
    r = sr.Recognizer()
    mic = sr.Microphone(source_index)
    return 

    with mic as source:
            audio = r.listen(source)

    type(audio)
    c = r.recognize_sphinx(audio, language='zh-cn')
    print(c)


def device():
    os.system('clear')
    pa = pyaudio.PyAudio();
    device_count = pa.get_device_count()
    print('Select an input to listen to (default 0):')
    for index in range(0, device_count):
         print('%d \t %s' % (index, pa.get_device_info_by_index(index)['name']))
    selected_index = int(input('Input device index: '));
    if(selected_index > device_count or selected_index < 0 ):
         return device()
    else:
         return selected_index
    

input_source_index = device()
listen(input_source_index)
