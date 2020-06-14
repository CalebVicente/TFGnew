# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:49:21 2020

@author: cvicentm
"""

#pip install SpeechREcognition
#pip install pydub
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from tqdm import tqdm
song = AudioSegment.from_wav("audio\ser_prueba_long.wav")
chunk_length_ms = 10000 # pydub calculates in millisec
chunks = make_chunks(song, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = "audio_chunks\chunk{0}.wav".format(i)
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")


r = sr.Recognizer()
hola = []
#tiene que ser en forma en formato wav, no vale ni mp3 ni 
for i in tqdm(range(74)):
    harvard = sr.AudioFile('audio_chunks\chunk{0}.wav'.format(i))
    with harvard as source:
        audio = r.record(source)
    print("empieza el reconocimiento")
    try:
        hola.append(r.recognize_google(audio, language="es-ES"))
    except:
        print("[AudioChunkError] this audio fails audio_chunks\chunk{0}.wav".format(i))
