# 💰 Budget Tracker – Django + Docker

A **modern Budget Tracking Web Application** built using **Django** and fully **Dockerized** for easy setup, deployment, and scalability.  
This application allows users to manage **income, expenses, and balance** with authentication and a clean, responsive UI.

---

## 🚀 Features

- 🔐 User Authentication (Register / Login / Logout)
- 💸 Add Income & Expense Transactions
- 📊 Real-time Balance Calculation
- 🧾 Transaction History with Delete Option
- 🎨 Clean & Responsive UI
- 🐳 Fully Dockerized Application
- 📦 Ready-to-run Docker Hub Image

---

## 🛠 Tech Stack

- **Backend:** Django 5
- **Frontend:** HTML, CSS
- **Database:** SQLite (default)
- **Authentication:** Django Auth
- **Containerization:** Docker
- **Deployment:** Docker Hub

---

## 📂 Project Structure

Budget_Tracker/
│
├── Budget_Tracker/ # Project settings
├── Tracker/ # Main app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/
│
├── manage.py
├── Dockerfile
├── requirements.txt

    
    ## 🐳 Run Using Docker (Recommended)
    
    You **do NOT need Python or Django installed locally**.  
    Only **Docker** is required.
    
    ### 🔹 Pull the image from Docker Hub
    
    ```bash
    docker pull gokulpawar93/budget-tracker:latest

**Run the container**
        
        docker run -p 8000:8000 gokulpawar93/budget-tracker:latest

**Open in browser**

    http://localhost:8000
✅ The application will start immediately.
    

    
