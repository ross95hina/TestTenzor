class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)
        return get_url

    """Method assert word"""

    def assert_word(self, word, result, msg1, msg2):
        value_word = word
        assert value_word == result, msg2
        print(msg1)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL is right")


