from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout(self):
        assert checkout_solution.checkout("AAAB") == 160

    def test_checkout_incorrect_item(self):
        assert checkout_solution.checkout("AAaB") == -1


