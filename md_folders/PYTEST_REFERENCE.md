# Pytest Command Reference Guide

## Basic Commands

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_users.py

# Run specific test class
pytest tests/test_users.py::TestUserAPI

# Run specific test
pytest tests/test_users.py::TestUserAPI::test_get_users

# Stop on first failure
pytest -x

# Run last failed tests
pytest --lf

# Show local variables on failure
pytest -l
```

## Useful Options

```bash
# Verbose output with short traceback
pytest -v --tb=short

# Show print statements
pytest -s

# Quiet mode (only show summary)
pytest -q

# Show warnings
pytest -W

# Capture output
pytest --capture=no
```

## Parallel Execution (pytest-xdist)

```bash
# Run tests in parallel (auto-detect CPU cores)
pytest -n auto

# Run with 4 workers
pytest -n 4

# Run with specific number of workers and verbose
pytest -n 4 -v
```

## Markers and Filtering

```bash
# Run only smoke tests
pytest -m smoke

# Run all except slow tests
pytest -m "not slow"

# Run positive tests only
pytest -m positive

# Run regression tests
pytest -m regression

# Run multiple markers
pytest -m "positive and not slow"
```

## Reporting

```bash
# Generate HTML report (self-contained)
pytest --html=reports/report.html --self-contained-html

# Generate Allure report
pytest --alluredir=reports/allure

# View Allure report in browser
allure serve reports/allure

# Generate JSON report
pytest --json-report --json-report-file=reports/report.json

# Generate JUnit XML (for CI/CD)
pytest --junit-xml=reports/junit.xml
```

## Environment Variables

```bash
# Set environment to staging
export ENV=staging
pytest -v

# Set custom base URL
export BASE_URL=https://api-staging.example.com
pytest -v

# Change timeout
export TIMEOUT=20
pytest -v
```

## Coverage Analysis (with pytest-cov)

```bash
# Generate coverage report
pytest --cov=utils --cov-report=html

# Show coverage summary
pytest --cov=utils --cov-report=term
```

## Debugging

```bash
# Run with Python debugger on failure
pytest --pdb

# Drop into debugger at start of test
pytest --trace

# Show fixture setup/teardown
pytest --setup-show

# Show test collection
pytest --collect-only
```

## Real-world Examples

```bash
# Run all tests, parallel, with HTML + Allure reports
pytest -n auto -v --html=reports/report.html --self-contained-html --alluredir=reports/allure

# Run only smoketests in parallel
pytest -m smoke -n 4 -v

# Run tests excluding slow ones, with coverage
pytest -m "not slow" --cov=utils --cov-report=html

# Run with custom base URL (staging)
export BASE_URL=https://api-staging.example.com
pytest tests/test_users.py -v

# Run in strict mode (all warnings = errors)
pytest -W error --strict-markers

# Run and save results for later analysis
pytest -v --junit-xml=reports/junit.xml --json-report --json-report-file=reports/report.json
```

## CI/CD Integration

```bash
# For GitHub Actions
pytest -v --junit-xml=reports/junit.xml --html=reports/report.html --self-contained-html

# For GitLab CI
pytest -v --junit-xml=reports/junit.xml

# For Jenkins
pytest -v --html=reports/report.html --junit-xml=reports/junit.xml
```

## Performance Testing

```bash
# Show slowest tests
pytest -v --durations=10

# Only run tests slower than specific time (seconds)
pytest -v --durations-min=1

# Show all durations
pytest -v --durations=0
```
