
def progress_rate(v1,x,k):
    #Check that x and v1 are lists
    if (type(v1) != list or type(x) != list):
        raise TypeError("v' & x must be passed in as a list")
    #Check that x,and k are numbers/list of numbers
    if (any(type(i) != int and type(i) != float for i in x)):
        raise TypeError("All elements in x must be numbers!")
    elif (type(k) != int and type(k) != float and type(k) != list):
        raise TypeError("k must be a numbers or list!")
    else:
        progress_rates = []
        #check for multiple reactions
        if(type(v1[0]) == list):
            for v in v1:
                for reactant in v:
                    if(type(reactant) != int and type(reactant) != float):
                        raise TypeError("All elements in v1 must be numbers!")
            #Calculate the progress rate of each reaction
            reactions = len(v1[0])
            for j in range(reactions):
                if (type(k) == list):
                    progress_rate = k[j]
                else:
                    progress_rate = k
                for i in range(len(v1)):
                    progress_rate = progress_rate*(x[i]**v1[i][j])
                progress_rates.append(progress_rate) 
        else:
            #Check types of V1
            if (any(type(i) != int and type(i) != float  for i in v1)):
                raise TypeError("All elements in v1 must be numbers!")
            #Calculate the progress rate of each reaction
            progress_rate = k
            for i in range(len(v1)):
                progress_rate = progress_rate*(x[i]**v1[i])
            progress_rates.append(progress_rate)
        return progress_rates
    
def reaction_rate(v1,v2,x,k):
    w = progress_rate(v1,x,k)
    #Check that x,v2 and v1 are lists
    if (type(v2) != list or type(x) != list or type(v1)!= list):
        raise TypeError("v' & x must be passed in as a list")
    if (any(type(i) != int and type(i) != float for i in x)):
        raise TypeError("All arguments must be numbers!")
    elif (type(k) != int and type(k) != float and type(k) !=list):
        raise TypeError("All arguments must be numbers!")
    else:
        reaction_rates = []
        for i in (range(len(v2))):
            reaction_rate = 0
            for j in (range(len(v2[0]))):
                reaction_rate = reaction_rate + (v2[i][j]-v1[i][j])*w[j]
            reaction_rates.append(reaction_rate)
        return reaction_rates