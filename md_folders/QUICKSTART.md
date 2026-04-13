# 🚀 Quick Start Guide

Get the API Test Automation Framework running in **5 minutes**.

---

## 📦 Prerequisites

- **Python 3.10+** (3.10, 3.11, or 3.12)
- **pip** (comes with Python)
- **Git** (optional, for GitHub integration)

---

## 1️⃣ Installation

### Step 1: Clone the repository
```bash
git clone <your-repo-url>
cd API_Test_Automation
```

### Step 2: Create virtual environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

That's it! You're ready to run tests.

---

## 2️⃣ Run Your First Tests

### Basic test execution
```bash
pytest -v
```

**Expected Output:**
```
tests/test_users.py::test_get_users PASSED
tests/test_users.py::test_create_user PASSED
tests/test_users.py::test_get_user_by_id PASSED
tests/test_users.py::test_update_user PASSED
tests/test_users.py::test_delete_user PASSED
... 
7 passed in 2.34s
```

### With HTML report
```bash
pytest -v --html=reports/report.html --self-contained-html
```
Then open `reports/report.html` in your browser.

### Parallel execution (faster!)
```bash
pytest -n auto -v
```

---

## 3️⃣ Common Commands

### Run specific test file
```bash
pytest tests/test_users.py -v
```

### Run advanced tests
```bash
pytest tests/test_advanced.py -v
```

### Run only quick tests
```bash
pytest -m "not slow" -v
```

### Run with specific markers
```bash
pytest -m schema -v          # Schema validation tests
pytest -m negative -v        # Error scenario tests
pytest -m e2e -v             # End-to-end tests
```

### Run tests matching a pattern
```bash
pytest -k "create" -v        # Only tests with "create" in name
```

### Stop on first failure
```bash
pytest -x -v                 # Exit after first failure
```

### Verbose with print statements
```bash
pytest -v -s                 # Show print() output
```

---

## 4️⃣ Configuration

### Change API endpoint
Edit `.env` or set environment variable:

```bash
export BASE_URL=https://jsonplaceholder.typicode.com
pytest -v
```

### Switch environment
```bash
export ENV=staging
pytest -v   # Uses staging config
```

Available environments:
- `dev` (default) - localhost:3000
- `staging` - api-staging.example.com
- `prod` - api.example.com

### Set timeout
```bash
export TIMEOUT=15
pytest -v
```

---

## 5️⃣ Authentication Setup

### Method 1: No Auth (for public APIs)
```python
api_client.get("/endpoint")
```

### Method 2: JWT Token
```python
api_client.set_token("your-jwt-token-here", token_type="Bearer")
api_client.get("/protected-endpoint")
```

### Method 3: API Key
```python
api_client.set_header("X-API-Key", "your-api-key")
api_client.get("/endpoint")
```

### Method 4: Custom Auth
```python
api_client.set_header("Authorization", "Custom xyz123")
api_client.get("/endpoint")
```

For more examples, see [AUTHENTICATION_GUIDE.md](AUTHENTICATION_GUIDE.md)

---

## 6️⃣ Understanding the Project

### Project Structure
```
API_Test_Automation/
├── utils/                    # Core framework
│   ├── api_client.py        # HTTP client wrapper
│   ├── config.py            # Environment config
│   └── logger.py            # Logging utility
├── tests/                    # Test files
│   ├── test_users.py        # Basic tests (7 tests)
│   └── test_advanced.py     # Advanced tests (20+ tests)
├── data/                     # Test data
│   └── test_data.json       # Sample test data
├── reports/                  # Generated reports
│   └── report.html          # HTML test report
├── conftest.py              # Pytest fixtures & hooks
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Dependencies
├── .env.example             # Environment template
├── .github/
│   └── workflows/
│       └── tests.yml        # CI/CD pipeline
└── *.md files               # Documentation
```

### Key Files

| File | Purpose |
|------|---------|
| `utils/api_client.py` | Reusable HTTP client |
| `utils/config.py` | Environment settings |
| `conftest.py` | Test fixtures |
| `tests/test_users.py` | Basic test examples |
| `tests/test_advanced.py` | Advanced patterns |

---

## 7️⃣ Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'pytest'`
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Tests fail with connection error
**Solution:**
```bash
# Check your BASE_URL
export BASE_URL=https://jsonplaceholder.typicode.com
pytest -v
```

### Issue: Pytest not found
**Solution:**
```bash
# Make sure venv is activated
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

### Issue: Port already in use (for local API)
**Solution:**
```bash
export BASE_URL=http://localhost:3000  # Change port as needed
pytest -v
```

---

## 8️⃣ Advanced Features

### Schema Validation
```bash
pytest tests/test_advanced.py::TestSchemaValidation -v
```

### Negative Testing (Error Cases)
```bash
pytest tests/test_advanced.py::TestNegativeScenarios -v
```

### Edge Cases
```bash
pytest tests/test_advanced.py::TestEdgeCases -v
```

### Performance Testing
```bash
pytest -m performance -v
```

For full advanced examples, see [FEATURES.md](FEATURES.md) and [PYTEST_REFERENCE.md](PYTEST_REFERENCE.md)

---

## 9️⃣ Next Steps

1. ✅ Run the basic tests (see Step 2)
2. ✅ Configure your API endpoint (see Step 4)
3. ✅ Set up authentication if needed (see Step 5)
4. ✅ Explore the test files
5. ✅ Review [FEATURES.md](FEATURES.md) for advanced capabilities
6. ✅ Check [README.md](README.md) for complete documentation
7. ✅ Push to GitHub to trigger CI/CD pipeline

---

## 🎯 Common Workflows

### Local Development
```bash
# Run tests in watch mode (needs pytest-watch)
ptw

# Or run frequently
pytest tests/test_users.py -v --lf
```

### Before Commit
```bash
pytest -v --html=reports/report.html
# Check reports/report.html before committing
```

### CI/CD Testing
```bash
# GitHub Actions runs automatically
# Or simulate locally:
pytest -n auto -v --html=reports/report.html --junitxml=reports/junit.xml
```

### Performance Baseline
```bash
pytest --durations=10 -v
# Shows slowest 10 tests
```

---

## 📚 Learn More

- **Commands Reference:** [PYTEST_REFERENCE.md](PYTEST_REFERENCE.md)
- **Authentication Examples:** [AUTHENTICATION_GUIDE.md](AUTHENTICATION_GUIDE.md)
- **Feature Overview:** [FEATURES.md](FEATURES.md)
- **How to Contribute:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Full Documentation:** [README.md](README.md)

---

## ❓ Getting Help

1. Check [PYTEST_REFERENCE.md](PYTEST_REFERENCE.md) for command examples
2. Review [AUTHENTICATION_GUIDE.md](AUTHENTICATION_GUIDE.md) for auth patterns
3. Look at test examples in `tests/test_users.py` and `tests/test_advanced.py`
4. Check out [README.md](README.md) for comprehensive documentation

---

## 🎉 You're Ready!

Run this command to start:
```bash
pytest -v
```

**Happy Testing!** 🚀

---

**Need help?** Check the documentation files:
- `README.md` - Complete overview
- `FEATURES.md` - Feature highlights
- `PYTEST_REFERENCE.md` - Command reference
- `AUTHENTICATION_GUIDE.md` - Auth examples
