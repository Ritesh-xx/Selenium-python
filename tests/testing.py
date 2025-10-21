import allure

def test_simple_steps():
    with allure.step("Step 1: Open home page"):
        pass
    with allure.step("Step 2: Click button"):
        pass
    with allure.step("Step 3: Verify result"):
        assert True
