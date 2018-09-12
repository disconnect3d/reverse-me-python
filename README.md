# Reverse Me

Reverse Me or "I hate portals" was a challenge made by [Disconnect3d](https://disconnect3d.pl) for [Python Challenges 2018](https://www.python-challenges.com) competition held at [PyCon PL 2018](https://pl.pycon.org/2018/en/).

The challenge requires user to find out three flags that are hidden in the Python script that is being executed. The catch is: the challenges source code cannot be read. At least in theory. There are multiple ways to solve all three levels of the challenges =).

**The challenge is not hosted there anymore, but with the source code in this repo, you can host it locally or on your machine.**

## Launching the challenge locally

Clone the repo, go to `src` and fire `./build_and_launch.sh`. This will build a docker image that will run nsjail and expose it on 31337 port.

NOTE: This requires `docker` to be installed and uses an unofficial docker image `disconnect3d/nsjail`. Yeah, this is my image and has been built by `docker build -t disconnect3d/nsjail .` fired in the `nsjail` repo on its `1bb5808` git commit id/revision.

## Configuration and writeups

*I am going to create 1-2 videos about the challenge, different solutions and how it's hosted.*
Stay tuned! o/

During the PyCon PL I have also gathered solutions and made a short talk about it:
* https://docs.google.com/presentation/d/1ARiS5JSu9u4LGbiveSVY4Uzo27aHuw--lwCr8JKtEFU/

I also described the configuration in a normal talk I made during PyCon PL, but I am not sure if pure slides are that helpful (see 37+ slides):
* https://docs.google.com/presentation/d/1LTIuStnvlKvkyRdpFmXrJ6-fxYE0roU_gHJ-83nk0zU/
