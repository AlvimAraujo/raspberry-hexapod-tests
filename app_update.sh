#!/bin/bash

# Set the source and destination variables
PASSWORD="raspberrypi"
DESTINATION_DEVICE="raspberry@192.168.0.107"
SOURCE_DIR="../sources/"
DESTINATION_DIR="/home/raspberry/tests/sources/"

# Copy the .ipk file to the destination device using scp
sshpass -p "$PASSWORD" scp -r "$SOURCE_DIR" "$DESTINATION_DEVICE:$DESTINATION_DIR"

# SSH into the destination device and install the .ipk file using opkg
sshpass -p "$PASSWORD" ssh "$DESTINATION_DEVICE" "opkg install $DESTINATION_DIR/file.ipk"
