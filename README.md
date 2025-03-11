# admin-tackerAdmin Tracker

Overview

Admin Tracker is a PostgreSQL-based monitoring tool that tracks admin and user activities in a database. It logs authentication events, active sessions, query execution, data modifications, role changes, and security-related incidents. This tool provides real-time alerts, reports, and a visual dashboard for effective monitoring.

Features

1. User Authentication & Role Management

✅ Login & Logout Tracking – Logs timestamps of user logins and logouts.

✅ Role-Based Access Control (RBAC) – Differentiates admin and regular users for permission enforcement.

✅ Failed Login Attempt Logging – Tracks failed login attempts for security.

2. Active Session Monitoring

✅ View Live Sessions – Displays a real-time list of active users.

✅ Idle Session Detection – Identifies inactive users.

✅ Force Logout/Terminate Session – Admins can manually terminate sessions.

3. Query Execution Tracking

✅ Track All SQL Queries – Logs all queries executed.

✅ Highlight Suspicious Queries – Flags long-running or mass delete queries.

✅ Query Performance Analysis – Identifies slow queries affecting performance.

4. Data Modification Tracking

✅ Record Data Insertions – Logs every INSERT operation.

✅ Track Data Updates – Monitors changes to existing records.

✅ Log Data Deletions – Records DELETE operations.

✅ Compare Before & After Changes – Displays data before and after updates.

5. Role & Permission Change Monitoring

✅ Detect Role Modifications – Logs changes in user roles.

✅ Track Permission Changes – Records changes in access rights.

6. Security & Suspicious Activity Detection

✅ Monitor Unauthorized Access Attempts – Detects brute-force attempts.

✅ Detect Unusual Query Patterns – Flags abnormal queries.

✅ Identify High-Impact Changes – Alerts on unauthorized schema modifications.

7. Database Backup & Restore Logging

✅ Track Backup Events – Logs database backup activities.

✅ Monitor Restore Actions – Records database restore operations.

8. Alert System & Notifications

✅ Send Real-Time Alerts – Notifies admins on suspicious activity.

✅ Customizable Alerts – Allows setting thresholds for alerts.

9. Reporting & Analytics Dashboard

✅ Activity Summary Reports – Generates activity trend reports.

✅ Top Active Users Report – Identifies most active users.

✅ Suspicious Activity Reports – Lists flagged activities.

✅ Export Logs – Supports CSV, Excel, and PDF exports.

10. API Integration & Log Retrieval

✅ Provide API Endpoints – Allows external applications to access logs.

✅ Enable Log Filtering – Supports filtering by date, user, or action type.

✅ Secure API with Authentication – Ensures only authorized access.

11. Dashboard for Visual Insights

✅ Real-Time Graphs & Charts – Displays user activity trends.

✅ Filter by User/Date/Action – Enables easy log searches.

Installation & Setup

Prerequisites

Python 3.x

PostgreSQL

FastAPI (Backend)

React.js (Frontend)

Steps to Run

Clone the Repository

git clone https://github.com/your-username/admin-tracker.git
cd admin-tracker

Set Up Virtual Environment (Optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Configure Database

Update config.py with PostgreSQL credentials.

Run migrations (if applicable).

Start the Backend Server

uvicorn main:app --reload

Start the Frontend

cd frontend
npm install
npm start

API Endpoints

Endpoint

Method

Description

/auth/login

POST

User login

/auth/logout

POST

User logout

/sessions/active

GET

Get live active sessions

/queries/logs

GET

Retrieve query logs

/data-changes

GET

Fetch data modification logs

/alerts/realtime

GET

Get real-time alerts

Contribution

Fork the repository.

Create a new branch (feature/your-feature-name).

Commit your changes and push.

Open a Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For queries or issues, contact www.mk996820@gmail.com] or raise an issue on GitHub.

🚀 Admin Tracker - Keep your database secure and monitored!

