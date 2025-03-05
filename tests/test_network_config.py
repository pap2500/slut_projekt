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
    