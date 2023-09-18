
# Set the IP address of the MoMo server
MOMO_SERVER_IP="35.240.103.94"

# This script blocks all incoming traffic on the MoMo server's IP address, allows
# outgoing traffic from the MoMo server's IP address, logs all incoming and
# outgoing traffic, blocks all incoming traffic on all ports, and allows
# specific IP addresses. It also includes error handling to check the exit status
# of the `iptables-save` command.

# To use this script, simply run it from the command line. For example:

# $ sudo ./firewall.sh

# Flush all current firewall rules
function flush_firewall_rules() {
  iptables -F
}

# List all current firewall rules
function list_firewall_rules() {
  iptables -L
}

# Block all incoming traffic on the MoMo server's IP address
iptables -A INPUT -s $MOMO_SERVER_IP -j DROP

# Allow outgoing traffic from the MoMo server's IP address
iptables -A OUTPUT -s $MOMO_SERVER_IP -j ACCEPT

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
