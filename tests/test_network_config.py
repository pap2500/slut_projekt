import pytest
from network_config_manager import NetworkConfigManager

class TestNetworkCongigManager:
    
    def setup_method (self):
        self.conn = NetworkConfigManager()
        self.conn.connect ()
        self.conn.update_hostname('1')
        self.conn.update_interface_state('down')
        self.conn.update_response_prefix ('Standard Response')

#Metod som kollar att hostname är rätt

    def test_show_hostname (self):
        host_name = self.conn.show_hostname()
        assert host_name == 'hostname: 1'

#Metod som updaterar hostname

    def test_update_hostname (self):
        self.conn.update_hostname('2')
        host_name = self.conn.show_hostname()
        assert host_name == 'hostname: 2'


#show_hostname = ConnectHandler (**server)
#command = "cat /etc/config/hostname/config.txt"
#output = show_hostname.send_command (command)
#print (output)


#update_hostname = ConnectHandler (**server)
#command = f"bash -c \"echo 'hostname: {3}' > /etc/config/hostname/config.txt\""
#output = update_hostname.send_command (command)
#print (output)



#net_connect = ConnectHandler(**server)
#print("Conneted to server")
#command = "cat /etc/config/hostname/config.txt"
#output = net_connect.send_command(command)
#print (output)