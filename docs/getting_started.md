# Getting Started
## Pre-requisites
* [Python 3.6.0](https://www.python.org/downloads/release/python-360/)+ (including `pip`)
* [Docker](https://www.docker.com/) (needed for `DockerAgent`)

## Installation
* Clone the repository
```
$ git clone https://dev.azure.com/corpinfosupportdev/_git/Pommerman
```
* **OPTIONAL**: Setup an isolated virtual Python environment by running the following commands
```
$ python3 -m venv ./venv
```
This environment needs to be activated for usage. Any package installations will now persist
in this virtual environment folder only. (For linux, replace `Scripts` with `bin`). 
```
$ ./venv/Scripts/activate
```
* Install the `pommerman` package. This needs to be done every time the code is updated to get the
latest modules
```
pip install .
```
* Run your first game
```
python examples/simple_ffa_run.py
```

### Running a Docker Agent
The above example can be extended to use **DockerAgent** instead of a **RandomAgent**. The code in examples/docker-agent/run.py wraps a **SimpleAgent** inside Docker.  
* We will build a docker image with the name `pommerman/simple-agent` using the `Dockerfile` provided.
```shell
$ docker build -t pommerman/simple-agent -f examples/docker-agent/Dockerfile .
```

* The agent list used in simple_ffa_run.py can now be updated. Note that a `port` argument (of an unoccupied port) is
needed to expose the HTTP server.
```python
agent_list = [
    agents.SimpleAgent(),
    agents.RandomAgent(),
    agents.SimpleAgent(),
    agents.DockerAgent("pommerman/simple-agent", port=12345)
]
```
You should now be able to run the game with the example docker agent, using simple_ffa_run.py. 

## Running your own agent
1. Implement your own agent that can observe the environment and respond with its next action. Make sure this agent runs inside a docker container. Examples are available in C# (clone the [PommermanDotNet Repository](https://dev.azure.com/corpinfosupportdev/Pommerman/_git/PommermanAgentDotNet)) and python (examples/docker-agent). 
2. Build the docker image
3. Run the game with your own docker agent. In simple_ffa_run.py, replace one or multiple of the agents with your docker agent: 
```
agents.DockerAgent(<docker-image>, port=<port>)
```
The container starts itself when this script is called. 

## Playing an interactive game
You can also play the game! See below for an example where one **PlayerAgent** controls with the `Arrow` keys and the other with the `WASD` keys.
```python
#!/usr/bin/python
agent_list = [
    agents.SimpleAgent(),
    agents.PlayerAgent(agent_control="arrows"), # Arrows = Move, Space = Bomb
    agents.SimpleAgent(),
    agents.PlayerAgent(agent_control="wasd"), # W,A,S,D = Move, E = Bomb
]
```

## CLI
You can also run pommerman using the CLI. See [CLI](CLI.md) for more information and examples.