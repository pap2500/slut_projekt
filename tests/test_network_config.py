import pytest
from network_config_manager import NetworkConfigManager

class TestNetworkConfigManager:
    def setup_method(self):
        self.conn = NetworkConfigManager()
        self.conn.connect()
        self.conn.update_hostname('1')
        self.conn.update_interface_state('down')
        self.conn.update_response_prefix('Standard Response')
    
    def test_show_response_prefix(self):
        response = self.conn.show_response_prefix()
        assert response == 'response_prefix: Standard Response'

    def test_update_response_prefix(self):
        self.conn.update_response_prefix('New Response')
        response = self.conn.show_response_prefix()
        assert response == 'response_prefix: New Response'

    def teardown_method(self):
        self.conn.disconnect()