import urllib2
from time import sleep
import wave
import pyaudio
#import os

chunk=1024
spoke = False


def test_conn():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=3)
        return True
    except urllib2.URLError as err: 
        return False

def speakthis(msg):
    print msg
##    msg = "\"" + msg + "\""
##    os.system("pico2wave --wave speech.wav " + msg)
    speak()


def speak():
    f = wave.open(r"speech.wav","rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
        channels = f.getnchannels(),  
        rate = f.getframerate(),
        output = True)
    
    #read data  
    data = f.readframes(chunk)  

    #paly stream  
    while data != '':  
        stream.write(data)  
        data = f.readframes(chunk)  

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    return;       


def beep():


        f = wave.open(r"beep.wav","rb")
        p = pyaudio.PyAudio()
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
        channels = f.getnchannels(),  
        rate = f.getframerate(),
        output = True)
    
        #read data  
        data = f.readframes(chunk)  

        #paly stream  
        while data != '':  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

        return;




while True:
    try:
        if test_conn():
            if spoke == False:
                speakthis("connection available.")
                spoke = True
            sleep(5)
    except:
        print "*** Some error occurred!!! ***\n\n"
        beep()
        sleep(1)
        beep()
        sleep(1)
        beep()
        
    else :
        print "No internet connection avialable"
        beep()
        spoke = False

    sleep(5)
