FROM disconnect3d/nsjail

RUN apt-get update && apt-get install -y python3

ADD . /task

RUN groupadd nobody

CMD /task/launch_jail.sh

