
Vagrant.configure("2") do |config|

  config.vm.box = "hashicorp/bionic64"

  # Create a forwarded port mapping (not needed for hyperv) 
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.network "public_network"

  config.vm.provider "hyperv"

  config.vm.provision "shell", privileged:false, path: "vagrant_provision_script.sh"
    
  config.trigger.after :up do |trigger|
    trigger.name = "Launching App"
    trigger.info = "Running the TODO app setup script"
    trigger.run_remote = {privileged: false, path: "vagrant_trigger_script.sh"}
    end

end
