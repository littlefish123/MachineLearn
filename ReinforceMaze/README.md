Reinforcement Learning by resolving MAZE game
=============================================
What is Reinforcement Learing ?

Reinforcement Learnng is a machine learning technique by a feedback system (penalites and reward) applied on an AGENT under a predefined ENVIRONMENT. It moves through a series 
of states in order to reach a pre-defined target final state. This MAZE game is a rat (agent) which is trying to find the shortest route to get the cheese in a maze (ENVIRONMENT).
The agent is EXPERIMENTING and EXPLOITING past experiences (episodes) in order to achieve the goal. With subsequent fail trail and error (REWARDS and PENALITES), it will arrive
the solution of a problem. 

The solution will be reached if the agent finds the optimal sequence of states in which the ACCUMATED SUM OF REWARDS is maximal. In order to reach the goal, the agent 
need to encounter many penalites (negative reward. In this game, the rat in the maze get a small penality for each legal move because we want to get the cheese in the shortest 
possible path. Conversely, the shortest path to the target cheese cell is sometimes long and winding, and our agent have to endure many penalities.

Maze Game
=========
A simple maze consists of a rectangular grid of cells, a rat and "cheese" cell.

1. Use small 7x7, 8x8 and 10x10 mazes
2. The cheese is always at the bottom right cell of the maze
3. Two type of cell : free cell (white) and occupied cell(black)
4. The rat starts from any cell and is allowed to travel on free cells only.

https://www.samyzaf.com/ML/rl/qmaze.html

Environment
===========
A framework from Markov Decision Process consists of an environment and an agent. There are 3 types of cells in the maze :
1. Occupied Cells
2. Free Cells
3. Target Cell

In our model, the rat will be encouraged to find the shortest path to the target cell by rewarding scheme with following 4 actions :
1. 0- LEFT
2. 1-UP
3. 2-RIGHT
4. 3-DOWN

a. Rewards will be floating points ranging from -1.0 to 1.0
b. Each move from one state to another will be rewarded (the rat get points) by a positve or negative (penalty).
c. Each move will cost the rate -0.04 points. This should discourage the rat from wandering around and get to the cheese in the shortest route.
d. The maximum reward of 1.0 points is given when the rat hits the cheese.
e. An attempt to enter the bloaked cell will cost -0.75 points.	 The rate will learn how to avoid this penality.
f. Same rule hold for an attemp to move outside the boundary of maze.
g. The rate will be penilized by -0.25 points for any move to a cell which it has already visited before.
h. To avoid infinite loops and senseless wandering, the game will ended (**lose**) once the total reward of the rat is below the negative 
   threshold (-0.5 * maze.size). The rat has lost its way and alredy made too many errors.
   
   