import numpy as np
def L2(v, *args):
    """Returns the computed L2 norm of a vector v.
    
    INPUTS
    =======
    v: list, 
        vector in form of list of numbers
    *args: optional, list
        vector of weights & must be same length at v
   
    
    RETURNS
    ========
    L2: float
        L2 norm of a vector v
    
    EXAMPLES
    =========
    >>> L2([3,4])
    5.0
    """
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)
def test_L2():
    assert L2([3,4]) == 5.0
test_L2()
def test_L2_types():
    try:
        L2([3,4],[3,3,3])
    except ValueError as err:
        assert(type(err) == ValueError)

test_L2_types()
def test_L2_weighted():
    assert L2([3,4],[1,1]) == 5.0
test_L2_weighted()