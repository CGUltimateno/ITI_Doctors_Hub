# Doctors Hub - A Medical Search Web Application

## Project Overview
**Doctors Hub** is a Django-based web application designed to allow users to search for doctors based on their specialization and location within Egypt. The platform provides a streamlined user experience with the ability to register, log in, and search for doctors based on criteria such as medical specialization and area. Doctors Hub features a clean, responsive design and follows a modern, medical-themed style.

## Features
- User registration and authentication (Login/Logout)
- Search for doctors by specialization and area
- Display doctor details (name, phone, address, specialization, area)
- Fully responsive design using **Bootstrap**
- Modern UI/UX optimized for medical-related searches
- Administrative interface for managing doctors, areas, and specializations

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: Bootstrap (HTML, CSS)
- **Database**: SQLite (default Django setup)

## Screenshots
![Doctors Hub Home](https://i.imgur.com/E4KUwum.png)  
*Home Page - Search for doctors by specialization and area*

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x installed on your machine
- Virtual environment tool (`venv` or `virtualenv`) to manage project dependencies
- Git

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/CGUltimateno/ITI_Doctors_Hub.git
   cd doctorshub
2. **Create and Activate a Virtual Environment:**
   
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
4. **Install Project Dependencies:**
   
   Install all the required Python dependencies listed in requirements.txt (create this file if needed):
   
   ```
   pip install -r requirements.txt
  
5. **Run Database Migrations:**
   
   Set up the database by running the Django migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate

6. **Run the Development Server:**

   Start the local Django development server:
   ```
   python manage.py runserver

  The app will now run successfully at http://127.0.0.1:8000/

## Sample Data (Optional)
  To quickly populate the app with sample doctors, specializations, and areas, you can use the provided management command:
  ```
python manage.py seed_data
```

## Project Structure
```
doctorshub_project/
│
├── doctorshub/            # Main app
│   ├── migrations/        # Database migrations
│   ├── static/            # Static files (CSS, JS)
│   ├── templates/         # HTML templates
│   ├── models.py          # Data models (Doctor, Specialization, Area)
│   ├── views.py           # View functions
│   └── urls.py            # URL routes for the app
│
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```
## Usage
Once you've set up the project locally, you can:
1) Register an account: Sign up for an account to access search functionality.
2) Search for doctors: Use the search form to filter doctors by specialization and area.
3) View doctor details: Click on any doctor's name to view more details.
4) The admin interface is accessible at /admin/ once logged in as a superuser.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

