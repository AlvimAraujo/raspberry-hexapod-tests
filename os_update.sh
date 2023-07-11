#!/bin/bash

# Set the source and destination variables
PASSWORD="raspberrypi"
DESTINATION_DEVICE="raspberry@192.168.0.107"
SOURCE_DIR="../sources/"
DESTINATION_DIR="/home/raspberry/tests/sources/"

# Copy the .mender file to the destination device using scp
sshpass -p "$PASSWORD" scp -r "$SOURCE_DIR" "$DESTINATION_DEVICE:$DESTINATION_DIR"

# SSH into the destination device and install the .mender file using the Mender CLI
sshpass -p "$PASSWORD" ssh "$DESTINATION_DEVICE" "sudo mender install $DESTINATION_DIR/file.mender"
