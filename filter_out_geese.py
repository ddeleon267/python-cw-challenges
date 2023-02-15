geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

#verbose
def goose_filter(birds):
    not_geese = []
    for birdie in birds:
        if birdie not in geese:
            not_geese.append(birdie)
    
    return not_geese

# if you want to use list comprehension
def goose_filter(birds):    
    return [birdie for birdie in birds if birdie not in geese]  
    