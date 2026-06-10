#!/bin/bash
# Environment setup for development and CI
set -e
echo "Setting up development environment..."
pip install -r requirements.txt
echo "Running environment validation..."
make validate
echo "Setup complete."
