import sounddevice as sd
import wave
import speech_recognition as sr

def guardar_audio (nome_arquivo,duracao,taxa=44100):
    audio=sd.rec(int(duracao*taxa),samplerate=taxa,channels=1,dtype='int16')
    print("Diga a lista de mercadorias para serem compradas: ")
    sd.wait()
    with wave.open(nome_arquivo,'wb') as wb:
        wb.setsampwidth(2)
        wb.setnchannels(1)
        wb.setframerate(taxa)
        wb.writeframes(audio.tobytes())
    print ("Gravado com sucesso!")
    
guardar_audio ("audio.wav",10)
