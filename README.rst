Read Me
=======

Dork is similar to the 1980 game Zork. A player is able to navigate through rooms in order to finish the story. There is a navigation system in place as well as a command line interface, with a repl and very basic load and save functions.

* Free software: MIT license
* Documentation:

Features
--------

* Added SonarCloud and TravisCI testing
* REPL
  * Accepts [verb] [nown] sentences and navigates between rooms
* Save and load using YAML format
  * Can save rooms

How Do I Start?
--------

* Install
  1. Install python 3+, and git
  2. git clone: https://github.com/cs-3250/dork
  3. pip install requirements-dev.txt and pip install requirements.txt
* Run
  - python -m dork
* Playing the game
  - quit - quits the game
  - load - loads room and item data
  - help - provides basic instructions
* Select play
  - Follow the interactive prompt instructions, use "help"
  - Some indicate what keywords to use
  - Most follow structure
  - When done type in quit
* Developers
  - Currently the game consists of a single map with rooms, there are no development tools or tests.

Credits
-------

Please see the credits provided in the repo or Documentation.
