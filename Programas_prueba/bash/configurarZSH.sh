#!/bin/bash

sudo apt update && sudo apt install zsh -y 

chsh -s $(which zsh)

sudo apt install git curl -y

wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh

sh install.sh

sudo usermod --shell /usr/bin/zsh $(whoami)

git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
nombre = $(whoami)
sudo su root

cd 

rm .zshrc

ln -s -f /home/$nombre/.zshrc .zshrc
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
rm .p10k.zsh

ln -s -f /home/$nombre/.p10k.zsh .p10k.zsh

