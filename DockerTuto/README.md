# Docker Tuto

**To Add**
- [ ] Docker Hub

**Resources :**
* docker for begineers : https://docker-curriculum.com/
* A smiple docker tutoriel youtube : https://www.youtube.com/watch?v=zkMRWDQV4Tg

## What is docker
Docker is a tool that allows developers, sys-admins etc. to easily deploy their applications in a sandbox (called containers) to run on the host operating system i.e. Linux. The key benefit of Docker is that it allows users to **package an application with all of its dependencies into a standardized unit** for software development. Unlike virtual machines, containers do not have high overhead and hence enable more efficient usage of the underlying system and resources.

<details>
  <summary>More details about Docker(images,containers,...)</summary>

  <details>
    <summary>Docker Image</summary>
    <p>An image is a read-only template that contains the application code, the required system libraries, tools, dependencies, and other configuration settings needed to run the app. It's like a blueprint for building a house: it defines all the materials, design, and components needed but isn’t the actual house.</p>
    <p><strong>Key characteristics of Docker images:</strong></p>
    <ul>
      <li><strong>Static:</strong> Once created, an image doesn't change.</li>
      <li><strong>Portable:</strong> You can share it with others, move it across machines, or deploy it in different environments, and it will behave the same way everywhere.</li>
      <li><strong>Layered:</strong> Images are made up of multiple layers, where each layer represents an instruction in the Dockerfile (e.g., installing dependencies, copying files, etc.). Each time you modify the image, a new layer is added.</li>
    </ul>
    <p><strong>Example of what's inside a Docker image:</strong></p>
    <ul>
      <li>A base operating system (e.g., Linux).</li>
      <li>Installed software or libraries (e.g., Python, Node.js).</li>
      <li>Your application code.</li>
    </ul>
  </details>

  <details>
    <summary>Docker Container</summary>
    <p>A container is a running instance of a Docker image. While the image is just a set of files and configurations, the container is where the actual work happens. When you start a container, Docker takes the image and creates a runnable, isolated environment for your app to execute.</p>
    <p><strong>Key characteristics of Docker containers:</strong></p>
    <ul>
      <li><strong>Isolated:</strong> Containers run in their own environments, separated from other containers and the host machine. This ensures that your app runs without conflicts, even if other apps need different versions of software.</li>
      <li><strong>Ephemeral:</strong> Containers are meant to be lightweight and temporary. You can start, stop, and remove them without affecting the underlying image or other containers.</li>
      <li><strong>Running Process:</strong> Each container has its own process running inside it. When you stop a container, that process is also stopped.</li>
    </ul>
    <p><strong>Example Comparison:</strong></p>
    <p>Think of an image like a recipe for baking a cake, and the container as the baked cake itself:</p>
    <ul>
      <li><strong>Image:</strong> This is the recipe with all the details about ingredients, measurements, and steps (the code, libraries, etc.).</li>
      <li><strong>Container:</strong> This is the actual cake, baked according to the recipe. You can eat the cake (run the container), slice it (stop or restart it), or throw it away (remove the container). But the recipe (the image) stays unchanged, and you can use it to make more cakes (run more containers).</li>
    </ul>
  </details>

  <p><strong>In summary:</strong></p>
  <ul>
    <li><strong>Image:</strong> A static blueprint that defines how to build and configure your app’s environment.</li>
    <li><strong>Container:</strong> A live, isolated instance where your app actually runs, based on the image.</li>
  </ul>
</details>

## Working with docker
### 1. Creating a Docker file

