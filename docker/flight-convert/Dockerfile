FROM ubuntu:16.04
MAINTAINER jing wang <jingwangian@gmail.com>

RUN apt-get update

# curl/wget/git
RUN apt-get install -y curl wget git

# vim/emacs
RUN apt-get install -y vim emacs

RUN apt-get install -y build-essential gcc
RUN apt-get install -y valgrind
RUN apt-get install -y ltrace
RUN apt-get install -y libc6-dev-i386
RUN apt-get install -y libssl-dev

# Python
RUN apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev

RUN cd /usr/src ; wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz ; tar xzf Python-3.6.2.tgz ; cd Python-3.6.2 ; ./configure ; make altinstall


#RUN ! ls /usr/bin/python3.4 && ls /usr/src/Python-3.4.3/python && cp /usr/src/Python-3.4.3/python /usr/bin/python3.4 ; exit 0
# replace python version to have 3.4.4 as default RUN rm -f /usr/bin/python
RUN rm -f /usr/bin/python3
RUN ln -s /usr/bin/python3.6 /usr/bin/python
RUN ln -s /usr/bin/python3.6 /usr/bin/python3

# SSH
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN apt-get install -y python3-pip


ADD run.sh /tmp/run.sh
RUN chmod u+x /tmp/run.sh
# start run!
CMD ["./tmp/run.sh"]
