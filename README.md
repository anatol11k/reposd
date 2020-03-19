It's a Python script which prints basic cpu or memory metrics about Linux OS to console.

The script accept a single parameter to specify which metrics set to print:

    cpu - prints CPU metrics
    mem - prints RAM metrics

Requirements

    python 3 or 2
    pip
    psutil

Installation

git clone https://github.com/anatol11k/reposd.git

pip install psutil

Examples

$python3 got_metrics.py mem

MEM:

virtual total 1918517248
virtual used 364630016
virtual free 172896256
virtual shared 7729152
swap total 2222977024
swap used 1847296
swap free 2221129728



$python3 got_metrics.py cpu

CPU:

system.cpu.idle 13570.12
system.cpu.user 81.66
system.cpu.guest 0.0
systemc.cpu.iowait 2.96
systemc.cpu.stolen 0.0
system.cpu.system 36.33


DOCKER

Script can be run under docker container.
https://hub.docker.com/repository/docker/anatol11k/metrics

RUN

docker run -t --rm tolkol/metrics:v1 mem
docker run -t --rm tolkol/metrics:v1 cpu
