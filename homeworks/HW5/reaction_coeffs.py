import numpy as np
R=8.314
def const(k):
    return k

def arr(A, E, T):
        #Check that A,T,E  are numbers
        if ((type(A) != int and type(A) != float) or 
            (type(T) != int and type(T) != float) or
            (type(E) != int and type(E) != float)):
            raise TypeError("All arguments must be numbers!")
            
        elif (T<0 or A<0): # A & T must be positive
            raise ValueError("Temperature and Arrhenius prefactor must be positive!")
            
        else:
            #Calculate karr
            karr = A*(np.exp(-E/(R*T)))
            return karr
        
def mod_arr(A,E,b,T):
            #Check that A,T,E  are numbers
        if ((type(A) != int and type(A) != float) or 
            (type(b) != int and type(b) != float) or
            (type(E) != int and type(E) != float) or
            (type(T) != int and type(T) != float)):
            raise TypeError("All arguments must be numbers!")
            
        elif (T<0 or A<0): # A & T must be positive
            raise ValueError("Temperature and Arrhenius prefactor must be positive!")
            
        else:
            #Calculate karr
            karr = A*(T**b)*(np.exp(-E/(R*T)))
            return karr