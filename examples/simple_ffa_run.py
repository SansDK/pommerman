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
        # agents.SimpleAgent(),
        # agents.DockerAgent("twaiger-agent", port=5000),
        agents.PlayerAgent(agent_control="arrows"),
        # Bottom left
        # agents.SimpleAgent(),
        agents.DockerAgent("python-docker-agent", port=5001)
    ]
    # Make the "Free-For-All" environment using the agent list
    env = pommerman.make('PommeFFACompetition-v0', agent_list)

    print('states: {}'.format(env.observation_space.shape[0]))
    print('actions: {}'.format(env.action_space.n))

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
