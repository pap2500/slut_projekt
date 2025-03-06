import pytest
from network_config_manager import NetworkConfigManager

class TestNetworkCongigManager:
  
    @pytest.fixture

    def connect_method (self):
        conn = NetworkConfigManager()
        conn.connect ()
        conn.update_hostname ('1')
        conn.update_interface_state('down')
        conn.update_response_prefix ('Standard Response')

        yield conn
        conn.disconnect()

    #Metod som kollar att hostname är rätt

    def test_show_hostname (self, connect_method):
        connect_method.show_hostname ()
        host_name = connect_method.show_hostname ()
        assert host_name == 'hostname: 1'


    #Metod som updaterar hostname

    def test_update_hostname (self, connect_method):
        connect_method.update_hostname ('2')
        host_name = connect_method.show_hostname ()
        assert host_name == 'hostname: 2'

    