# Web Shop Playwright Automation

[![Playwright UI Tests](https://github.com/Vlady057/web-shop-playwright-automation/actions/workflows/ci.yml/badge.svg)](https://github.com/Vlady057/web-shop-playwright-automation/actions/workflows/ci.yml)

UI test automation project for the [Tricentis Demo Web Shop](https://demowebshop.tricentis.com/).

## Tech Stack

- Python
- Playwright
- Pytest
- pytest-html
- Page Object Model (POM)
- Git and GitHub
- GitHub Actions (CI)

## Test Coverage

The project includes automated UI tests covering the following areas.

### Login

- Verify that the login page is available.
- Verify validation for invalid login credentials.

### Registration

- Verify that the registration page is available.
- Register a new user with a unique email address.

### Product Search

- Search for products by keyword.
- Verify the search results.
- Verify the message displayed when no products match the search.

### Shopping Cart

- Open the shopping cart.
- Configure a product and add it to the cart.
- Verify the success notification and cart quantity.

### Logout

- Register a new user and verify that logout works.

## Test Results

Latest recorded local test run: **9 passed, 0 failed**.

The test suite is executed locally with Pytest and automatically in GitHub Actions.

### Test Report Screenshot

![Playwright HTML test report](screenshots/test-report.png)

The full HTML report is generated at `reports/report.html` when the report command is run locally. In GitHub Actions, the generated report is uploaded as a workflow artifact when available.

## Continuous Integration (CI)

This project uses GitHub Actions to automatically run the Playwright UI test suite.

The workflow is defined in `.github/workflows/ci.yml` and runs on:

- Pushes to the `main` branch.
- Pull requests targeting the `main` branch.
- Manual workflow runs from the GitHub Actions tab.

### CI Workflow

1. Checks out the repository.
2. Sets up Python 3.13.
3. Installs project dependencies.
4. Installs Playwright and Chromium.
5. Runs the automated UI tests with Pytest.
6. Uploads the HTML test report as a workflow artifact when available.

The workflow status is shown by the badge at the top of this README. A successful workflow indicates that all workflow steps, including the automated tests, completed successfully.

The HTML report artifact is retained for 14 days.

## Project Structure

```text
web-shop-playwright-automation/
├── .github/
│   └── workflows/
│       └── ci.yml
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── register_page.py
├── tests/
│   ├── test_cart.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_registration.py
│   └── test_search.py
├── utils/
│   └── __init__.py
├── reports/
│   └── report.html
├── screenshots/
│   └── test-report.png
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```powershell
git clone https://github.com/Vlady057/web-shop-playwright-automation.git
cd web-shop-playwright-automation
```

Create and activate a virtual environment on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies and Chromium:

```powershell
pip install -r requirements.txt
playwright install chromium
```

## Run Tests

Run the complete test suite:

```powershell
pytest
```

Run a specific test module:

```powershell
pytest tests/test_login.py -v
```

## Generate an HTML Report

```powershell
New-Item -ItemType Directory -Force reports
pytest --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to review the results.

## Design

The project follows the Page Object Model (POM) design pattern. Page classes contain locators and reusable UI actions, while test modules contain test scenarios and assertions.

Playwright's `page` fixture provides browser-page access. Pytest is used to organize and execute tests, and Playwright assertions verify the expected UI behavior.

Registration tests generate unique email addresses to avoid conflicts with existing accounts.
