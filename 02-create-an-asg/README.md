# Autoscaling Group - ASG

## Create an Autoscaling Group - ASG

- Enter EC2 menu
- At the bottom enter the Auto Scaling Groups menu
- Name your ASG
- Create a new launch template
  - choose instance type : t2.micro
  - user-data: copy the script from below
- Choose VPC and subnets - make sure it's public
- No load balancer
- min: 1, max: 2, desired: 1
- Add stress using:

```bash
docker run -dti --rm polinux/stress stress --cpu 1 --io 1 --vm 1 --vm-bytes 8M --timeout 600s --verbose
```

user-data script:

```bash
#!/bin/bash

# Update the instance
sudo yum update -y
# Install docker
sudo yum -y install docker
sudo yum -y install python-pip
pip3 install bpytop --upgrade
# sudo yum -y install htop
# Add the ec2-user to the docker group so you can execute Docker commands without using sudo
sudo usermod -a -G docker ec2-user
sudo su - $USER
# Start Docker and enable it to start at boot time
sudo systemctl start docker
sudo systemctl enable docker
# Run our container
docker run -d -p 80:80 assafushy/aws-demo-server:latest

```
