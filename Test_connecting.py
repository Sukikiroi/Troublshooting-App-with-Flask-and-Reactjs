from demo_simple import connecting
from demo_simple_scp import connecting_scp

def do_ssh(ip):
 connecting(ip)
 connecting_scp(ip)


do_ssh('10.205.14.60')