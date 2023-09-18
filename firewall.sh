#!/bin/bash

# Set the IP address of the MoMo server
MOMO_SERVER_IP="35.240.103.94"

# Get the current SIM card ICCID
SIM_ICCID=$(cat /sys/fs/cgroup/device/phone/modem/0/iccid)

# Check if the SIM card ICCID has changed since the last boot
if [ "$SIM_ICCID" != "$(cat /var/run/sim_iccid)" ]; then

  # The SIM card ICCID has changed, so lock the firewall
  iptables -F
  iptables -P INPUT DROP

  # Add a rule to allow incoming connections from the MoMo server
  iptables -A INPUT -s "$MOMO_SERVER_IP" -j ACCEPT

  # Add a rule to allow incoming connections from the user's trusted IP address
  iptables -A INPUT -s 192.168.1.100 -j ACCEPT

  # Save the new firewall rules
  iptables-save

  # Log the SIM card swap event
  logger "SIM card swap detected. Firewall locked."

fi

# Update the SIM card ICCID file
echo "$SIM_ICCID" > /var/run/sim_iccid

# Block all incoming traffic on the MoMo server's IP address
iptables -A INPUT -s "$MOMO_SERVER_IP" -j DROP

# Allow outgoing traffic from the MoMo server's IP address
iptables -A OUTPUT -s "$MOMO_SERVER_IP" -j ACCEPT

# Allow incoming traffic on port 8080 (honeypot)
iptables -A INPUT -p tcp --dport 8080 -j ACCEPT

# Log all incoming and outgoing traffic
iptables -A INPUT -j LOG --log-prefix "INCOMING: "
iptables -A OUTPUT -j LOG --log-prefix "OUTGOING: "

# Block all incoming traffic on all ports
iptables -P INPUT DROP

# Allow specific IP addresses
iptables -A INPUT -s 192.168.1.1 -j ACCEPT # Allow traffic from IP address 192.168.1.1
iptables -A INPUT -s 192.168.1.2 -j ACCEPT # Allow traffic from IP address 192.168.1.2

# Save the firewall rules
iptables-save

# Error handling
if [[ $? != 0 ]]; then
  echo "Failed to save firewall rules."
  exit 1
fi

echo "Firewall rules saved successfully."
