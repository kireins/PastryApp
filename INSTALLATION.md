# 🔧 Installation & Deployment Guide

## System Requirements

### Minimum Specifications
- **OS**: Mac, Linux, or Windows with WSL
- **Python**: 3.8 or higher
- **MySQL**: 5.7 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Disk Space**: 500MB

### Required Software
- Python 3.8+
- MySQL Server
- Git (optional)
- Postman (for API testing, optional)
- Modern web browser

## 📥 Installation Steps

### Step 1: Install Python

#### macOS
```bash
# Using Homebrew
brew install python@3.10

# Verify installation
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3.10 python3-pip python3-venv

# Verify
python3 --version
```

#### Windows
- Download from python.org
- Run installer
- ✅ Check "Add Python to PATH"
- Verify in PowerShell: `python --version`

### Step 2: Install MySQL

#### macOS
```bash
# Using Homebrew
brew install mysql

# Start MySQL
brew services start mysql

# Secure installation
mysql_secure_installation
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install mysql-server

# Start MySQL
sudo systemctl start mysql

# Secure installation
sudo mysql_secure_installation
```

#### Windows
- Download MySQL installer from mysql.com
- Run installer
- Choose "Developer Default"
- Configure MySQL Server
- Start MySQL service

#### Verify Installation
```bash
mysql -u root -p
# Enter password, then type: exit
```

### Step 3: Clone/Download Project

```bash
# Create projects directory
mkdir -p ~/Documents/projects
cd ~/Documents/projects

# If using git (optional)
git clone <repository-url>

# Or download and extract ZIP file
# Then navigate to the directory
cd PastryApp
```

### Step 4: Set Up Python Environment

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### Step 5: Install Python Dependencies

```bash
# Make sure you're in the backend directory with venv activated
pip install -r requirements.txt

# Verify installation
pip list | grep Flask
```

### Step 6: Configure Environment Variables

Edit `backend/.env` file:

```bash
# macOS/Linux
nano .env

# Windows (use your preferred text editor)
# Or from PowerShell:
notepad .env
```

Set the following values:

```env
# Flask Environment
FLASK_ENV=development
FLASK_DEBUG=True

# JWT Configuration
JWT_SECRET_KEY=change_this_to_a_very_secure_random_string_in_production
JWT_ALGORITHM=HS256

# API Gateway
API_GATEWAY_PORT=5000
API_GATEWAY_DEBUG=True

# Microservices Ports
CUSTOMER_SERVICE_PORT=5001
RESTAURANT_SERVICE_PORT=5002
MENU_SERVICE_PORT=5003
ORDER_SERVICE_PORT=5004

# Microservices Base URLs
CUSTOMER_SERVICE_URL=http://localhost:5001
RESTAURANT_SERVICE_URL=http://localhost:5002
MENU_SERVICE_URL=http://localhost:5003
ORDER_SERVICE_URL=http://localhost:5004

# MySQL Configuration
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=pastry_db
MYSQL_PORT=3306
```

### Step 7: Initialize Database

```bash
# Make sure MySQL is running
# macOS/Linux: brew services start mysql
# Windows: Services app → MySQL → Start

# Run database initialization
python init_db.py

# Expected output:
# 🔧 Creating database and tables...
# ✅ All tables created successfully!
# ✅ Sample data inserted successfully!
```

### Step 8: Start Microservices

**Important**: Open 5 separate terminal windows!

#### Terminal 1: API Gateway
```bash
cd backend/api_gateway
python app.py
# Output: Running on http://0.0.0.0:5000
```

#### Terminal 2: Customer Service
```bash
cd backend/services/customer_service
python app.py
# Output: Running on http://0.0.0.0:5001
```

#### Terminal 3: Restaurant Service
```bash
cd backend/services/restaurant_service
python app.py
# Output: Running on http://0.0.0.0:5002
```

#### Terminal 4: Menu Service
```bash
cd backend/services/menu_service
python app.py
# Output: Running on http://0.0.0.0:5003
```

#### Terminal 5: Order Service
```bash
cd backend/services/order_service
python app.py
# Output: Running on http://0.0.0.0:5004
```

### Step 9: Start Frontend Server

Open a new terminal window:

```bash
cd frontend

# Python 3
python3 -m http.server 8000

# Or Python 2 (if available)
python -m SimpleHTTPServer 8000

# Output: Serving HTTP on 0.0.0.0 port 8000
```

### Step 10: Access Application

Open your browser:

- **Customer Interface**: http://localhost:8000/index.html
- **Admin Dashboard**: http://localhost:8000/admin.html
- **API Gateway Health**: http://localhost:5000/api/health

## 🐛 Troubleshooting Installation

### Python Not Found
```bash
# macOS/Linux: Use python3 instead of python
which python3
python3 --version

# Windows: Add Python to PATH
# Or reinstall Python with "Add Python to PATH" checked
```

