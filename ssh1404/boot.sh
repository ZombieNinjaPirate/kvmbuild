# This script runs the first time the virtual machine boots

# Install avalible updates and upgrade kernel.
apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && apt-get autoclean -y && apt-get autoremove