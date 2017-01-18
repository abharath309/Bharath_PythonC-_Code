import unittest
import sys
#import w4_polynomial
# AUTHOR Bharath abharath@bu.edu
authors=['abharath@bu.edu']
class PolynomialTestCase(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_assert_true(self):
        
        Zero = Polynomial([])
        One = Polynomial([0,1])
        self.assertTrue(True)
        self.assertTrue(One)
        
    def test_assert_false(self):
        
        Zero = Polynomial([])
        One = Polynomial([0,1])
        #self.assertFalse(False)
        self.assertFalse(Zero != Zero + One )
    
    def test_assert_Equal(self): 
        
        Zero = Polynomial([])
        One = Polynomial([1])
        
        #self.assertEqual(self.q1 + self.q2,Polynomial([6,5]))
        self.assertNotEqual(Zero == One, True)
        #self.assertGreater(Zero,One)
        
    
    def test_addition(self): 
        
       Y = (Polynomial([]) + Polynomial([1]))
       X = Polynomial([0,1])
       self.assertNotEqual([Y],[X])
       
    def test_sub(self): 
        
       Y = (Polynomial([1]) - Polynomial([0]))
       X = Polynomial([0,1])
       self.assertNotEqual([Y],[X])
       #self.assertEqual(X,Y)
       
    def test_dict(self):
       #Zero = Polynomial([])       
       D1 = {'a': 1, 'b': 2, 'c': [1, 2]}
       D2 = {'a': 1, 'b': 2, 'c': [1, 2]}
       self.assertDictEqual(D1,D2)
       
    def test_init(self):
        z = Polynomial()
        self.assertIsInstance(z,Polynomial)
       
    def test_scalar_mul(self):
        
       Zero = Polynomial([])
       One = Polynomial([1]) 
       p = Polynomial([2,3,4])
       self.assertNotEqual(p * One, p)
       self.assertEqual(p * Zero, Zero)
       self.assertEqual(Zero * p, Zero)
       self.assertAlmostEquals(p.eval(1),9)


    def test_operations(self):
        p = [2,3,4]
        #self.assertEqual((p * p) * p, p * (p * p))
        self.assertEqual((p + p) + p, p + (p + p))
        #self.assertEqual(p-p, Zero)

    def test_unitary(self):
        p = Polynomial([2,3,4])
        q = Polynomial([-2,-3,-4])
        self.assertNotEqual(p + q, Polynomial([]))
#        self.assertEqual(p, +p)
        #self.assertEqual(self.p1-self.p2,Polynomial([4,-2,-3]))
        
#            

	
    def test_set_coeff(self):
        N = 10
        p = [1,2,3,4,5,6,7,8,9,1,0]
        q = len(p)
        self.assertGreaterEqual(q, N)
        
#    def test_deriv(self):
#        out = Polynomial([1,2])
#        self.assertNotEqual(out.deriv(),Polynomial([8,0]))
        
    def tearDown(self):
        "tear down"

        
    def test_sparse_zeros(self):
        n = 10000
        p = Polynomial([0]*n)
        q = Polynomial([])

        p_size =sum(sys.getsizeof(getattr(p,x)) for x in vars(p))
        q_size =sum(sys.getsizeof(getattr(q,x)) for x in vars(q))        
        factor_increase = p_size/q_size
        self.assertEqual(p,q)
        self.assertLess(factor_increase,10,msg='Implementation not sparse, init with {} zeros'.format(n))
        
#    def testPow(self):
#        self.assertEquals(Polynomial([10, 3, 9]), (pow(Polynomial([-1, 1], 13), 10, Polynomial([1, 0, 0, 1], 13)));

    def testRepr(self):
        self.assertNotEquals("-1 + x^3 - x^4 + 2x^7", Polynomial([-1, 0, 0, 1, -1, 0, 0, 2]));


if __name__ == '__main__':
    unittest.main()
