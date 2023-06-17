from solutions.CHK import checkout


class TestCheckout:
    def test_checkout(self):
        assert checkout("AAAB") == 160
