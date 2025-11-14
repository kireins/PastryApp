#!/bin/bash

# Start Customer Service (Port 5001)
echo "🚀 Starting Customer Service (Port 5001)..."
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/backend
source venv/bin/activate
cd services/customer_service
python app.py
