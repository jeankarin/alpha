#!/bin/bash

# Añadimos repositorio
sudo apt-add-repository ppa:ansible/ansible

# Actualizamos los repositorios
sudo apt update

# Instalamos ansible
sudo apt install ansible

# Testing collections
# ansible all -m ping -u root
# ansible all -a "df -h" -u root
# ansible all -m apt -a "name=vim state=latest" -u root
# ansible servers -a "uptime" -u root
# ansible server1:server2 -m ping -u root

# Fuente: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-ubuntu-20-04
