# Docker

To be able to run the agents of all teams smoothly, we use Docker. You should make a Docker image of your agent. This means that you will create a web server that implements the Bombersauce API, and run that web server in a Docker container.

To make this work, here are a few important notes:
- The Bombersauce client (i.e. the Python program that runs the competition) will communicate with Docker to start all the necessary containers.
- Your web server is assumed to run on port 5000 within the Docker container. The Bombersauce client will map this port to a port outside Docker.
- You may make your implementation as complex as you want, but each agent must respond to API calls within a limited time frame. If it is too late, the agent will not perform any action.
- You may want to save data on the file system outside Docker; for example, to remember the stuff your agent learned while training. Here is how that works:
  - The Bombersauce agent will instruct Docker to map the `/data` directory *inside* the container to the `C:\temp\bombersauce\your-image-name` directory *outside* the container.
  - If you develop on a non-Windows OS, you probably won't have the `C:` directory, so you will have to change that path in the Bombersauce code.
  - In your submission, please submit a standalone Docker image that no longer needs the file system outside Docker. If this really won't work for you, please contact us so that we can find a solution. 

If you have any questions, please don't hesitate to ask.
