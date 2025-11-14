#!/bin/bash

# Navigate to the PastryApp directory
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp

# Activate virtual environment
source backend/venv/bin/activate

echo "✅ Virtual environment activated"
echo "📍 Current directory: $(pwd)"
echo "🐍 Python version: $(python --version)"
echo ""

# Start API Gateway
echo "🚀 Starting API Gateway (Port 5000)..."
cd backend/api_gateway
python app.py
