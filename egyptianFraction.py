def egyptianFraction(num, de, res):
    #numerator be bigger than denominator? no
    #numerator be 0?
    
    #4/13 ---> 1 / (13 / 4)
    # 1/something + new_fraction         ---> new_fraction < the fraction before that
    # something = (13/4) ceiling of the value ---> 4 
    # new_fraction = original_fraction - 1 / something
    
    #num == 1 ---> stop recursing and append that to res
    #num = 0 ---> not gonna do anything and stop there
    
    if num == 1:
        res.append("{0} / {1}".format(num,de))
        return
    if num == 0:
        return    
    
    #new_fraction = num/den - 1/something
    #new_fraction_num = original_fraction_num * something - 1 * original_fraction_denominator
    #new_fractional_den = something * original_fraction_denominator
    #check if new_fraction_den % new_fraction_numerator == 0
    #if it is then it's gonna be reduced down to 1 / new_fraction_den / new_fraction_den

    import pdb; pdb.set_trace()
    something = de // num + 1
    new_numerator = num * something - de
    new_den = something * de

    if new_den % new_numerator == 0:
        new_den = new_den // new_numerator
        new_numerator = 1

    res.append("{0} / {1}".format(1, something))
    egyptianFraction(new_numerator, new_den, res)
    
    
    




    pass

if __name__ == "__main__":
    res = []
    egyptianFraction(4,13, res) #--> [1/4, 1/18, 1/468]
    print(res)