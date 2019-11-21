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
   
   
Exploitation Vs Exploration
===========================
The story of "epsilon" is called Exploitation (exploration factor) is part of Q-LEARNING story :

1. The main objective of Q-training is to develope a policy  π  for navigating the maze successfully. Presumably, after playing hundreds of games, the agent (rat in our case) should attain a clear deterministic policy for how to act in every possible situation. Which action to take in every possible maze state?
2. The term policy should be understood simply as a function  π  that takes a maze snapshot (envstate) as input and returns the action to be taken by the agent (rat in our case). The input consists of the full nxn maze cells state and the rat location
			next action=π(state)
3. At start, we simply choose a completely random policy. Then we use it to play thousands of games from which we learn how to perfect it. Surely, at the early training stages, our policy  π  will yield lots of errors and cause us to lose many games, but our rewarding policy should provide feedback for it on how to improve itself. Our learning engine is going to be a simple feed-forward neural network which takes an environment state (maze cells) as input and yields a reward per action vector (see later for better description)
4. In order to enhance the Q-learning process, we shall use two types of moves:

Exploitation: these are moves that our policy  π  dictates based on previous experiences. The policy function is used in about 90% of the moves before it is completed.
Exploration: in about 10% of the cases, we take a completely random action in order to acquire new experiences (and possibly meet bigger rewards) which our strategy function may not allow us to make due to its restrictive nature. Think of it as choosing a completey random new restaurant once in a while instead of choosing the routine restaurants that you already familiar with

5. The exploration factor epsilon is the the frequency level of how much exploration to do. It is usually set to 0.1, which roughly means that in one of every 10 moves the agent takes a completely random action. There are however many other usage schemes you can try (you can even tune epsilon during training!)


Markov Decision Process
=======================
A Reinforcement Learning system consists of an environment and a dynamic agent which acts in this environment in finite discrete list of time steps.

1. At every time step  t , the agent is entering a state  s , and needs to choose an action  a  from a fixed set of possible actions. The decision about which action to take should depend on the current state only (previous actions history is irrelevant). This is sometimes reffered to as MDP: Markov Decision Process (or shortly Markov Chain)
2. The result of performing action  a  at time  t  will result in a transition from a current state  s  at time  t  to a new state  s′=T(s,a)  at time  t+1 , and an immediate reward  r=R(s,a)  (numerical value) which is collected by the agent after each action (could be called a "penalty" in case the reward is negative).  T  is usually calle the transition function, and  R  is the reward function:
	s′=T(s,a)
	r=R(s,a)
3. The agent's goal is to collect the maximal total reward during a "game". The greedy policy of choosing the action that yields the highest immediate reward at state  s , may not lead to the best possible total reward as it may happend that after one "lucky" strike all the subsequent moves will yield poor rewards or even penalties. Therefore, selecting the optimal route is a real and difficult challenge (just as it is in life, delayed rewards are hard to get by).
    In the following figure we see a Markov chain of 5 states of a rat in a maze game. The reward for every legal move is  −0.04  which is actually a "small penalty". The reason for this is that we want to minimize the rat's route to the cheese. The more the rat wonders around and wastes time, the less reward he gets. When the rat reaches the cheese cell, he gets the maximal reward of  1.0  (all rewards are ranging from  −1.0  to  1.0 
4. If our agent takes the action sequence (starting at state  s1  till the game end):  a1 ,  a2 ,  a3 , ...,  an , then the resulting total reward for this sequence is
     A=R(s1,a1)+R(s2,a2)+⋯+R(sn,an)
 
Our goal is to find a policy function π that maps a maze state s to an "optimal" action a that we should take in order to maximize our total reward A. The policy π tells us what action to take in whatever state s we are in by simply applying it on the given state s

		action=π(s)
		
5. Once we have a policy function  π , all we need to do is to follow it blindly
a1=π(s1)
s2=T(s1,a1)
a2=π(s2)
....
an=π(sn−1)
 

