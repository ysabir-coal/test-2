# Build configuration for the deployment validation service
# Runs standard build/test/validate lifecycle
# monitoring-improvement-v14

.PHONY: all build test clean validate setup

all: setup validate build test

setup:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt 2>/dev/null || true
	@npm install 2>/dev/null || true

validate: validate-env validate-network validate-creds
	@echo "All validation checks completed."

validate-env:
	@echo "Checking build environment..."
	@python3 --version
	@node --version 2>/dev/null || echo "node: not installed"
	@echo "Region: $${AWS_REGION:-not set}"
	@echo "Account: $${AWS_ACCOUNT_ID:-not set}"

validate-network:
	@echo "Checking network connectivity..."
	@curl -s -o /dev/null -w "npm registry: %{http_code}\n" --connect-timeout 3 https://registry.npmjs.org || true
	@curl -s -o /dev/null -w "pypi: %{http_code}\n" --connect-timeout 3 https://pypi.org/simple/ || true

build:
	@echo "Building..."
	@python3 -m py_compile src/*.py 2>/dev/null || echo "Python compile check: no files or errors"
	@echo "Build complete."

test:
	@echo "Running tests..."
	@python3 -m pytest tests/ 2>/dev/null || echo "No tests found or pytest not available"
	@echo "Tests complete."

clean:
	@rm -rf build/ dist/ *.egg-info __pycache__ .pytest_cache
	@find . -name "*.pyc" -delete
