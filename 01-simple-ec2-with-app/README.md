# Run an Nginx inside docker on ec2

## spin up ec2 instance

- spin up ec2 instance with security group allowing port 80 and 22.
- make sure to have key pair to ssh into the instance.
- make sure that docker is installed on the instance.

```bash
# Update the instance
sudo yum update -y
# Install docker
sudo yum -y install docker
```

- Pull and run nginx container on Docker, mapping port 80 of the container to port 80 on the host
  docker run -d -p 80:80 nginx

## Do it with user-data:

After all done manually, we can use user-data to automate the process:

```bash
#!/bin/bash

# Update the instance
sudo yum update -y
# Install docker
sudo yum -y install docker
# Add the ec2-user to the docker group so you can execute Docker commands without using sudo
sudo usermod -a -G docker ec2-user
sudo su - $USER
# Start Docker and enable it to start at boot time
sudo systemctl start docker
sudo systemctl enable docker
# Pull and run nginx container on Docker, mapping port 80 of the container to port 80 on the host
docker run -d -p 80:80 nginx

```

## After instance is up browse to it's public IP in route - /consume_memory
