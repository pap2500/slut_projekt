import pytest
from network_config_manager import NetworkConfigManager


class TestNetworkConfigManager:
    @pytest.fixture
    def connection_method(self):

        conn = NetworkConfigManager()
        
        conn.connect()
        
        conn.update_hostname('1')
        
        conn.update_interface_state('down')
        
        conn.update_response_prefix('Standard Response')
   

      
               
        
        yield conn
        conn.disconnect()
        
        
      
    def test_show_interface_state(self, connection_method):
            # en simpel funktion som returerar om värdet på interface_state är down
            assert connection_method.show_interface_state() == 'interface_state: down'

    def test_update_interface_state(self, connection_method):
            # en simpel funktion som updaterar värdet på interface_state och sedan verifierar uppdateringen
             connection_method.update_interface_state('up')
             assert connection_method.show_interface_state() == 'interface_state: up'   