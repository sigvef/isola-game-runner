isola-game-runner
=================

Runs an isola game between to AI bots.

Usage:
```
python isola.py "some runnable command for player 1" "some runnable command for player 2"
```

Example using input_bot:
```
python isola.py "python input_bot.py" "python input_bot.py"
```

Bots are called with two args: a single character denoting which player they are, and a 7*7 string representing the board.
The board representation uses ```X``` and ```O``` for players, ```-``` for squares, and ``` ``` (a space) for empty spaces. 