### Port Already in Use
```bash
# Find process on port (macOS/Linux)
lsof -i :5000

# Kill process
kill -9 <PID>

# Or change ports in .env file
```

### MySQL Connection Failed
```bash
# Check if MySQL is running
# macOS:
brew services list | grep mysql

# Linux:
sudo systemctl status mysql

# Windows: Check Services app for MySQL service
```

### Permission Denied
```bash
# Make scripts executable (macOS/Linux)
chmod +x backend/init_db.py

# Or use python to run
python backend/init_db.py
```

### Virtual Environment Issues
```bash
# Deactivate and reactivate
deactivate
source venv/bin/activate

# Or delete and recreate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Production Deployment

### Pre-Deployment Checklist

- [ ] Change JWT_SECRET_KEY to random 32+ character string
- [ ] Change MySQL password from default
- [ ] Set FLASK_ENV=production
- [ ] Disable Flask debug mode
- [ ] Enable HTTPS/SSL certificates
- [ ] Configure CORS for production domain
- [ ] Set up database backups
- [ ] Configure logging
- [ ] Test all endpoints
- [ ] Review security settings

### Production Environment (.env)

```env
FLASK_ENV=production
FLASK_DEBUG=False
JWT_SECRET_KEY=<very_long_random_string>
MYSQL_PASSWORD=<strong_password>
# Restrict CORS to production domain only
```

### Deployment Options

#### Option 1: Using Gunicorn (Recommended)

```bash
# Install Gunicorn
pip install gunicorn

# Run API Gateway with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Run each service similarly
```

#### Option 2: Docker (Advanced)

Create `Dockerfile` for each service:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

#### Option 3: Cloud Deployment

Services can be deployed to:
- **AWS**: EC2, Lambda, RDS for MySQL
- **Heroku**: Using Procfile
- **DigitalOcean**: Droplets or App Platform
- **Google Cloud**: Compute Engine, Cloud SQL

### Production Architecture

```
┌─────────────────────────────────────────┐
│      Nginx / Load Balancer              │
│         (HTTPS/SSL)                     │
└────────────────┬────────────────────────┘
                 │
         ┌───────┴────────┐
         ↓                ↓
    ┌────────┐       ┌────────┐
    │App     │       │App     │
    │Server  │       │Server  │
    │Instance│       │Instance│
    │1       │       │2       │
    └────────┘       └────────┘
         │                │
         └────────┬───────┘
                  ↓
         ┌───────────────────┐
         │  MySQL Database   │
         │   (RDS/Managed)   │
         └───────────────────┘
```

## 🔒 Security Hardening

### 1. Environment Variables
- Never commit `.env` to Git
- Use `.gitignore` to exclude `.env`
- Use different credentials per environment

### 2. Database Security
```sql
-- Create database user (not root)
CREATE USER 'pastry_user'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON pastry_db.* TO 'pastry_user'@'localhost';
FLUSH PRIVILEGES;
```

### 3. JWT Security
- Use strong secret key (minimum 32 characters)
- Implement token expiration (currently no expiry)
- Rotate keys periodically

### 4. CORS Configuration
```python
# production
CORS(app, resources={r"/api/*": {"origins": ["https://yourdomain.com"]}})
```

### 5. HTTPS Setup
- Get SSL certificate (Let's Encrypt recommended)
- Configure Nginx reverse proxy
- Redirect HTTP to HTTPS

### 6. Input Validation
- Validate all user inputs
- Sanitize data before database insertion
- Use parameterized queries (already implemented)

## 📊 Performance Monitoring

### Logging Setup

```python
import logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Database Optimization
- Add indexes on frequently queried columns
- Monitor query performance
- Use connection pooling

### Caching Strategy
- Cache menu items (rarely change)
- Cache restaurant data
- Use Redis for session management

## 🔄 Maintenance Tasks

### Regular Backups
```bash
# Backup MySQL database
mysqldump -u root -p pastry_db > backup_$(date +%Y%m%d).sql

# Restore from backup
mysql -u root -p pastry_db < backup_20231113.sql
```

### Log Rotation
- Configure logrotate (Linux)
- Implement log archival
- Monitor log disk space

### Updates & Patches
- Keep Python updated
- Update dependencies regularly: `pip list --outdated`
- Update MySQL security patches

## 📚 Documentation

- **README.md**: Complete project documentation
- **QUICKSTART.md**: 5-minute setup guide
- **ARCHITECTURE.md**: System design and structure
- **API Documentation**: Postman collection included

## 🆘 Getting Help

If you encounter issues:

1. **Check Logs**: Review terminal output and log files
2. **Verify Requirements**: Ensure all prerequisites installed
3. **Check Connectivity**: Verify all services running
4. **Review Documentation**: Check README and QUICKSTART
5. **Test Individually**: Test each service with curl/Postman

---

**Installation Complete! 🎉**

Next steps:
1. Follow QUICKSTART.md for testing
2. Review API endpoints in Postman collection
3. Customize menu items and data
4. Deploy to production

