# Contributing to API Test Automation Framework

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 🤝 How to Contribute

### 1. Fork & Clone
```bash
git clone https://github.com/your-username/api-test-framework.git
cd api-test-framework
```

### 2. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes
- Follow existing code style
- Add tests for new features
- Update documentation

### 4. Commit with Clear Messages
```bash
git commit -m "feat: add new authentication feature"
```

### 5. Push & Create Pull Request
```bash
git push origin feature/your-feature-name
```

## 📋 Contribution Guidelines

### Code Style
- Follow PEP 8
- Use type hints where possible
- Include docstrings for functions and classes
- Use meaningful variable names

### Testing Requirements
- All new features must include tests
- Minimum 80% code coverage
- Tests must pass locally before PR
- Include both positive and negative test cases

### Commit Message Format
```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `test:` Adding tests
- `docs:` Documentation changes
- `refactor:` Code refactoring
- `chore:` Maintenance tasks

### Examples
```
feat: add JWT token refresh support
fix: correct timeout handling in api_client
test: add edge case tests for unicode characters
docs: update authentication guide with examples
```

## 🏗️ Project Structure Guidelines

- `tests/test_*.py` - Test files
- `utils/` - Helper modules
- `data/` - Test data files
- `reports/` - Generated reports (don't commit)

## ✅ Before Submitting PR

- [ ] Code follows PEP 8
- [ ] All tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] No hardcoded secrets or tokens
- [ ] Commit messages are clear

## 🐛 Reporting Bugs

Create an issue with:
1. **Title:** Clear bug description
2. **Environment:** Python version, OS, pytest version
3. **Steps to reproduce:** Exact steps to recreate
4. **Expected behavior:** What should happen
5. **Actual behavior:** What actually happens
6. **Screenshots/logs:** If applicable

## 💡 Suggesting Features

Create an issue with:
1. **Title:** Feature request
2. **Motivation:** Why this feature is useful
3. **Use cases:** Real-world examples
4. **Implementation ideas:** Optional suggestions

## 🔍 Code Review Process

1. PR is reviewed by maintainers
2. Feedback provided if changes needed
3. Updates requested are addressed
4. PR merged once approved

## 📚 Documentation

When adding features:
- Update README.md
- Add examples in AUTHENTICATION_GUIDE.md if auth-related
- Update PYTEST_REFERENCE.md with new commands
- Add docstrings to code

## 🎓 Learning Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Requests Library](https://requests.readthedocs.io/)
- [JSON Schema](https://json-schema.org/)
- [Python Best Practices](https://pep8.org/)

## 📞 Questions?

- Open an issue with `question:` label
- Check existing issues first
- Be respectful and clear

## 🙏 Thank You!

Your contributions help make this framework better for everyone!

---

**Happy Contributing!** 🚀
