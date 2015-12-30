from fabric.api import *


def restart_servers():
    sudo('service tomcat7 restart')


"""
Restart the Master Node, could take up to 1hr to reload the cache and fully restart
"""
env.user = 'user'
env.password = 'pwd'
env.hosts = [
    '10.112.91.142']

results = execute(restart_servers)


"""
Restart the 3 servers AV created for Optimization
"""
env.user = 'user1'
env.password = 'pwd1'
env.hosts = [
    '10.112.91.203',
    '10.112.91.202',
    '10.112.91.182']

results = execute(restart_servers)



"""
Restart the 6 servers Frontier installed for Optimization
"""
env.user = 'user2'
env.password = 'pwd2'
env.hosts = [
    '10.112.91.184',
    '10.112.91.186',
    '10.112.91.190',
    '10.112.91.191',
    '10.112.91.192',
    '10.112.91.199']

results = execute(restart_servers)