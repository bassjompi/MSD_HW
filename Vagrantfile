# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"
  config.vm.hostname = "MSD-JUAN"


  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  
    config.vm.network "private_network", ip: "192.168.33.13"
 

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL

  config.vm.provision :ansible do |ansible|
  ansible.playbook = "playbook.yml"

end
end
