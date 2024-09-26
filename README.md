# Tuto

This a tuto for some concepts that I study as a 3rd year engineering student





## 1. Docker

# To Add
- [ ] Complete Docker Hub tuto

**Resources :**
* docker for begineers : https://docker-curriculum.com/
* A siple docker tutoriel youtube : https://www.youtube.com/watch?v=zkMRWDQV4Tg

### What is docker
Docker is a tool that allows developers, sys-admins etc. to easily deploy their applications in a sandbox (called containers) to run on the host operating system i.e. Linux. The key benefit of Docker is that it allows users to **package an application with all of its dependencies into a standardized unit** for software development. Unlike virtual machines, containers do not have high overhead and hence enable more efficient usage of the underlying system and resources.

### Working with docker
#### 1. Creating a Docker file
A file provided to set the instruction for creating a **docker image**, it contains some instructions like : `FROM python:latest`
Look up [Dockerfile exemple](DockerTuto/Dockerfile)


#### 2. Creating a container
After creating the **Dockerfile**, here’s how to proceed to build and run a Docker container :
1. Build the Docker Image :
    Open your terminal (or command prompt) and navigate to the directory containing the Dockerfile. Then, run the following command to build the Docker image: `docker build -t my-python-app .`
    
    * `-t my-python-app` : This tags the image with the name my-python-app.
    * `.` : This specifies the build context, which is the current directory Docker will use the files in this directory to build the image.

2. Verify the Image
    Once the image is built, you can list your Docker images to ensure the build was successful : `docker images`


3. Run the Docker Container from the image
    Once the image is built, you can run a container from it with the following command: `docker run -d -p 80:80 my-python-app`

    * `-d` : Runs the container in detached mode (in the background).
    * `-p 80:80` : Maps port 80 of your host machine to port 80 of the container. This means you can access the application via http://localhost on your host machine.
    * `my-python-app` : This is the name of the image you just built.
    * `--name <container-name>`(Optionnal): Assigns a name to the running container for easier reference.

4. Check Running Containers
    You can verify if the container is running by listing all active containers: `docker ps`

5. Interact with the Running Container
    You can enter the running container's shell to inspect it further:`docker exec -it <container-name> /bin/bash`
    This opens an interactive terminal session inside the container.

6. Stop and Remove Containers
    Once you're done with the container, you can stop it: `docker stop <container-name>`

    To remove it: `docker rm <container-name>`


7. Push the Docker Image to a Registry (Optional)
If you want to share your image or deploy it on another server, you can push it to a Docker registry like [Docker Hub](https://hub.docker.com/)  or a private registry.







