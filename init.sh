service iptables status
yum install -y iptables
yum update iptables
yum install iptables-services
systemctl stop firewalld
systemctl mask firewalld
iptables -L -n
iptables -P INPUT ACCEPT
iptables -F
iptables -X
iptables -Z
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 25565 -j ACCEPT
iptables -A INPUT -p icmp --icmp-type 8 -j ACCEPT
iptables -A INPUT -m state --state  RELATED,ESTABLISHED -j ACCEPT
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
service iptables save
systemctl enable iptables.service
systemctl start iptables.service
systemctl status iptables.service
