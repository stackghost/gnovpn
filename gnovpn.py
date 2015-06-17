#!/usr/bin/env python3
# @name gnovpn.py
# @description convert OpenVPN Access Server (*.ovpn) profiles to
#  Gnome network manager format
#
# @usage ./gnovpn.py /path/to/client.ovpn
#
# @author Harim G.A.
# @email wizgeeky@stackghost.com
# @copyright 2015 StackGhost.com, All Rights Reserved
# 
import os
import sys
from html.parser import HTMLParser

class ConvertOpenVPNConfig(HTMLParser):
	opentag = False
	currtag = None
	convert = ''

	def handle_starttag(self, tag, attrs):
		if tag == 'ca':
			self.opentag = True
			self.currtag = 'ca'
		elif tag == 'cert':
			self.opentag = True
			self.currtag = 'cert'
		elif tag == 'key':
			self.opentag = True
			self.currtag = 'key'
		elif tag == 'tls-auth':
			self.opentag = True
			self.currtag = 'tls-auth'
	def handle_endtag(self, tag):
		self.opentag = False
	def handle_data(self, data):
		if self.opentag == False:
			self.convert += data
		else:
			if self.currtag == 'ca':
				cafile = open("{}/ca.crt".format(os.path.dirname(filename)), 'w')
				data = os.linesep.join([s for s in data.splitlines() if s])
				cafile.write(data)
				print("Generated ca.crt ...")
				self.convert += 'ca ca.crt'
			elif self.currtag == 'cert':
				certfile = open("{}/config.crt".format(os.path.dirname(filename)), 'w')
				data = os.linesep.join([s for s in data.splitlines() if s])
				certfile.write(data)
				print("Generated config.crt ...")
				self.convert += 'cert config.crt'
			elif self.currtag == 'key':
				keyfile = open("{}/config.key".format(os.path.dirname(filename)), 'w')
				data = os.linesep.join([s for s in data.splitlines() if s])
				keyfile.write(data)
				print("Generated config.key ...")
				self.convert += 'key config.key'
			elif self.currtag == 'tls-auth':
				tlsfile = open("{}/config-tls.key".format(os.path.dirname(filename)), 'w')
				data = os.linesep.join([s for s in data.splitlines() if s])
				tlsfile.write(data)
				print("Generated config-tls.key ...")
				self.convert += 'tls-auth config-tls.key'

if len(sys.argv) == 1:
	print("Please specify OpenVPN profile [e.g. {}/client.ovpn]:".
		format(os.environ['HOME']))
	filename = input("> ")

	if filename == '':
		sys.exit("ERROR: OpenVPN Access Server profile cannot be blank")
else:
	script, filename = sys.argv

if os.path.exists(filename):
	config = open(filename)
else:
	sys.exit("ERROR: File Not Found {!r}".format(filename))

parser = ConvertOpenVPNConfig()
parser.feed(config.read())

profile = open("{}/config.ovpn".format(os.path.dirname(filename)), 'w')
output = os.linesep.join([s for s in parser.convert.splitlines() if s])
profile.write(output)
print("Generated config.ovpn ...")
print("Done!")