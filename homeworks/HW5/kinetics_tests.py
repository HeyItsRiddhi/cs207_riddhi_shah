import reaction_coeffs
#Test k_const
def test_const():
    assert reaction_coeffs.const(107) == 107
    
#Test k_arr
def test_arr():
    assert reaction_coeffs.arr(107,103,102) == 94.762198593430469

def test_arr_values1():
    try:
        reaction_coeffs.arr(-1,103,102)
    except ValueError as err:
        assert(type(err) == ValueError)
        
def test_arr_values2():
    try:
        reaction_coeffs.arr(107,103,-2)
    except ValueError as err:
        assert(type(err) == ValueError)

def test_arr_types1():
    try:
        reaction_coeffs.arr('107',103,102)
    except TypeError as err:
        assert(type(err) == TypeError)
        
def test_arr_types2():
    try:
        reaction_coeffs.arr(107,'103',102)
    except TypeError as err:
        assert(type(err) == TypeError)

def test_arr_types3():
    try:
        reaction_coeffs.arr(107,103,[102])
    except TypeError as err:
        assert(type(err) == TypeError)  
        
#Test mod_arr
def test_mod_arr():
    assert reaction_coeffs.mod_arr(107,103,0.5,102) == 957.05129266439894
    
def test_mod_arr_values1():
    try:
        reaction_coeffs.mod_arr(-1,103,0.5,102)
    except ValueError as err:
        assert(type(err) == ValueError)

def test_mod_arr_values2():
    try:
        reaction_coeffs.mod_arr(107,103,0.5,-2)
    except ValueError as err:
        assert(type(err) == ValueError)
        
def test_mod_arr_types1():
    try:
        reaction_coeffs.mod_arr('107',103,0.5,102)
    except TypeError as err:
        assert(type(err) == TypeError)
        
def test_mod_arr_types2():
    try:
        reaction_coeffs.mod_arr(107,'103',0.5,102)
    except TypeError as err:
        assert(type(err) == TypeError)

def test_mod_arr_types3():
    try:
        reaction_coeffs.mod_arr(107,103,[0.5],102)
    except TypeError as err:
        assert(type(err) == TypeError)

def test_mod_arr_types4():
    try:
        reaction_coeffs.mod_arr(107,103,0.5,False)
    except TypeError as err:
        assert(type(err) == TypeError)
    

test_const()
test_mod_arr()
test_arr()
test_arr_values1()
test_arr_values2()
test_arr_types1()
test_arr_types2()
test_arr_types3()
test_mod_arr_values1()
test_mod_arr_values2()
test_mod_arr_types1()
test_mod_arr_types2()
test_mod_arr_types3()
test_mod_arr_types4()