> Check this link for better understanding on the official Docker Webpage : [Dockerfile](https://docs.docker.com/build/concepts/dockerfile/)

A file provided to set the instruction for creating a **docker image**, it contains some instructions like : 

```
# Use a base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install any dependencies
RUN pip install -r requirements.txt

# Specify the command to run the app
CMD ["python", "app.py"]

```

* **Layers**
    In the context of Docker, a layer refers to an immutable file system change or instruction added to the image during the build process. Each command in a Dockerfile (such as `RUN`, `COPY`, or `ADD`) creates a new layer, which is then stacked on top of the previous layers to form the final Docker image.

    *Note that Docker caches each layer and can reuse layers from previous builds if the corresponding instructions haven't changed, and it will run all instruction (rebuild all layer) that comes after the layer where the changes happenned*

    *Note that it's a best practices to minimize the number of layers by running for example multiple commands in the same layer :* `RUN apt-get update && apt-get install -y package1 package2`

Look up [Dockerfile exemple](Dockerfile)

---

### 2. Creating a container from a Docker image
After creating the **Dockerfile**, here’s how to proceed to build and run a Docker container :
1. **Build the Docker Image :**

    Open your terminal (or command prompt) and navigate to the directory containing the Dockerfile. Then, run the following command to build the Docker image:
   ```
   docker build -t my-python-app .
   ```
    
    * `-t my-python-app` : This tags the image with the name my-python-app.
    * `.` : This specifies the build context, which is the current directory Docker will use the files in this directory to build the image.

3. **Verify the Image**
   
    Once the image is built, you can list your Docker images to ensure the build was successful :

    ```
    docker images
    ```

5. **Run the Docker Container from the image**
   
    Once the image is built, you can run a container from it with the following command:

   ```
   docker run -d -p 80:80 my-python-app
   ```

    * `-d` : Runs the container in detached mode (in the background).
    * `-p 80:80` : Maps port 80 of your host machine to port 80 of the container. This means you can access the application via http://localhost on your host machine.
    * `my-python-app` : This is the name of the image you just built.
    * `--name <container-name>`(Optionnal): Assigns a name to the running container for easier reference.

7. **Check Running Containers**
   
    You can verify if the container is running by listing all active containers:
    ```
    docker ps
    ```
    
9. **Interact with the Running Container**
    
    You can enter the running container's shell to inspect it further:
    ```
   docker exec -it <container-name> /bin/bash
    ```
    
    This opens an interactive terminal session inside the container.

11. **Stop and Remove Containers**
    
    Once you're done with the container, you can stop it:

    ```
    docker stop <container-name>
    ```

    To remove it:

    ```
    docker rm <container-name>
    ```


13. **Push the Docker Image to a Registry (Optional)**
    
    If you want to share your image or deploy it on another server, you can push it to a Docker registry like [Docker Hub](https://hub.docker.com/)  or a private registry.



### 3. Docker Compose

**Docker Compose is** a tool that allows you to define and manage multi-container Docker applications. Instead of running multiple docker run commands for each container in your application, you can use Docker Compose to define all the services (containers), their configurations, and dependencies in a single YAML file (docker-compose.yml).

Docker Compose simplifies starting, stopping, and managing complex applications with multiple containers by allowing you to control everything with just a few commands.

1. **docker-compose.yaml file**

    The key concepts of a **docker-compose.yaml** file
    * **Services:** In Docker Compose, each container is referred to as a service. Each service runs a container, and it’s defined in the docker-compose.yml file. For example, you might have a service for your application, a database, and a caching service like Redis.
    * **docker-compose.yml File:** This is the core configuration file for Docker Compose, where you define all your services, their build configuration, environment variables, volumes, networks, etc.

    This an example of dockercompose file :

    ```
    version: '3'

    services:
    web:
        build: .
        ports:
        - "5000:5000"
        volumes:
        - .:/code
        environment:
        - FLASK_ENV=development

    redis:
        image: "redis:alpine"
    ```

2. **How to use Docker compose**

    * Create a **docker-compose.yaml**
    * Start Start the Application : With docker compose this can be done with one single command: `docker-compose up`
    * Docker also allows to scale (create multiple) services : `docker-compose up --scale web=3` This will run 3 instances of the **web** service.
    * Stop the Application to stop and clean up all resources created by Docker Compose: `docker-compose down`
