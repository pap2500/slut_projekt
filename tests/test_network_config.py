import pytest
from network_config_manager import NetworkConfigManager

class TestNetworkConfigManager:
    @pytest.fixture
    def connection(self):
        conn = NetworkConfigManager()
        conn.connect()
   
        yield conn
        conn.disconnect()
    
    
    @pytest.fixture
    def connection_method(self, connection):
        connection.update_hostname('1')
        connection.update_interface_state('down')
        connection.update_response_prefix('Standard Response')
   
        return connection
    
    
    def test_update_host_name(self, connection_method):
        connection_method.update_hostname('2')
        host_name = connection_method.show_hostname()
        assert host_name == 'hostname: 2'


    def test_show_response_prefix(self, connection_method):
        response = connection_method.show_response_prefix()
        assert response == 'response_prefix: Standard Response'


    def test_update_response_prefix(self, connection_method):
        connection_method.update_response_prefix('New Response')
        response = connection_method.show_response_prefix()
        assert response == 'response_prefix: New Response'
        
        
    def test_update_interface_state_error(self, connection):
        with pytest.raises(ValueError):
            connection.update_interface_state('upp')
