VAGRANTFILE_API_VERSION = "2"

# NOTE(gyee) we have to do this because there appears to be a bug in the
# vagrant virtualbox plugin, that it can automatically detect the provider
# from the box. 'vagrant box list' does show the correct provider btw.
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'libvirt'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "keystone-idp", autostart: true, primary: true do |keystone|
    #keystone.vm.box = "opensuse/openSUSE-15.0-x86_64"
    keystone.vm.box = "dcermak/openSUSE-Leap-15.1-Vagrant.x86_64"
    keystone.vm.hostname = "keystone-idp"

    keystone.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.name = "keystone-idp"
    end

    keystone.vm.provider :libvirt do |lv|
      lv.memory = "4096"
    end

    #keystone.vm.synced_folder "./shared_dir", "/home/vagrant/shared_dir"

    # for Horizon browser access
    #config.vm.network "forwarded_port", guest: 80, host: 80
    #config.vm.network "forwarded_port", guest: 443, host: 443

    # setup private network only
    keystone.vm.network "private_network", ip: "192.168.0.10"
  end

  config.vm.provision :ansible do |ansible|
    ansible.config_file = "./ansible.cfg"
    ansible.playbook = "./ansible/keystone.yml"
    ansible.extra_vars = {
      "enable_gather_facts" => true,
      "need_python_interpreter" => true,
      "user_home_dir" => "/home/vagrant"
    }
    ansible.groups = {
      "kerberos" => ["keystone-idp"],
      "keystone" => ["keystone-idp"],
      "pki" => ["keystone-idp"],
      "glance" => ["keystone-idp"],
      "horizon" => ["keystone-idp"]
    }
    ansible.host_vars = {
      "keystone-idp" => {
        "host_ip" => "192.168.0.10"
      }
    }
  end

  # Copy my ssh keys over so I can submit upstream reviews
  config.vm.provision "file", source: "~/.ssh/id_rsa", destination: ".ssh/id_rsa"
  config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: ".ssh/id_rsa.pub"

end
