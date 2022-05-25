'''An example to show how to set up a Bombersauce game programmatically'''
import pommerman
from pommerman import agents


def main():
    '''Simple function to bootstrap a game.
       
       Use this as an example to set up your training env.
    '''
    # Print all possible environments in the Pommerman registry
    print(pommerman.REGISTRY)

    # Create a set of agents (exactly four)
    agent_list = [
        # Top left
        agents.SimpleAgent(),
        # Top right
        agents.RandomAgent(),
        # Bottom right
        agents.DockerAgent("my-bombersauce-agent-in-aspnetcore", port=5000),
        # Bottom left
        agents.DockerAgent("python-docker-agent", port=5001)
    ]
    # Make the "Free-For-All" environment using the agent list
    env = pommerman.make('PommeFFACompetition-v0', agent_list)

    # Run the episodes
    for i_episode in range(1):
        state = env.reset()
        done = False
        while not done:
            env.render()
            actions = env.act(state)
            state, reward, done, info = env.step(actions)
        print('Episode {} finished'.format(i_episode))
    env.close()


if __name__ == '__main__':
    main()
