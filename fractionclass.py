# Fractions as a class

class Frac:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.denom = denominator
        self.write =  "%d/%d" % (numerator, denominator)
        
def recip(fraction):
    return Frac(fraction.denom, fraction.num)    
    
def fracplus(f1, f2):
    a = f1.num
    b = f1.denom
    c = f2.num
    d = f2.denom
    return Frac(a*d + b*c, b*d)

        
x = Frac(1,2)

print x.write

y = recip(x)

print y
print y.denom
print y.write

x = Frac(1,2)
y = Frac(1,3)

z = fracplus(x,y)
print z.write
        
    