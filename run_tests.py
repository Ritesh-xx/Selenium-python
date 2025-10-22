import pytest

if __name__ == "__main__":
    pytest.main([
        "-s",
        "tests/",
        "--html=reports/report.html",             # Pytest HTML report
        "--self-contained-html",                  # Embed CSS/JS
        "--alluredir=reports/allure-results",     # ✅ Needed for Allure results
        "--headless",                             # Custom flag for your browser setup
        "-n", "4"                                  # Run in 4 parallel processes
    ])
