from test_requests.api.wework import WeWork


class TestWeWork:
    def test_get_token(self):
        secrete = 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'
        print(WeWork().get_token(secrete))