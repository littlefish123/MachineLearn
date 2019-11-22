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
 
<<<<<<< HEAD
Q-Learning and Bellman Equation
================================
The trick that was used by startups such as Google DeepMind for finding  π  was to start with a different kind of function  Q(s,a)  called best utility function (and sometimes best quality function, from which the Q letter and Q-learning terms were coined).

The definition of  Q(s,a)  is simple:
Q(s,a)=the maximum total reward we can get by choosing action a in state s
 
At least for our maze solving, it is easy to be convinced that such function exists, although we have no idea how to compute it efficiently (except for going through all possible Markov chains that start at state  s , which is insanely inefficient). But it can also be proved mathematically for all similar Markov systems. Look for example in: https://webdocs.cs.ualberta.ca/~sutton/book/ebook/the-book.html

Once we have  Q(s,a)  at hand, finding a policy function is easy!
	π(s)=argmaxi=0,1,…,n−1Q(s,ai)
 
That is: we calculate  Q(s,ai)  for all actions  ai ,  i=0,1,…,n−1  (where  n  is the number of actions), and select the action  ai  for which  Q(s,ai)  is maximal. This is obviously the way to go. But we do not have the function  Q(s,a)  yet ... how do we get it?

It turns out that the function  Q(s,a)  has a simple recursive property which characterizes it, and also helps to approximate it. It is called Bellman's Equation and it is obvious from first sight:
	Q(s,a)=R(s,a)+maxi=0,1,…,n−1Q(s′,ai),(where s′=T(s,a))
 
In simple words: the value  Q(s,a)  is equal to the immediate reward  R(s,a)  plus the maximal value of  Q(s′,aj) , where  s′  is the next state and  ai  is an action.

In addition, Bellman's Equation is also a unique characterization of the best utility function. That is, if a function  Q(s,a)  satisfies the Bellman Equation the it must be the best utility function.

To approximate  Q(s,a)  we will build a neural network  N  which accepts a state  s  as input and outputs a vector  q  of q-values corresponding to our  n  actions:  q=(q0,q1,q2,⋯,qn−1) , where  qi  should approximate the value  Q(s,ai) , for each action  ai . Once the network is sufficiently trained and accurate, we will use it to define a policy, which we call the derived policy, as follows
	q=N[s]
	j=argmaxi=0,1,…,n−1(q0,q1,…,qn−1)
	n(s)=aj
	

Q-Training
==========
The question now is how do we train our neural network  N ? The usual arrangement (as we've seen a lot) is to generate a sufficiently large dataset of  (e,q)  pairs, where  e  is an environment state (or maze state in our case), and  q=(q0,q1,…,qn−1)  are the correct actions q-values. To do this, we will have to simulate thousands of games and make sure that all our moves are optimal (or else our q-values may not be correct). This is of course too tedious, too hard, and impractical in most real life cases.
Deep learning startups (like Google DeepMind) came up with more practical and surprisingly elegant schemes for tackling this problem. We will explore one of them (thanks to Eder Santana post which included a small and clear demonstration).

We will generate our training samples from using the neural network  N  itself, by simulating hundreds or thousands of games. We will exploit the derived policy  π  (from the last section) to make 90% of our game moves (the other 10% of the moves are reserved for exploration). However we will set the target function of our neural network  N  to be the function in the right side of Bellman's equation! Assuming that our neural network  N  converges, it will define a function  Q(s,a)  which satisfies Bellman's equation, and therefore it must be the best utility function which we seek.

The training of  N  will be done after each game move by injecting a random selection of the most recent training samples to  N . Assuming that our game skill will get better in time, we will use only a small number of the most recent training samples. We will forget old samples (which are probably bad) and will delete them from memory.

In more detail: After each game move we will generate an episode and save it to a short term memory sequence. An episode is a tuple of 5 elements that we need for one training:

episode = [envstate, action, reward, envstate_next, game_over]

(a) envstate - environment state. In our maze case it means a full picture of the maze cells (the state of each cell including rat and chees location) To make it easier for our neural network, we squash the maze to a 1-dimensional vector that fits the networks input.

(b) action - one of the four actions that the rat can do to move on the maze:

     0 - left
     1 - up
     2 - right
     3 - down
(c) reward - is the reward received from the action

(d) envstate_next - this is the new maze environment state which resulted from the last action

(e) game_over - this is a boolean value (True/False) which indicates if the game is over or not. The game is over if the rat has reached the cheese cell (win), or of the rats has reached a negative reward limit (lose).

After each move in the game, we form this 5-elements episode and insert it to our memory sequence. In case that our memory sequence size grows beyond a fixed bound we delete elements from its tail to keep it below this bound.

The weights of network  N  are initialized with random values, so in the beginning  N  will produce awful results, but if our model parameters are chosen properly, it should converge to a solution of the Bellman Equation, and therefore later experiments are expected to be more truthful. Currently, building model that converge quickly seems to be very difficult and there is still lots of room for improvements in this issue.


Experience Class
================
The Experience Class
This is the class in which we collect our game episodes (or game experiences) within a memory list. Note that its initialization methods need to get a

model - a neural network model
max_memory - maximeal length of episodes to keep. When we reach the maximal lenght of memory, each time we add a new episode, the oldest episode is deleted
discount factor - this is a special coefficient, usually denoted by  γ  which is required for the Bellman equation for stochastic environments (in which state transitions are probabilistic). Here is a more practical version of the Bellman equation:
	Q(s,a)=R(s,a)+γ⋅maxi=0,…,n−1Q(s′,ai),(where s′=T(s,a))
	
	
Q-Training Algorithm
====================
We define the algorithm for training a our neural network model to solve the maze. It accepts a keyword argument list. Here are the most significant options:
epoch - Number of training epochs
max_memory - Maximum number of game experiences we keep in memory (see the Experince class above)
data_size - Number of samples we use in each training epoch. This is the number episodes (or game experiences) which we randomly select from our experiences repository (again, see the Experience class above)	

Buildng Neural Network
======================
Choosing the correct parameters for a suitable model is not easy and requires some experience and many experiments. In the case of a maze we found that:

The most suitable activation function is SReLU (the S-shaped relu)
Our optimizer is RMSProp
Our loss function is mse (Mean Squared Error).
We use two hidden layers, each of size equals to the maze size. The input layer has also the same size as the maze since it accepts the maze stae as input. The output layer size is the same as the number of actions (4 in our case), since its outputs the estimated q-value for each action. (we need to take the action with the maximal q-value for playing in the game
=======
6. 
>>>>>>> 1344c4a2451a8a3c5c2b39c6e6f7eecbe9abb2f0
