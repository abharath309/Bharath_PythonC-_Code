# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:38:43 2016

@author: bharath
"""


def HalfToFloat(h):
    s = int((h >> 15) & 0x00000001)    # sign
    print (s)
    e = int((h >> 10) & 0x0000001f)    # exponent
    f = int(h & 0x000003ff)            # fraction

    if e == 0:
       if f == 0:
          return int(s << 31)
       else:
          while not (f & 0x00000400):
             f <<= 1
             e -= 1
          e += 1
          f &= ~0x00000400
          print (s,e,f)
    elif e == 31:
       if f == 0:
          return int((s << 31) | 0x7f800000)
       else:
          return int((s << 31) | 0x7f800000 | (f << 13))

    e = e + (127 -15)
    f = f << 13

    return int((s << 31) | (e << 23) | f)


if __name__ == "__main__":

    # sample (1.0) - see Wikipedia
    FP16='\x00\x3c'



 