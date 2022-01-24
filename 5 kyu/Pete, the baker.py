def cakes(recipe, available):
    return min([available[i] // recipe[i] if i in available else 0 for i in recipe])



    #two dictionaries recipe and available
    #1 iterate through the keys in recipe
    #2 check if key exists in available
    #for the key with smallest value in available, use floor division to get smallest amount Pete can bake
    #  
   
'''
    for key in recipe.keys():
        if key not in available:
            return 0
        numofcakes = min([available[key] // val for key, val in recipe.items()]) 
    return numofcakes


# or using a ratio might do it



    if len(recipe) > len(available):
        return 0
    else: 
        ratio = []
        for ingredient in recipe:
            ratio.append(int(available[ingredient]/recipe[ingredient]))
        return min(ratio)

''' 



    
