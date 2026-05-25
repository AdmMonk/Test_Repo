# 🌍 Geospatial Data Manager with OCR

A comprehensive geospatial data management system with integrated OCR (Optical Character Recognition) capabilities. Built with Spring Boot, Angular, PostgreSQL, and Python.

## 🚀 Quick Start

### Windows (Single Command)
```bash
# Setup everything (run as administrator)
setup-windows.bat

# Start the system
start-complete-system-with-ocr.bat
```

### Linux (Single Command)
```bash
# Setup everything
chmod +x setup-linux.sh
./setup-linux.sh

# Start the system
./start-system.sh
```

## 📋 System Overview

### Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Angular        │    │  Spring Boot    │    │  PostgreSQL     │
│  Frontend       │◄──►│  Backend        │◄──►│  Database       │
│  (Port 4200)    │    │  (Port 8080)    │    │  (Port 5432)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐
│  Python OCR     │
│  Service        │
│  (Port 5000)    │
└─────────────────┘
```

### Components
- **🅰️ Angular Frontend**: Modern web interface with Material Design
- **☕ Spring Boot Backend**: RESTful API and business logic
- **🐘 PostgreSQL Database**: Reliable data persistence
- **🐍 Python OCR Service**: Industry-grade document processing

## 🛠️ Prerequisites

### Required Software
- **Java 17+** - [Download](https://adoptium.net/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **Python 3.8+** - [Download](https://python.org/)
- **PostgreSQL 12+** - [Download](https://postgresql.org/)
- **Maven 3.6+** - [Download](https://maven.apache.org/)

### Optional (for better OCR)
- **Tesseract OCR** - [Windows](https://github.com/UB-Mannheim/tesseract/wiki) | [Linux](https://tesseract-ocr.github.io/)

## 📦 Installation

### Automated Setup

#### Windows
1. **Download/Clone the repository**
2. **Run as Administrator:**
   ```cmd
   setup-windows.bat
   ```
3. **Start the system:**
   ```cmd
   start-complete-system-with-ocr.bat
   ```

#### Linux
1. **Download/Clone the repository**
2. **Run setup:**
   ```bash
   chmod +x setup-linux.sh
   ./setup-linux.sh
   ```
3. **Start the system:**
   ```bash
   ./start-system.sh
   ```

### Manual Setup

#### 1. Database Setup
```sql
-- Create database
CREATE DATABASE geospatial_db;
CREATE USER geospatial_user WITH ENCRYPTED PASSWORD 'geospatial_pass';
GRANT ALL PRIVILEGES ON DATABASE geospatial_db TO geospatial_user;

-- Run schema
psql -d geospatial_db -f src/main/resources/schema.sql
```

#### 2. Backend Setup
```bash
# Build Spring Boot application
mvn clean package -DskipTests

# Run application
java -jar target/geospatial-data-manager-*.jar
```

#### 3. OCR Service Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Start OCR service
cd Ocr-cursor
python industry_ocr_app.py
```

#### 4. Frontend Setup
```bash
# Install dependencies
cd intelligence-angular
npm install

# Start development server
ng serve
```

## 🎯 Usage

### Accessing the Application
1. **Open browser**: `http://localhost:4200`
2. **Navigate to sections**:
   - Dashboard: Overview and statistics
   - OCR Processor: Document processing
   - Records Table: Data management
   - Map View: Geospatial visualization

### OCR Document Processing
1. **Go to OCR Processor section**
2. **Upload documents**:
   - Drag & drop files
   - Or click "Browse Files"
   - Supported: PDF, JPG, PNG, TIFF, BMP
3. **Process files**: Click "Process Files"
4. **View results**: Check processing history
5. **Download text**: Click download button

### API Endpoints

#### Spring Boot Backend (Port 8080)
```
GET    /api/records          - Get all records
POST   /api/records          - Create new record
PUT    /api/records/{id}     - Update record
DELETE /api/records/{id}     - Delete record
GET    /actuator/health      - Health check
```

#### OCR Service (Port 5000)
```
POST   /api/ocr/process      - Process document
GET    /api/ocr/jobs         - Get OCR jobs
DELETE /api/ocr/jobs/{id}    - Delete OCR job
GET    /api/health           - Health check
GET    /api/info             - System info
```

## 🔧 Configuration

### Database Configuration
Edit `src/main/resources/application.properties`:
```properties
spring.datasource.url=jdbc:postgresql://localhost:5432/geospatial_db
spring.datasource.username=geospatial_user
spring.datasource.password=geospatial_pass
```

### OCR Service Configuration
Edit `Ocr-cursor/industry_ocr_app.py`:
```python
# Change port
app.run(host='0.0.0.0', port=5000)

# Enable debug mode
app.run(debug=True)
```

