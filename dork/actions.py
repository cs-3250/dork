# example of handling an action
# okay to rename and rewrite 'go'
# okay to add other functions here too

def go(*args, **kwargs):
    if 'adverbs' in kwargs:
        print("Went " + ' '.join([str(adv) for adv in kwargs['adverbs']]) + '!')
    elif 'to' in kwargs:
        print("Went to " + ' '.join([str(adv) for adv in kwargs['to']]) + '!')
    else:
        print("Go where?")


def pick_up(*args, **kwargs): # example of a phrasal verb
    print("Picked it up!")
