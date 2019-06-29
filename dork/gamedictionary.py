"""THE GAME DICTIONARY
"""
__all__ = ['MOVEMENT', 'ACTION', 'PICK']

MOVEMENT = {'north': 'You have moved north',
            'n': 'You have moved north',
            'east': 'You have moved east',
            'e': 'You have moved east',
            'south': 'You have moved south',
            's': 'You have moved south',
            'west': 'You have moved west',
            'w': 'You have moved west'
            }

PICK = {'up': "nothing picked up you have nowhere to put it"
        }

ACTION = {'jump': 'you have jumped',
          'run': 'You have ran',
          'cry': 'You started crying',
          'go': MOVEMENT,
          'help': 'usage: your damn mom',
          'load': "can't load at the moment",
          'save': "can't save at the moment",
          'pick': PICK
          }

if __name__ == "__main__":
    pass
