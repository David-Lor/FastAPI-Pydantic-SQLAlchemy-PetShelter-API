from .base_test import BaseAPITest


class TestAPI(BaseAPITest):
    def test_get_status(self):
        """Test the status endpoint of the API. Should return 200 with plain text 'OK'"""
        r = self.client.get("/status")
        assert r.status_code == 200
        assert r.text == "OK"
