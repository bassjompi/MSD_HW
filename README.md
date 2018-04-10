# Description

This Repo will deploy a centOS 7 VM using vagrant and will provision it with Ansible with the following items:

1. Install Nginx server
2. Deploy of a python (flask) app that will show the system info
3. The app will be communicating with Nginx using uWSGI
4. Nginx is used as a reverse proxy in front of the application and provides SSL communication based on self-signed certificate
5. Install Supervisord  and implementation of the Nging and uWSGI services using it
6. Add an entry in your local /etc/hosts with the new server  (MSD_JUAN)
---

# Requirements

You will need the following software installed in your machine:

1. Ansible
2. Vagrant
---

# Use instructions

1. Clone the repository to your local host
2. Issue the command "vagrant up", that should start the VM creation and the ansible provisioning
3. Once the VM is created and provisioned you should be able to access the site https://192.168.33.13
4. Suervisord interface should be now accesible at http://192.168.33.13:9001
5. Execute the playbook_local.yml  to add an entry in your local /etc/hosts with the new server  (MSD_JUAN)

          									ansible-playbook -i "localhost," -c local playbook_local.yml
											
6. Now try to ssh the server using the hostname

          									ssh vagrant@MSD_JUAN -i  PATH_TO_REPO/.vagrant/machines/default/virtualbox/private_key
---

# Roles description

## Nginx

This role will simply install the EPEL repository for Centos7 and the it will install Nginx. EPEL is needed in order to download nginx via yum
