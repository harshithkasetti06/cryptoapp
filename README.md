🚀 Crypto Tracker Web Application

A full-stack web application that provides real-time cryptocurrency data, interactive charts, and market insights using Django, APIs, Docker, and Kubernetes.

📌 Features
🔍 Search any cryptocurrency (Bitcoin, Ethereum, etc.)
💰 Live price tracking (INR)
📊 24-hour High / Low / Market Cap
📈 Interactive price charts (Chart.js)
🧠 Market sentiment visualization
📉 Hourly volume analysis
⚡ Real-time data from CoinGecko API
🐳 Docker containerization
☸️ Kubernetes deployment (Minikube)
🧱 Tech Stack
Frontend
HTML5
CSS3
JavaScript
Chart.js
Backend
Python
Django
API
CoinGecko API
DevOps
Docker
Docker Compose
Kubernetes (Minikube)

🚀 Crypto Tracker Web Application

A full-stack web application that provides real-time cryptocurrency data, interactive charts, and market insights using Django, APIs, Docker, and Kubernetes.

📌 Features
🔍 Search any cryptocurrency (Bitcoin, Ethereum, etc.)
💰 Live price tracking (INR)
📊 24-hour High / Low / Market Cap
📈 Interactive price charts (Chart.js)
🧠 Market sentiment visualization
📉 Hourly volume analysis
⚡ Real-time data from CoinGecko API
🐳 Docker containerization
☸️ Kubernetes deployment (Minikube)
🧱 Tech Stack
Frontend
HTML5
CSS3
JavaScript
Chart.js
Backend
Python
Django
API
CoinGecko API
DevOps
Docker
Docker Compose
Kubernetes (Minikube)

⚙️ Project Structure

cryptoapp/
│── tracker/
│   ├── templates/tracker/index.html
│   ├── views.py
│   ├── urls.py
│
│── cryptoapp/
│   ├── settings.py
│   ├── urls.py
│
│── Dockerfile
│── docker-compose.yml
│── deployment.yaml
│── service.yaml
│── manage.py


🚀 Getting Started
🔹 1. Clone Repository
git clone https://github.com/your-username/cryptoapp.git
cd cryptoapp

👉 Downloads the project to your system

🔹 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

👉 Creates and activates Python environment

🔹 3. Install Dependencies
pip install django requests

👉 Installs required Python packages

🔹 4. Run Django Server
python manage.py runserver 8001

👉 Starts the app locally

🔹 5. Open in Browser
http://127.0.0.1:8001
🐳 Docker Setup
🔹 Build Image
docker build -t cryptoapp-web .

👉 Creates Docker image

🔹 Run Container
docker run -p 8001:8001 cryptoapp-web

👉 Runs app inside container

☸️ Kubernetes (Minikube)
🔹 Start Minikube
minikube start --driver=docker
🔹 Load Image
minikube image load cryptoapp-web
🔹 Deploy App
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
🔹 Access App
minikube service cryptoapp
🔄 Working Flow
User searches for a cryptocurrency
Django backend processes request
Fetches data from CoinGecko API
Sends data to frontend
UI updates dynamically with charts and stats
⚠️ Common Issues & Fixes
❌ Port already in use
netstat -ano | findstr :8001
taskkill /PID <PID> /F
❌ Docker not running

👉 Start Docker Desktop

❌ Image pull error (Kubernetes)
minikube image load cryptoapp-web
🚀 Future Enhancements
User authentication system
Portfolio tracking
Real-time updates using WebSockets
Mobile responsive improvements
Advanced analytics dashboard
📌 Conclusion

This project demonstrates:

Full-stack web development
API integration
Data visualization
Docker containerization
Kubernetes deployment

👨‍💻 Author

HARSHITH KASETTI

⭐ If you like this project

Give it a ⭐ on GitHub!
