# Environment Reference

This reference contains:
 1. explanation of the game
 2. an overview of the available directories
 3. the observations of each agent
 4. the actions each agent can do
 5. the parameters needed to run the game
 6. possibly useful details about the game

## The game explained:

* Every battle starts on a randomly drawn symmetric 11x11 grid (`board'). There are four agents, one in each of the corners. An agent's teammate (if applicable) will be on the kitty corner.
* The board is randomly constructed before each battle and, besides the agents, contains wood walls and rigid walls. We guarantee that the agents will have an accessible path to each other, possibly through wooden walls.
* Rigid walls are indestructible and impassable.
* Wooden walls can be destroyed by bombs (see below). Until they are destroyed, they are impassable. After they are destroyed, they become either a passage or a power-up.
* In any given turn, an agent can choose from one of six actions:
  * Stop (0): This action is a pass.
  * Up (1): Move up on the board.
  * Left (2): Move left on the board.
  * Down (3): Move down on the board.
  * Right (4): Move right on the board.
  * Bomb (5): Lay a bomb.
  * If there is communication, each agent additionally emits a message on each turn consisting of two words from a dictionary of size eight. These words will be given to its teammate in the next step as part of the observation.
* The agent starts with one bomb ("ammo"). Every time it lays a bomb, its ammo decreases by one. After that bomb explodes, its ammo will increase by one.
* The agent also has a blast strength (starts at three). Every bomb it lays is imbued with the current blast strength, which is how far in the vertical and horizontal directions that bomb will effect.
* A bomb has a life of 10 time steps. After its life expires, it explodes and any wooden walls, agents, power-ups or other bombs in its range (given by the blast strength) are destroyed.
* Power-Ups: Half of the wooden walls have power-ups hidden underneath them that are revealed when they are destroyed. These are:
  * Extra Bomb: Picking this up increases the agent's ammo by one.
  * Increase Range: Picking this up increases the agent's blast strength by one.
  * Can Kick: Picking this up allows an agent to kick bombs. It does this by running into them. They then travel in the direction that the agent was moving at a speed of one unit per time step until they are impeded either by a player, a bomb, or a wall.
* The game ends when three out of four players have been destroyed. The winner team is of course the remaining player.
* Ties can happen when the game does not end before the max steps or if multiple agents are destroyed on the same turn. If this happens in a competition, we will rerun the game once.        

## Directory Overview:

* agents: Baseline agents will reside here in addition to being available in the Docker directory. 
* characters.py: Here lies the actors in the game. This includes Agent, Bomb, and Flame.
* configs.py: This configs module contains the setup. Feel free to edit this in your local directory for easy game loading.
* envs (module):
  * utility.py has shared Enums, constants, and common functions to the different environments.
  * v0.py: This environment is the base one that we use. 
  * v1.py: This is a modification of v0.py that collapses the walls in order to end the game more quickly.
  * v2.py: This is a modification of v0.py that adds in communication. It works by having the agents send a message as part of their actions and then includes that message in the next turn of observations.

## Agent Observations

Each agent sees:
  * Board: The 11x11 board is a numpy array where each value corresponds to one of the representations below. The first element in this 2D array corresponds to the configuration of topmost row of the board and so on.
    * Passage = 0
    * Rigid Wall = 1
    * Wooden Wall = 2
    * Bomb = 3
    * Flames = 4
    * Fog = 5: This is only applicable in the partially observed (2v2 Team Radio) setting.
    * Extra Bomb Power-Up = 6: adds ammo.
    * Increase Range Power-Up = 7: increases the blast_strength
    * Can Kick Power-Up = 8: can kick bombs by touching them.
    * AgentDummy = 9
    * Agent0 = 10
    * Agent1 = 11
    * Agent2 = 12
    * Agent3 = 13
  * Position: A tuple of Ints of (X position, Y position)
  * Ammo: An Int representing the amount of ammo this agent has. 
  * Blast Strength: An Int representing the blast strength of this agent's bombs.
  * Can Kick: Whether this agent can kick bombs. This ability is gained by stepping on the can kick power-up.
  * Teammate: One Int in [9, 13].  Which agent is this agent's teammate. In the FFA game, this is the AgentDummy.
  * Enemies: A list of three Ints, each in [9, 13]. Which agents are this agent's enemies. There are three here to be amenable to all variants of the game. When there are only two enemies like in the team competitions, the last Int will be the AgentDummy to reflect the fact that there are only two enemies.
  * Bomb Blast Strength: An 11x11 numpy int array representing the bombs' blast strengths in the agent's view. Everything outside of its view will be fogged out.
  * Bomb Life: An 11x11 numpy int array representing the bombs' life in the agent's view. Everything outside of its view will be fogged out.


![Pommerman-enviroment Output](./assets/pom_env_output.png) *This is the output from env.step()*  

## Agent Actions:

* Each agent's actions are:
  * Movement: a single integer in [0, 5] representing which of the six actions that agent would like to take of the following
    * Stop (0): This action is a pass.
    * Up (1): Move up on the board.
    * Down (2): Move down on the board.
    * Left (3): Move left on the board.
    * Right (4): Move right on the board.
    * Bomb (5): Lay a bomb.
        

## Parameters
There are two parameters for `pommerman.make`: Configuration and Agent.

### Configurations
Pommerman is a play on Bomberman. Multiple game configurations are possible in Pommerman. In the battle we will use the PommeFFACompetition-v0 configuration. However, feel free to use the other configurations during the training period. This can be set using the `config_id` parameter of `pommerman.make` as a String. The possibilities are:   

* `PommeFFACompetition-v0` - In this all agents are against each other  
* `PommeTeamCompetition-v0` - In this teams of two agents each are set against each other. The teams are [Agent0, Agent2] and [Agent1, Agent3]  
* `OneVsOne-v0` - In this two agents are against each other  
* `PommeFFA-v1` - In this all agents are against each other while the board collapses uniformly by replacing the outermost square with walls  
* `PommeTeamCompetition-v1` - This is similar to PommeFFA-v1 but with Teams instead of being Free-For-All  
* `PommeRadio-v2` - This is similar to `PommeTeamCompetition-v0` but the agents can send a list of two integers in the range [1, 8] to their teammates on every turn.



### Agents
There are already some example agents included in the repository. Those can be used for inspiration, or to test your agent against. This is the `agent_list` parameter of `pommerman.make` as a list of 4 agent classes. All of these can be found under `pommerman.agents`:  

* `base_agent` - This is the class that all agents inherit from   
* `random_agent` - This randomly selects an action and plays it out  
* `simple_agent` - This is an agent based on a non-ML approach (This agent is prone to killing itself)   
* `tensorforce_agent` - This agent calls [TensorForce](https://github.com/reinforceio/tensorforce) to return an action  
* `player_agent` - This is an agent controlled by an keyboard. You can change the control scheme by feeding the `agent_control` parameter as either: `"arrows"` for Arrows = Move and Space = Bomb or `"wasd"` for W,A,S,D = Move, E = Bomb  
* `http_agent` - This agent outputs to accepts input in the form of a REST requests to it  
* `docker_agent` - This agent outputs and accepts inputs to an agent wrapped inside a Docker container  

## Useful information
1. Two agents cannot move to the same cell. They will bounce back to their prior places if they try. The same applies to bombs. If an agent and a bomb both try to move to the same space, then the agent will succeed but the bomb will bounce back.
2. If an agent with the can_kick ability moves to a cell with a bomb, then the bomb is kicked in the direction from which the agent came. The ensuing motion will persist until the bomb hits a wall, another agent, or the edge of the grid. 
3. When a bomb explodes, it immediately reaches its full blast radius. If there is an agent or a wall in the way, then it prematurely ends and destroys that agent or wall. 
4. If a bomb is in the vicinity of an explosion, then it will also go off. In this way, bombs can chain together.
5. The SimpleAgent is very useful as a barometer for your own efforts. Four SimpleAgents playing against each other have a win rate of ~18% each with the remaining ~28% of the time being a tie. Keep in mind that it **can** destroy itself. That can skew your own results if not properly understood.

## Request example
```json
{
    "obs": {
        "alive": [
            10,
            11,
            12,
            13
        ],
        "board": [
            [
                0,
                0,
                2,
                1,
                1,
                0,
                1,
                1,
                2,
                2,
                2
            ],
            [
                0,
                10,
                0,
                0,
                2,
                2,
                2,
                0,
                0,
                13,
                2
            ],
            [
                2,
                0,
                0,
                1,
                2,
                2,
                2,
                2,
                0,
                0,
                1
            ],
            [
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                1
            ],
            [
                1,
                2,
                2,
                0,
                0,
                1,
                1,
                1,
                1,
                2,
                1
            ],
            [
                0,
                2,
                2,
                0,
                1,
                0,
                1,
                0,
                0,
                2,
                1
            ],
            [
                1,
                2,
                2,
                0,
                1,
                1,
                0,
                1,
                2,
                2,
                1
            ],
            [
                1,
                0,
                2,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                2
            ],
            [
                2,
                0,
                0,
                1,
                1,
                0,
                2,
                0,
                0,
                0,
                2
            ],
            [
                2,
                11,
                0,
                0,
                2,
                2,
                2,
                0,
                0,
                12,
                0
            ],
            [
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                0,
                0
            ]
        ],
        "bomb_blast_strength": [
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ]
        ],
        "bomb_life": [
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ]
        ],
        "bomb_moving_direction": [
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ]
        ],
        "flame_life": [
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ],
            [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
            ]
        ],
        "game_type": 1,
        "game_env": "pommerman.envs.v0:Pomme",
        "position": [
            1,
            9
        ],
        "blast_strength": 2,
        "can_kick": false,
        "teammate": 9,
        "ammo": 1,
        "enemies": [
            10,
            11,
            12
        ],
        "step_count": 0
    },
    "action_space": "6"
}
```
