# IS 404 -- Docker Lab

[<< Back to main](readme.md)

This walkthrough will help you get started installing and using Docker. You should already conceptually understand what Docker is. Checkout [this page](https://www.docker.com/resources/what-container) if you need a refresher.

## INSTALL DOCKER

You can install Docker in a lot of different ways. Because a Raspberry Pi (RPi) uses an ARM-based CPU, some online tutorials for installing Docker might not work. 

The tutorial I found [here](https://linuxhint.com/install_docker_on_raspbian_os/) is made specifically for the RPi, and seems to work. I'll repeat the basics of that tutorial below.

1. `sudo apt update`
    * [ update package list ]
2. `sudo apt upgrade`
    * [ update pckages ]
3. `sudo apt install raspberrypi-kernel raspberrypi-kernel-headers`
    * [ install necessary packages ]
4. `curl -sSL https://get.docker.com | sh`
    * [ download the installation program and run it ]
5. `sudo usermod -aG docker pi`
    * [ add the `pi` user to the `docker` group ]
6. `sudo reboot`
    * [ restart so the changes can take place ]
7. `docker version`
    * [ test that everything works! ]

---
## BASIC DOCKER COMMANDS

`docker` is the main command we use to interact with Docker. The following "commands" are all used as arguments to the `docker` command. IOW, the `images` command is called with `docker images` and so on. 

Running `docker` will give a comprehensive list of all Docker commands, but here are some basic ones that are important to know.

* `pull` : Pull a Docker image from the Docker repository
* `run` : Create a new Docker container by 'running' an image
* `images` : Show all the Docker images available to the system
* `ps` : Show the Docker containers that are currently running
* `build`: Build a Docker image from a Dockerfile (more on this later)

---
## HELLO WORLD

Docker makes it easy to run our first container. There is an image called **hello-world** on the Docker repository. Use the following command to pull the image and run the container.
```
$ docker run hello-world
```
If it was your first time running the **hello-world** image, you'll notice that Docker had to *pull* the image before it could run it. Try running it again. Did it go faster? Because the image was pulled when we first ran `docker run hello-world`, the image was already on the system, and didn't need to pulled again. Instead, Docker found took the image and made the container.

But how can we know whether or not we have the **hello-world** image saved? If you didn't skip the above section, you would know that we can use `docker images`.

Let's see what images we have saved:
```
$ docker images
```

This command provides a list of all your saved images. It'll show the image name, the tag, the image ID, when it was created, and the size. You should see that the **hello-world** image is listed here (along with others you might have).

---
## SIMPLE EXAMPLE

Running the **hello-world** example wasn't all that cool, so let's do something more practical. Let's imagine that we want to build a NodeJS application on our RPi, but installing NodeJS can be tricky sometimes. Plus, we would want to make sure that we have the latest NodeJS / NPM versions, and we'd need to worry about these versions in future deployment.

Things will be a lot simpler if we just used Docker! Before we make a container for our NodeJS app, let's check if we have NodeJS on our system. If you are using the standard Raspbian distribution, you probably won't have NodeJS installed, and will recieve the following error message upon entering the `node` command.

```
$ node
-bash: node: command not found
```
Looks like we don't have NodeJS installed! (**NOTE**: if you do happend to have Node installed, just pretend that don't for the sake of this example)

Before we run a container-ized version of our app, we need the appropriate image. As you might've guessed, the image we are looking for is called **node**. Pull the image with the following command:
```
$ docker pull node
```
This might take awhile due to the RPi's limited resources, so be patient.

You can use `docker images` to double check that you have successfully pulled the **node** image.

Now that we have the **node** image, let's test it out. We can use *interactive* mode with the `-it` option. This will put us in the Node shell as if we had ran the `node` command.
```
$ docker run -it node
```

Now that you are in the Node shell, try writing some Javascript to test it out.
```js
> console.log('using node now!')
using node now!
```
When you are done, hit `Ctrl+c` twice to exit the Node shell (and the container).

If you try running `node` again in your terminal, you'll see that the `node` command is still not found. The Node environment only existed in the Docker container. After we stopped the container, Node no longer exists. 

---
## CREATING YOUR OWN IMAGE

Aside from testing out small snippets of code, writing some Javascript in the Node shell isn't all that useful. Generally, we have some application that we have written, and will want to use Docker to deploy it. To do this, we need to create our own Docker image. This is much easier than it sounds, because we can *pull* in other Docker images, add then customize it by adding some rules and commands for the container to run. Actually, many Docker images are built in this way, using other Docker images for their foundation.

Before we create our Docker image, we first need to write an "application". First, let's make a folder for our app:
```
$ mkdir js_timer
$ cd js_timer
```
Create a file named `timer.js` and add the following:
```js
setInterval( () => console.log(`UTC TIME: ${Date.now()}`), 5000 )
```
Now that we have our "application", we are ready to create our Docker image. Docker images are defined by a file named `Dockerfile`. Notice how the Dockerfile doesn't have a file extenstion, it is simply named `Dockerfile`. 

We don't have enough time to discuss every command that can be used in Dockerfiles, so we'll just cover the basic ones needed for running our app:
* `FROM` : Pull in the base image that we will be working with
* `RUN` : Run a command within the new container
* `WORKDIR` : Set the working directory within the new container
* `COPY` : Copy files from the local system to the container
* `CMD` : Define the final command that should be run to start the application

Make sure you are are still in the application folder, and create a file named `Dockerfile` and add the following:
```Dockerfile
FROM node:latest

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN ["node", "timer.js"]
```
What's going on here?
1. We are going to use the **node** image as our base
1. We make a new folder called `app` inside our container
1. We set the `app` folder as our working directory
1. We copy all the files (that's what the `.` means) in the local system, and put it into the `app` folder in the container
1. We tell the container to run the command `node timer.js`

With our Dockerfile created, we are ready to make the image! We use the `build` command and the `-t` option to give it a name. Note the period (`.`) at the end: it tells the `build` command to look for the Dockerfile in the current directory.
```
$ docker build -t my_timer .
```

This command will run through each line in the Dockerfile and provide some output. Look thru each step and try to understand what it is saying.

Run `docker images` to make sure that our image was created successfully. If so, we are ready to create a container from the image we just created.
```
$ docker run --name MyTimer --detach my_timer
```
If everything goes correctly, this command will return the ID (a really long string of letters and numbers) of the newly made container.

We used the `--detach` option to run the the Docker container in the "background". Without this option, we would see the output of our Node application. This may be useful in some situations, but generally we want to run our Docker container in the background so we can continue doing other things on the computer.

## MANAGING CONTAINERS

If our Docker container is running in the background, how can we really make sure that it is running? We use the `ps` command as follows:
```
$ docker ps
```
You should be able to see the "MyTimer" container, along with several details about it. Just like images, each container has a unique ID. We can use this ID to manage our containers. Luckily, we can usually use the first three characters of the container ID to run most commands instead of copy-and-pasting the entire ID. For example, we can check the output of our container with the the `logs` command:
```
$ docker logs <FIRST_3_CHARS_OF_CONTAINER_ID>
```
Hopefully you were able to see the output of our Javascript program.

We can use the ID to stop this container:
```
$ docker stop <FIRST_3_CHARS_OF_CONTAINER_ID>
```

We can view this stopped container by adding the `-a` to the `ps` command:
```
$ docker ps -a
```
From here, we can use the `start` or `rm` command to start or delete the container, respectively. 

---
## THANKS
<!-- ---
## YOUR TURN

have them do something on their own?
    TBD

-->