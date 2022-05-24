# Competition
## Submitting an Agent
Agents should be submitted in our Docker registry: 
1. Install Azure CLI
2. `az login`. Let op: als het goed is logt dit in op de Info Support Corporate Development tenant.
3. `az acr login --name acrcicdpommweu001`
4. `docker login`


## Rules and Submission

1) Each submission should have a Docker file per agent. Teams can submit multiple agents. Instructions and an example for building Docker containers from trained agents can be found in our repository.

2) The positions for each agent will be randomized.

3) The agents should follow the prescribed convention specified in our example code and expose an "act" endpoint that accepts a dictionary of observations. Because we are using Docker containers and http requests, we do not have any requirements for programming language or framework. There will be ample opportunity to test this on our servers beforehand.

4) If an agent has a bug in its software that causes its container to crash, that will count as a loss for that agent's team.

5) The expected response from the agent will be a single integer in [0, 5] representing which of the six actions that agent would like to take.

6) If an agent does not respond in an appropriate time limit (100ms), then we will automatically issue them the Stop action.

7) Agents submitted by organizers can participate in the competitions but are not eligible for prizes. They will be excluded from consideration in the final standings.
