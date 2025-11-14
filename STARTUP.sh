#!/bin/bash

# ============================================================================
# PastryApp - Complete Startup Script
# ============================================================================
# This script starts all services and the frontend for the Pastry delivery app
# ============================================================================

set -e  # Exit on error

BACKEND_DIR="/Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/backend"
FRONTEND_DIR="/Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/frontend"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🍰 Welcome to PastryApp Startup Script${NC}"
echo "=================================="
echo ""

# Function to check if port is in use
check_port() {
    local port=$1
    if netstat -an | grep -q ".*\.$port.*LISTEN"; then
        return 0
    else
        return 1
    fi
}

# Kill any existing Python processes on app ports
echo -e "${YELLOW}🛑 Cleaning up old processes...${NC}"
killall Python 2>/dev/null || true
sleep 1

# Initialize database
echo -e "${YELLOW}📊 Initializing database...${NC}"
cd "$BACKEND_DIR"
source venv/bin/activate
python app.py init_db 2>/dev/null || python3 init_db.py
echo -e "${GREEN}✅ Database initialized${NC}"
echo ""

# Start services in background
echo -e "${YELLOW}🚀 Starting microservices...${NC}"
echo ""

# API Gateway (Port 5050)
echo -e "${BLUE}Starting API Gateway (Port 5050)...${NC}"
cd "$BACKEND_DIR/api_gateway"
nohup python app.py > /tmp/api_gateway.log 2>&1 &
API_GATEWAY_PID=$!
sleep 2
if check_port 5050; then
    echo -e "${GREEN}✅ API Gateway is running (PID: $API_GATEWAY_PID)${NC}"
else
    echo -e "${RED}❌ API Gateway failed to start${NC}"
    cat /tmp/api_gateway.log
    exit 1
fi

# Customer Service (Port 5001)
echo -e "${BLUE}Starting Customer Service (Port 5001)...${NC}"
cd "$BACKEND_DIR/services/customer_service"
nohup python app.py > /tmp/customer_service.log 2>&1 &
CUSTOMER_PID=$!
sleep 2
if check_port 5001; then
    echo -e "${GREEN}✅ Customer Service is running (PID: $CUSTOMER_PID)${NC}"
else
    echo -e "${RED}❌ Customer Service failed to start${NC}"
    cat /tmp/customer_service.log
fi

# Menu Service (Port 5003)
echo -e "${BLUE}Starting Menu Service (Port 5003)...${NC}"
cd "$BACKEND_DIR/services/menu_service"
nohup python app.py > /tmp/menu_service.log 2>&1 &
MENU_PID=$!
sleep 2
if check_port 5003; then
    echo -e "${GREEN}✅ Menu Service is running (PID: $MENU_PID)${NC}"
else
    echo -e "${RED}❌ Menu Service failed to start${NC}"
    cat /tmp/menu_service.log
fi

# Order Service (Port 5004)
echo -e "${BLUE}Starting Order Service (Port 5004)...${NC}"
cd "$BACKEND_DIR/services/order_service"
nohup python app.py > /tmp/order_service.log 2>&1 &
ORDER_PID=$!
sleep 2
if check_port 5004; then
    echo -e "${GREEN}✅ Order Service is running (PID: $ORDER_PID)${NC}"
else
    echo -e "${RED}❌ Order Service failed to start${NC}"
    cat /tmp/order_service.log
fi

echo ""
echo -e "${YELLOW}🌐 Starting Frontend Server (Port 8000)...${NC}"
cd "$FRONTEND_DIR"
nohup python3 -m http.server 8000 > /tmp/frontend.log 2>&1 &
FRONTEND_PID=$!
sleep 2
if check_port 8000; then
    echo -e "${GREEN}✅ Frontend Server is running (PID: $FRONTEND_PID)${NC}"
else
    echo -e "${RED}❌ Frontend Server failed to start${NC}"
    cat /tmp/frontend.log
fi

echo ""
echo -e "${GREEN}=================================="
echo "🎉 All Services Started Successfully!"
echo "=================================="
echo ""
echo -e "${BLUE}📱 Access the Application:${NC}"
echo -e "  Customer Interface: ${YELLOW}http://localhost:8000/index.html${NC}"
echo -e "  Admin Dashboard:    ${YELLOW}http://localhost:8000/admin.html${NC}"
echo ""
echo -e "${BLUE}🔐 Test Credentials:${NC}"
echo -e "  Customer: ${YELLOW}username: customer${NC} | ${YELLOW}password: iamcustomer${NC}"
echo -e "  Admin:    ${YELLOW}username: admin${NC} | ${YELLOW}password: iamadmin${NC}"
echo ""
echo -e "${BLUE}🔌 Services Running On:${NC}"
echo -e "  API Gateway:      ${YELLOW}http://localhost:5050${NC}"
echo -e "  Customer Service: ${YELLOW}http://localhost:5001${NC}"
echo -e "  Menu Service:     ${YELLOW}http://localhost:5003${NC}"
echo -e "  Order Service:    ${YELLOW}http://localhost:5004${NC}"
echo ""
echo -e "${YELLOW}📝 Log Files:${NC}"
echo "  /tmp/api_gateway.log"
echo "  /tmp/customer_service.log"
echo "  /tmp/menu_service.log"
echo "  /tmp/order_service.log"
echo "  /tmp/frontend.log"
echo ""
echo -e "${YELLOW}🛑 To stop all services, run:${NC}"
echo "  killall Python"
echo ""
