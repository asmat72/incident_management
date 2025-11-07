# incident_management

# 🚨 Open-Source Incident Management System
   - A lightweight, open-source portal to log, track, and resolve infrastructure or application issues — designed with role-based access and RESTful

- 🎯 Objective:
   - Clone the repository: git clone "https://github.com/asmat72/incident_management.git"
   - Build a basic incident management system that empowers teams to:
     -  Log and categorize incidents.
     -  Assign and update incident status.
     -  Resolve and track issues efficiently.
     -  Control access based on user roles.

- 🛠️ Tech Stack:
     - **Backend** : Python (Flask or Django).
     - **Database** : SQLite.
     - **Frontend** : Bootstrap.
     - **Containerization** : Docker.
     - **Version Control** : Git.

- 📘 Mini Guide:
   - ✅ Core Features:
   - **REST APIs** to:
     - Create incidents.
     - Update incident details.
     - Assign incidents to users.
     - Resolve and close incidents.
   
   - **Docker Integration**:
     -  Containerized deployment.
     -  Easy portability and testing.

   - **SQLite Storage**:
     -  Lightweight and simple setup.
     -  Ideal for prototyping and local development.

   - **Git Version Control**:
     - Source code management.
     - Collaboration and history tracking.

- 📁 Suggested Project Structure:
   - incident-management/
         ├── incident_app/           # Django app for incidents
         │    ├── migrations/
         │    ├── admin.py
         │    ├── apps.py
         │    ├── tests.py 
         │    ├── templates/
         │    ├── static/
         │    ├── models.py
         │    ├── views.py
         │    ├── urls.py
         │    ├── serializers.py 
         │    └── forms.py
         ├── incident_management/    # Django project settings
         │    ├── settings.py
         │    ├── urls.py
         │    └── wsgi.py
         ├── db.sqlite3              # SQLite database
         ├── Dockerfile              # Docker build instructions
         ├── docker-compose.yml      # Optional: for multi-container setup
         ├── requirements.txt        # Python dependencies
         ├── manage.py
         └── README.md               # Project documentation

- 📦 Deliverables:
   - ✅ Source code hosted on GitHub.
   - ✅ Docker image for deployment.
   - ✅ Demo video and screenshots.
   - ✅ Sample incidents (logged and resolved).

- 🎥 Storytelling: Behind the Demo Video:
   - While recording the demo video, I walk through the entire lifecycle of an incident:
     - 1. **Creating a New Incident**  
        - I show how a user logs a fresh issue — whether it's infrastructure downtime or a bug in the app.
     - 2. **Assigning and Updating**  
        - I demonstrate how the issue is assigned to a team member and how status updates are tracked.
     - 3. **Final Showcase**  
        -I display sample incidents and screenshots to validate the system’s functionality.

- 🙌 Credits:
   - Developed by **Asmatullah Khan**.  
   - Aspiring DevOps & Django Developer.  
   - Focused on building real-world infrastructure and incident management solutions.

  
 
