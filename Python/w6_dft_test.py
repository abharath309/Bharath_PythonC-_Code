# AUTHOR Bharath abharath@bu.edu
#from w6_dft import DFT
import unittest
import numpy

class DFTTestCase(unittest.TestCase):
    """unit testing for polynomials"""

    def setUp(self):
        pass

    def test_eq(self):
        x = [3,5]
        #print (DFT(x).shape)
        y = numpy.fft.fft([3,5])
        #print(y)
        #print (y.shape)
        self.assertEqual(DFT(x).shape,y.shape)
    
    def test_dtype(self):
        x = [4,7]
        #print (DFT(x).dtype)
        y = numpy.fft.fft([4,7])
        #print(y)
        #print (y.dtype)
        self.assertEqual(y.dtype,DFT(x).dtype)
    
    def test_badinp(self):
          a  = "abc"
          b  = [1,2,3,4,'a']
          c =  [[1,2,3,4],[2,3,4,5]]
          self.assertRaises(ValueError,DFT,a)
          self.assertRaises(ValueError,DFT,b)
          self.assertRaises(ValueError,DFT,c)
          self.assertRaises(ValueError,DFT,{1:2,4:6})
          
    def test_expl_handle(self):
        check_1=bytearray([1,3,4])
        numpy_1=DFT(check_1)
        numpy_2=numpy.fft.fft(check_1)
        for i in range(len(numpy_1)):
            self.assertAlmostEqual(numpy_1[i],numpy_2[i])

    
    def test_random(self):
        count=2
        list1=[]
        while(count<=20):
            for _ in range(10):
                for _ in range(count):
                    list1.append(complex(numpy.random.uniform(-1,1),numpy.random.uniform(-1,1)))
                np_1=DFT(list1)
                np_2=numpy.fft.fft(list1)
                for i in range(len(np_1)):
                    self.assertAlmostEqual(np_1[i],np_2[i])
                list1.clear()
            count=count+1
               

    def tearDown(self):
        "tear down"

if __name__ == '__main__':
    from w6_dft import DFT
    unittest.main(verbosity=4)

