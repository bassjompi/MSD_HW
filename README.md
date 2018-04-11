# Description

This Repo will deploy a centOS 7 VM using vagrant and will provision it with Ansible with the following items:

1. Install Nginx server
2. Deploy of a python (flask) app that will show the system info
3. The app will be communicating with Nginx using uWSGI
4. Nginx is used as a reverse proxy in front of the application and provides SSL communication based on self-signed certificate
5. Install Supervisord  and implementation of the Nginx and uWSGI services using it
6. Add an entry in your local /etc/hosts with the new server  (MSD_JUAN)
---

# Requirements

You will need the following software installed in your machine:

1. Ansible
2. Vagrant
3. VirtualBox or other VM provider for Vagrant (vmware_desktop,libvirt,hyperv)
---

# Use instructions

1. Clone the repository to your local host and change directory to the main /MSD_HW folder
2. Start the VM creation and the ansible provisioning with the command

                                           vagrant up
                                            
3. Once the VM is created and provisioned you should be able to access the site and see the system info at    https://192.168.33.13
4. Suervisord interface should be now accesible at      http://192.168.33.13:9001
5. Execute the playbook_local.yml  to add an entry in your local /etc/hosts with the new server  (MSD_JUAN)

          			ansible-playbook -i "localhost," -c local playbook_local.yml
											
6. Now try to ssh the server using the hostname

   				ssh vagrant@MSD_JUAN -i  PATH_TO_REPO/.vagrant/machines/default/virtualbox/private_key
---

# Roles description


## Nginx

This role will simply install the EPEL repository for Centos7 and then it will install Nginx. EPEL is needed in order to download nginx via yum


## SSL

This role has the final purpose of generating a self signed certificate in the host. For this the automation will:

1. Install the required packages: openssl, pip (needed to install python packages) and PyOpenssl
2. Create the directories were we will generate the certificate and key
3. Generate a private key  in /etc/ssl/private/msd.pem
4. Generate a certificate signing request using that key, and filling the data needed (email, country ...etc)
5. Finally it will generate a self signed certificate using the key and the signing request. We can now use our certificate sitting in the folder /etc/ssl/certs/nginx-selfsigned.crt


## App

This role will deploy a python app (flask) that will communicate with the nginx server using uWSGI so it can be used as a reverse proxy using SSL with the certificate we generated in the previous role.
Steps are:

1. Install all the required python dependencies and pip packages (including uWSGI and Flask framework) so our app can run
2. We will copy our python app into the host in the /etc/nginx/app folder.  The app is sitting in the /FILES folder of the role
3. Copy he nginx.conf file (configuration file for nginx) to redirect the app being served over uWSGI to the SSL port 443. The file is sitting in the /FILES folder of the role 

              Problem found: The reverse proxy seemed to be not working and i was receiving the "failed (98: Address already in use)" in the ssl port 443
	      The root cause was the Security-Enhaced linux interfering the communication. For this we will have to set Selinux to "Permissive" state
                             
4. Set the Selinux to "Permissive" state to solve the above mentioned problem   


## Supervisord

This role will install and setup supervisord and will link it to the Nginx and uWSGI proccesses. For this it will execute the following steps:

1. Upgrade pip (needed to install latest version of supervisord) and then install Supervisord
2. Copy the supervisord conf file sitting in the /FILES folder of the role to the host. This conf file has been already modified to add the nginx and uWSGI processes
3. Start supervisord.This will automatically start the Nginx server and the uWSGI bridge. From now we will be able to monitor the services through the web interface http://192.168.33.13:9001


## Local_actions

This is a very simple role. It will just add an entry in our local machine /etc/hosts  file for our new server. The server was automatically renamed to MSD_JUAN in the Vagrantfile configuration
