# 🍽️ Django Recipe Website

A full-featured recipe management web application built using Django. This platform allows users to explore a wide variety of recipes with step-by-step cooking instructions and ingredient details. Designed with user authentication, it ensures secure access and includes a specialized section for fitness-focused diets like **bulking** and **cutting**.

---

## 🔑 Features

### ✅ User Authentication
- User registration and login/logout
- Only **authenticated users** can access and view recipes

### 🍳 Recipe Management
- Browse various recipes with:
  - Ingredients list
  - Step-by-step cooking instructions
- Filtered sections for:
  - **Bulking Recipes** 💪
  - **Cutting Recipes** 🏋️

### 📁 Categories & Organization
- Recipes are grouped into regular, bulking, and cutting categories for better health-based dietary planning.

---

## 🛠️ Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| Backend      | Django (Python)|
| Frontend     | HTML, CSS (Django templates) |
| Database     | SQLite (default Django DB)  |
| Authentication | Django Auth System |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/hariprasath112005/django_recipe.git
cd django_recipe
```
### 2. Create a Virtual Environment & Activate
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Migrations
```bash
python manage.py migrate
```
### 5. Run the Development Server
```bash
python manage.py runserver
```
### 6. Access the Site
 Visit http://127.0.0.1:8000/ in your browser.
