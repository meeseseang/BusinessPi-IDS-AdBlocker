# BusinessPi-IDS-AdBlocker
Code files for 2020-21 AP Research project Business Pi IDS. Includes Python interface script.

# Goal 
Create a basic network IDS based on Snort IDS, PiHole, and a custom Python interface. In the future, I plan on add a Python program that takes the alerts and acts upon them.

# Install Instructions
2. Clone the Repo.
3. Run the Python file.
## Install all required dependencies.
### Python
### Snort
### PiHole
To install PiHole, use the command `curl -sSL https://install.pi-hole.net | bash` to install. When it asks how to configure PiHole, set it up with IPv4 and IPv6. Set logging to everything. I used Google DNS due to its reliability, however, you can choose whatever server works best for you.
## Clone the Repo.
Go into your home directory and use `git clone https://github.com/thewitchkingleader/BusinessPi-IDS-AdBlocker`
## Run the Python file.
