sudo apt update
sudo apt install bc
sudo rmmod r8188eu.ko
git clone https://github.com/aircrack-ng/rtl8188eus
cd rtl8188eus
sudo -i
echo "blacklist r8188eu" > "/etc/modprobe.d/realtek.conf"
exit
make
sudo make install
sudo modprobe 8188eu

ifconfig wlan0 down
airmon-ng check kill
iwconfig wlan0 mode monitor
ifconfig wlan0 up
iwconfig



echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee /etc/apt/sources.list
sudo apt-get update
sudo apt-get install -y bc linux-headers-$(uname -r)
git clone https://github.com/aircrack-ng/rtl8188eus.git
cd rtl8188eus
wget https://raw.githubusercontent.com/kimocoder/rtl8188eus/v5.7.6/realtek_blacklist.conf
cp realtek_blacklist.conf /etc/modprobe.d
make
make install



sudo ifconfig
ifconfig wlan0 down
airomon-ng
check kill
iwconfig wlan0 mode monitor
ifconfig wlan0 up
airodump-ng wlan0


git clone --recursive https://github.com/KanuX-14/rtl8188eus.git
cd rtl8188eus
printf "blacklist r8188eu\n" | sudo tee "/etc/modprobe.d/realtek.conf"
sudo rmmod r8188eu
make && sudo make install clean
sudo modprobe 8188eu