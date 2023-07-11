#!/bin/bash

# Set the OpenVPN configuration file path
CONFIG_FILE="/path/to/vpn/config.ovpn"

# Connect to the VPN server
sudo openvpn --config "$CONFIG_FILE"
