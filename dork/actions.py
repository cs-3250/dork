# example of handling an action
# okay to rename and rewrite 'go' - just be sure to update dictionary in cli.py to match
# okay to add other functions here too
    # just make sure to manually add function name & aliases to dict in cli.py for now

def go(*args, **kwargs):
    if 'adverbs' in kwargs:
        print("Went " + ' '.join([str(adv) for adv in kwargs['adverbs']]) + '!')
    elif 'to' in kwargs:
        print("Went to " + ' '.join([str(adv) for adv in kwargs['to']]) + '!')
    else:
        print("Go where?")
