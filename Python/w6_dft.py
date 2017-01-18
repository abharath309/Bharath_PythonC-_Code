# AUTHOR Bharath abharath@bu.edu
from numpy import fft,zeros,exp,array,pi
def DFT(x):
    try:
        x = array(x,complex)
        N = x.shape[0]
        X = zeros(N,complex)
        for k in range(N):
            for n in range(N):
                X[k] += x[n]*exp(-1j*2*pi*n*k/N)
        return X
    except:
        pass
    raise ValueError
    
def main():
    x = [1,6]
    print(DFT(x))
    print(fft.fft(x))

if __name__=='__main__':
    main()