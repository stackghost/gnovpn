# What?
Gnovpn is a very basic script to convert **OpenVPN Access Server** profiles
to use with **Gnome Network Manager**

# How?
The script splits a single *.ovpn file and splits the keys into separate
files and creates a new config.ovpn file to use for import

* Script-generated files
  * ca.crt (ca file)
  * config.crt (cert file)
  * config.key (key file)
  * config-tls.key (tls-auth file)
  * config.ovpn (new profile for import)

# Why?
I got tired of manually converting the profiles provided by the access
server everytime I needed to import a new vpn profile

# Where?
Tested on Linux Mint but should work on all flavors of Gnome

# Usage
`$ ./gnovpn.py /path/to/client.ovpn`
