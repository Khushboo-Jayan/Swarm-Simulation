# Swarm-Simulation
Robot swarm simulation NUI Gawlay

Swarms

##What is a Swarm and Swarm Intelligence?

A swarm in AI is an application of group behavior of living organisms in the ecosystem for example ‘School of fish’, ‘Flock of sheep’. These animals always stay together in form of groups usually following a leader, this process of solving the problems in groups and making decisions is referred to as ‘Swarm Intelligence SI’, SI supports the idea that ‘collective minds are better than one’. These groups emerge with the motive of survival and evolution. 

However, in this paper is based on swarm robots where each robot has sensing and communication ability and the interaction among the robots lead to a solution of a task at each stage. 

Task 1 – Explore the existing simulators 

Task 2 – Create an environment

Task 3 -Study how the agents will work. 

##Explore the existing Simulators

I read multiple articles available on the web and the most frequently discussed simulators were Webots and ARGoS. Webots was used for a single robot whereas ARGoS was used for swarm of robots and how they interact with each other, the problem faced with ARGoS  was that it runs on Linux and Mac only; I tried using virtual VM box but it made the machine really slow and difficult to deal with. 


##Development

Our aim was to build a simulator of our own. For which we imagined an N*N matrix where each robot can have a specific location (i,j) and capability to move one cell at a time. To create an environment, I used processing in JAVA. 

First of all, I started with the development of grid imagining each box as a possible location of the robot similar to as a chess board. 

![image](https://user-images.githubusercontent.com/79542266/191874927-bc827646-bcc7-48ee-aa43-901ba1317a42.png)

Secondly, I started placing the robots in form of stars that will move based on the key entered ‘A,S,D,W’ to ‘West, South, East, North’ respectively.

![image](https://user-images.githubusercontent.com/79542266/191874952-fdb28286-6307-45ca-9e7a-349dedb9067c.png)

Later I discovered that the movement of robots would not be restricted to a certain block instead it will move on continuous X and Y co-ordinate on the surface. Hence, I plotted multiple robots on the 

![image](https://user-images.githubusercontent.com/79542266/191874974-c945f20d-548d-44d8-b9d6-ec72288ae781.png)

Sample visualization of predator:

![image](https://user-images.githubusercontent.com/79542266/191875040-1a2bac07-0176-42bd-aa30-a90b52725a27.png)

##Working

In this paper is based on swarm robots where each robot has sensing and communication ability and the interaction among the robots lead to a solution of a task. Consider in the beginning the agents are moving randomly

Action rules governing the movement of bots:
1.	Assume that each bot can communicate and sense another bot within a range of S.
2.	If another is not detected, then the bots move randomly within the matrix. 
3.	If the bots are next to each other than no movement.
4.	If another bot is detected, then the two move towards each other and form a group 

Predator behavior rules:

1.	A predator whose role is to move towards the cluster. 
2.	The bots should move in the opposite direction of the predator but towards the bots. 

Currently we are working on application of action and predator rules for agents.  


