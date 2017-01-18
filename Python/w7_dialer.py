# AUTHOR Bharath abharath@bu.edu
import scipy.io.wavfile as wavfile
import numpy as np

file_name=open("one.wav", 'w')


def dialer(file_name,frame_rate,phone,tone_time):

    z=np.array([])
    y = ([])
    number_of_samples = (frame_rate * tone_time)
    #f=200/frame_rate
    x = np.linspace(0,tone_time,number_of_samples)
    #print (x)
    for i in phone:
        if (i=='0'):
            for i in x:
                y.append(np.sin(2*np.pi*941*i) + np.sin(2*np.pi*1336*i))
            z=np.array(y)
        if (i=='1'):
            #print ("value of i",i)
            for i in x:
                y.append(np.sin(2*np.pi*697*i) + np.sin(2*np.pi*1209*i))
            z=np.array(y)
            #print (z)
        if (i=='2'):
            #print ("Value of i",i)
            for i in x:
                #print ("Value of i",i)
                y.append(np.sin(2*np.pi*697*i) + np.sin(2*np.pi*1336*i))
            z=np.array(y)
            #print (z)
            #print (z)
        if (i=='3'):
            #print ("Value of i",i)
            for i in x:
                y.append(np.sin(2*np.pi*697*i) + np.sin(2*np.pi*1477*i))
            z=np.array(y)
            #print (z)
        if (i=='4'):
            for i in x:
                y.append(np.sin(2*np.pi*770*i) + np.sin(2*np.pi*1209*i))
            z=np.array(y)
        if (i=='5'):
            for i in x:
                y.append(np.sin(2*np.pi*770*i) + np.sin(2*np.pi*1336*i))
            z=np.array(y)
        if (i=='6'):
            for i in x:
                y.append(np.sin(2*np.pi*770*i) + np.sin(2*np.pi*1477*i))
            z=np.array(y)
        if (i=='7'):
            for i in x:
                y.append(np.sin(2*np.pi*852*i) + np.sin(2*np.pi*1209*i))
            z=np.array(y)
            #print (z)
        if (i=='8'):
            for i in x:
                y.append(np.sin(2*np.pi*852*i) + np.sin(2*np.pi*1336*i))
            z=np.array(y)
        if (i=='9'):
            #print ("Value of i",i)
            for i in x:
                y.append(np.sin(2*np.pi*852*i) + np.sin(2*np.pi*1477*i))
            z=np.array(y)
            #print (z)
       
        
#    print(z)
#    print(np.shape(z)) 
#    a = np.reshape(-1,1)
#    a = np.array(z)  
#    print (a)
    wavfile.write(file_name,10,z)
    
def main():
    dialer('one.wav',10,str(1),1.0)
    
if __name__ =='__main__':
    main()