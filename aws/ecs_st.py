#!/usr/bin/env python3

'''
ECS study
This document description the ECS on AWS

ECS: Amazon EC2 Container Service that make it easy run,stop and manage Docker containers on EC2 instances.

A Docker container is a standardized unit of software development, containing everything that your software application needs to run: code, runtime, system tools, system libraries, etc. Containers are created from a read-only template called an image.

1. build a Docker image using Dockerfile
2. Public the image file into Docker hub or other repository
3. Create the Task Definitions. The task definition is a json format file which describe one or more contains that form your application.


"containerDefinitions:"[
    {
        "name":"web",
        "image":"nginx",
        "cpu":100,
        "memory":100,
        "portMappings":[
            {
                "containerPort":80,
                "hostPort":8080
            }
        ],
        "mountPoints":[
            {
                "sourceVolumn":"webdata",
                "containerPath":"/usr/share/data"
            }
        ]
    }
]
'''


up_cmd = 'ecs-cli up --keypair id_rsa --capability-iam --size 2 --instance-type t2.medium'

# create a compose file

compose_cmd = 'ecs-cli compose --file hello-world.yml up'


view_cmd='ecs-cli ps'
