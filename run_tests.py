import pytest

if __name__ == "__main__":
    pytest.main([
        "-s",                     # print output to console
        "tests/",                 # folder to run tests from
        "--html=reports/report.html",  # generate HTML report
        "--self-contained-html",  # embed CSS in the HTML report
        "--headless"              # run tests in headless mode (added)
    ])
