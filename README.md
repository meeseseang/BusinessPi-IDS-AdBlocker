# BusinessPi-IDS-AdBlocker
Code files for 2020-21 AP Research project Business Pi IDS. Includes Python interface script.

# Goal
Create a basic network IDS based on Snort IDS, PiHole, and a custom Python interface. In the future, I plan on adding IPS functionality to the current script.

# Install Instructions

## Install all required dependencies.

### Python
I installed Python 3.9.2 from source. You can find tutorials on how to do that elsewhere. The module that needs to be installed for this project is PySimpleGUI. It can be installed with `pip3 install PySimpleGUI`

### Snort
Dependencies for Snort can be installed using `sudo apt update && sudo apt install ssh apache2 apache2-doc libapache2-mod-php5 autoconf automake bison ca-certificates ethtool flex g++ gcc gcc-4.4 libcrypt-ssleay-perl libmysqlclient-dev libnet1 libnet1-dev libpcre3 libpcre3-dev libphp-adodb libssl-dev libtool libwww-perl make mysql-client mysql-common mysql-server ntp php5-cli php5-gd php5-mysql php-pear sendmail-bin sendmail systat usbmount`
You will also need to install libpcap, libdnet and daq from source.
If using a debian based Linux OS then you can install Snort with `sudo apt update && sudo apt install snort -y` otherwise follow other tutorials for installing Snort from source.

### PiHole
To install PiHole, use the command `curl -sSL https://install.pi-hole.net | bash` to install. When it asks how to configure PiHole, set it up with IPv4 and IPv6. Set logging to everything. I used Google DNS due to its reliability, however, you can choose whatever server works best for you.

## Clone the Repo.
Go into your home directory and use `git clone https://github.com/thewitchkingleader/BusinessPi-IDS-AdBlocker`
Then move the StartInterface.sh file to your desktop.

## Run the Python file.
To start the GUI interface from the desktop with a touchscreen, double tap the StartInterface.sh bash script file. Otherwise, if you would like to start it from the terminal, open the directory where the Python script is stored. Then run `python3 BusinessPiInterface.py`
