# AUTHOR Bharath abharath@bu.edu

import scipy.io.wavfile as wavfile
import PyQt4.QtGui as qt
import time
import numpy as np
import matplotlib.pyplot as pyplot

def read_wave(fname,debug=False):
    frame_rate,music = wavfile.read(fname)
    if debug:
        print(frame_rate,type(music),music.shape,music.ndim)
    if music.ndim>1:
        nframes,nchannels = music.shape
    else:
        nchannels = 1
        nframes = music.shape[0] 
    #print (music)
    
    #print (music.flatten(),frame_rate,nframes,nchannels
    #print (np.shape(music))
#    print (music)
#    print (frame_rate)
    return music,frame_rate,nframes,nchannels

    
#def wavplay(fname):
#    qt.QSound.play(fname)
#    music,frame_rate,nframes,nchannels = read_wave(fname)
#    time.sleep(nframes/frame_rate)


def loudest_band (music,frame_rate,bandwidth):
  print ("frame_rate",frame_rate)
  print ("bandwidth",bandwidth)
  music_fft = np.fft.fft(music)
  print (abs(music_fft))
  N = music_fft.shape[0]
  print ("Value of N", N)
  wind_len = int(bandwidth*N/frame_rate)
  print ("Window_length",wind_len)
  abs_music = abs(music_fft)**2
  print ("Absolute square",abs_music)
  filter = np.ones(wind_len)
  print ("filter",filter)
  energy = np.convolve(abs_music[0:int(N/2)+1],filter,'valid')
  print ("energy",energy)
  low_freq = np.argmax(energy)
  print ("low_freq",low_freq)
  high_freq = low_freq+wind_len
  print ("high_freq",high_freq)
  low  = low_freq*frame_rate/N
  high = high_freq*frame_rate/N
  print ("low,high",low,high)
  out_music = np.zeros(N,'complex128')
  print (out_music)
  out_music[low_freq:high_freq+1]   = music_fft[low_freq:high_freq+1]
  out_music[-high_freq:-low_freq+1] = music_fft[-high_freq:-low_freq+1]
  print ("Out Music",out_music)
  print ("Inverse FFT",np.fft.ifft(out_music))
  loudest = np.real(np.fft.ifft(out_music))
  print ("low",low)
  print ("High",high)
  print ("loudest",loudest)
  return (low,high,loudest)
  
def main():
    
    fname = "one.wav"
    music,frame_rate,nframes,nchannels = read_wave(fname)
    loudest_band(music,10,2)
    
if __name__ == '__main__':
    main()
    
  

