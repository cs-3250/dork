"""THE GAME DICTIONARY
"""
__all__ = ['MOVEMENT', 'ACTION']

MOVEMENT = {'north': 'You have moved north',
            'n': 'You have moved north',
            'east': 'You have moved east',
            'e': 'You have moved east',
            'south': 'You have moved south',
            's': 'You have moved south',
            'west': 'You have moved west',
            'w': 'You have moved west'
            }

ACTION = {'jump': 'you have jumped',
          'run': 'You have ran',
          'cry': 'You started crying',
          'go': MOVEMENT,
          'help': 'usage: your damn mom'
          }

if __name__ == "__main__":
    pass
