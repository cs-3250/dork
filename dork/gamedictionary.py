"""THE GAME DICTIONARY
"""
__all__ = ['MOVEMENT', 'ACTION', 'get_action']

MOVEMENT = {'north' : 'You have moved north',
            'east' : 'You have moved east',
            'south' : 'You have moved south',
            'west' : 'You have moved west'
           }

ACTION = {'jump' : 'you have jumped',
          'run' : 'You have ran',
          'cry' : 'You started crying'
         }

def get_action():
    '''can't import, might as well pass it'''
    return ACTION

if __name__ == "__main__":
    pass
