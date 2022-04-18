echo PrismOS Installer
echo NOTICE: This software is still in beta and is currently in development. Expect there to be bugs.
echo Installing dependencies...
# Install dependencies (lxde, python3, pip)
sudo apt install lxde python3 python3-pip xterm

# Install Python Packages
pip3 install pyglet numpy imgui[pyglet] 
echo Done!

# Clone the repository
echo Cloning...
sudo git clone https://github.com/ChickenChunk579/Prism /opt/prism
echo Done!
echo To launch prism, type bash /opt/prism/launch.sh