### Angular Configuration
Edit `intelligence-angular/src/environments/environment.ts`:
```typescript
export const environment = {
  production: false,
  apiUrl: 'http://localhost:8080/api',
  ocrUrl: 'http://localhost:5000/api'
};
```

## 🧪 Testing

### System Health Check
```bash
# Windows
python check-system-status.py

# Linux
python3 check-system-status.py
```

### Individual Service Tests
```bash
# Test OCR service
cd Ocr-cursor
python test_ocr_service.py

# Test Spring Boot
curl http://localhost:8080/actuator/health

# Test Angular
curl http://localhost:4200
```

## 📊 Features

### Core Features
- ✅ **Geospatial Data Management**: CRUD operations for spatial data
- ✅ **Interactive Maps**: Leaflet-based map visualization
- ✅ **OCR Processing**: Multi-engine document text extraction
- ✅ **Real-time Updates**: Live processing status
- ✅ **Responsive Design**: Works on desktop and mobile
- ✅ **RESTful APIs**: Standard HTTP interfaces

### OCR Features
- 🔍 **Multi-Engine OCR**: Tesseract + Enhanced processing
- 🖼️ **Image Preprocessing**: Denoising, enhancement, deskewing
- 📄 **Format Support**: PDF, JPG, PNG, TIFF, BMP
- 📈 **Accuracy Scoring**: Confidence metrics for results
- 📥 **Batch Processing**: Multiple file handling
- 💾 **Result Management**: Download and delete processed jobs

### Technical Features
- 🏗️ **Microservices Architecture**: Loosely coupled components
- 🔒 **CORS Support**: Cross-origin request handling
- 📝 **Comprehensive Logging**: Detailed system logs
- 🔄 **Auto-restart**: Service recovery mechanisms
- 📊 **Health Monitoring**: System status endpoints

## 🐛 Troubleshooting

### Common Issues

#### Services Not Starting
```bash
# Check if ports are in use
netstat -an | grep :4200  # Angular
netstat -an | grep :8080  # Spring Boot
netstat -an | grep :5000  # OCR Service
netstat -an | grep :5432  # PostgreSQL

# Kill processes if needed
# Windows: taskkill /f /im java.exe
# Linux: pkill -f java
```

#### Database Connection Issues
```bash
# Check PostgreSQL status
# Windows: net start postgresql-x64-14
# Linux: sudo systemctl status postgresql

# Test connection
psql -U geospatial_user -d geospatial_db -h localhost
```

#### OCR Service Issues
```bash
# Check Python dependencies
pip list | grep -E "(flask|opencv|pillow)"

# Test OCR core
python -c "from Ocr-cursor.industry_ocr_core import create_industry_ocr_system; print('OK')"
```

#### Frontend Build Issues
```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

### Performance Optimization

#### Database
```sql
-- Create indexes for better performance
CREATE INDEX idx_records_created_at ON records(created_at);
CREATE INDEX idx_ocr_jobs_status ON ocr_jobs(status);
```

#### OCR Service
```python
# Increase worker threads
app.run(threaded=True, processes=4)

# Enable GPU acceleration (if available)
# Uncomment GPU dependencies in requirements.txt
```

## 📈 Monitoring

### System Logs
```bash
# View logs
tail -f logs/spring-boot.log    # Backend logs
tail -f logs/ocr-service.log    # OCR logs
tail -f logs/angular-build.log  # Frontend logs
```

### Performance Metrics
- **Response Times**: Monitor API endpoint performance
- **OCR Accuracy**: Track confidence scores
- **Resource Usage**: CPU, memory, disk usage
- **Error Rates**: Monitor failed requests

## 🔒 Security

### Production Considerations
- Change default passwords
- Enable HTTPS/SSL
- Configure firewall rules
- Set up authentication
- Regular security updates

### Environment Variables
```bash
# Set production environment
export SPRING_PROFILES_ACTIVE=production
export NODE_ENV=production
export FLASK_ENV=production
```

## 🚀 Deployment

### Docker Deployment
```dockerfile
# Example Dockerfile structure
FROM openjdk:17-jdk-slim
FROM node:18-alpine
FROM python:3.9-slim
FROM postgres:14
```

### Cloud Deployment
- **AWS**: EC2, RDS, S3
- **Azure**: App Service, SQL Database
- **GCP**: Compute Engine, Cloud SQL

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:
- 📧 Email: support@geospatial-manager.com
- 📖 Documentation: [Wiki](https://github.com/your-repo/wiki)
- 🐛 Issues: [GitHub Issues](https://github.com/your-repo/issues)

## 🙏 Acknowledgments

- **Spring Boot** - Backend framework
- **Angular** - Frontend framework
- **PostgreSQL** - Database system
- **Tesseract OCR** - OCR engine
- **OpenCV** - Computer vision library
- **Leaflet** - Map visualization

---

**Made with ❤️ for geospatial data management**