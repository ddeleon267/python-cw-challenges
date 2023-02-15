def well(ideas):
    good_ideas = ideas.count('good')
    if good_ideas > 2:
        return "I smell a series!"
    elif good_ideas == 0:
        return "Fail!"
    else:
        return "Publish!"