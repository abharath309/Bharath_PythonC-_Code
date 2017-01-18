#class Polynomial(object):                                
#  def __init__(self, coefficients):
#   self.coefficients = coefficients
#
#  def __str__(self):
#    polytostring = ' '
#    for exponent, coefficient in self.coefficients.iteritems():
#        if exponent == 0:
#            polytostring += '%s + ' % coefficient
#        else:
#            polytostring += '%sx^%s + ' % (coefficient, exponent)
#
#    polytostring = polytostring.strip(" + ")
#
#    return polytostring


#class Polynomial:
#    def __init__(self, *termpairs):
#        #print (self)
#        print("Termpairs are",termpairs)
#        self.termdict = dict(termpairs)
#        print ("Self.termdict",self.termdict)
# 
#    def print_result(self, key):
#        print ("%dx^%d" % (key, self.termdict[key]))
#        
#        
#if __name__ == '__main__':
#    d1 = Polynomial((2,3), (-4,5), (8,9))
#    #print (d1)    
#    ## extract and sort keys to process in numerical order
#    keys=d1.termdict.keys()
#    #keys.sort()
#    for key in keys:
#       d1.print_result(key)

class Polynomial(object):

    def __init__(self,coeffs):
        self.coefficients = coeffs

    def degree(self):
        return len(self.coefficients)-1

    def eval(self, x):
        p = 0
        for i in range(self.degree(), -1, -1):
            p = p + self.coefficients[i]*(x**i)
        return p

      
#q = [1,2,3]
#a = {}
#print (q)
#a[-4] = 3
#print (a)
#print 
##print (a.items())
##print (a.values())
##print (a.get(2,3))
##print (a.keys())
##q.append(a.__getitem__(self,key))
#q.sort()
#q.reverse()
#print (q)
