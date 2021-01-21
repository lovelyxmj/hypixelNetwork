import os

localip=input('内网ip')
remoteip=input('要加速的服务器ip')


shell = 'iptables -F'
shell1='iptables -X'
shell2='iptables -Z'
shell3=f'iptables -t nat -A PREROUTING -d {localip} -p tcp --dport 25565 -j DNAT --to-destination {remoteip}:25565'
shell4=f'iptables -t nat -A POSTROUTING -d {remoteip} -p tcp --dport 25565 -j SNAT --to {localip}'
shell5=f'iptables -A FORWARD -o eth0 -d {remoteip} -p tcp --dport 25565 -j ACCEPT'
shell6=f'iptables -A FORWARD -i eth0 -s {remoteip} -p tcp --sport 25565 -j ACCEPT'
shell7='echo 1 >/proc/sys/net/ipv4/ip_forward'

os.system(shell)
os.system(shell1)
os.system(shell2)
os.system(shell3)
os.system(shell4)
os.system(shell5)
os.system(shell6)
os.system(shell7)