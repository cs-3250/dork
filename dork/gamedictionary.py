"""THE GAME DICTIONARY
"""
__all__ = ['MOVEMENT', 'ACTION']

MOVEMENT = {'north': 'You have moved north',
            'east': 'You have moved east',
            'south': 'You have moved south',
            'west': 'You have moved west'
            }

ACTION = {'jump': 'you have jumped',
          'run': 'You have ran',
          'cry': 'You started crying',
          'movement': MOVEMENT,
          'go': MOVEMENT,
          }

if __name__ == "__main__":
    pass
