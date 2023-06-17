from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout(self):
        assert checkout_solution.checkout("AAAB") == 160

    def test_checkout_incorrect_item(self):
        assert checkout_solution.checkout("AAaB") == -1

    def test_checkout_2E_and_B(self):
        assert checkout_solution.checkout("EEB") == 80

    def test_checkout_4E_and_3B(self):
        assert checkout_solution.checkout("EEEEBBB") == 190

    def test_checkout_E(self):
        assert checkout_solution.checkout("E") == 40

