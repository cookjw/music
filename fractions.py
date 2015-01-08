class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator        
        self.decimal = float(self.numerator / self.denominator)
        
    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)        
        
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)   

    def __cmp__(self, other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator        
        return a*d - b*c             

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __add__(self, other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return Fraction(a*d + b*c, b*d) 

    def __sub__(self, other):
        return self + -other  

    def __mul__(self, other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return Fraction(a*c, b*d)

    def __div__(self, other):
        return self * other.reciprocal()             

    def __float__(self):
        return self.decimal    
            
    
    
    
