# Feedback Management System
- contributor: Puneet and Ajay
- Mentor : Dr Kushal shah

## Project Overview

The Feedback Management System is a web application built with Python Flask that allows students to submit feedback for various courses weekly. Faculty members can view and analyze the feedback. The system is integrated with Google OAuth for authentication and uses PostgreSQL as the database.

## Features

- **Google OAuth Authentication**: Secure login with Google accounts.
- **Role-Based Access Control**: Different portals for students, faculty, and administrators.
- **Automated Feedback Submission**: Students can submit feedback on Saturdays, and faculty can view feedback summaries.
- **Feedback Analysis**: Faculty can view average ratings, distribution of ratings, and individual remarks.
- **Responsive Design**: The application is mobile-friendly.
- **Weekly access: Feedback can be entered only on saturday.
- **Email Notifications**: Automated email reminders for students to submit feedback.

## Technologies Used

- **Backend**: Python Flask
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: OAuth (Google)
- **Scheduling**: `schedule` library
  

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
  

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/feedback-management-system.git
    cd feedback-management-system
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database**:
    - Create a PostgreSQL database and user with appropriate privileges.
    - Update the `db_config` dictionary in your Flask app with the database name, user, password, host, and port.

5. **Set up environment variables**:
    - Create a `.env` file in the root directory and add the following variables:
    ```env
    SECRET_KEY=your_secret_key
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    ```

6. **Run the Flask application**:
    ```bash
    flask run
    ```

7. **Access the application**:
    - Visit `http://127.0.0.1:5000` in your web browser.

## Usage

### Student Portal

- Students can log in using their Google accounts from sitare id only.
- They can view their courses dynamically and submit feedback on Saturday only.
- Students can view past feedback submissions on rest of the day.

### Teacher Portal

- For accessing teacher portal you can enter your email in code where ajaynavodayan01 email is written and see results(for code review of teacher portal)
- Teachers can log in using their authorized email addresses.

- They can view course-wise feedback, including average ratings, rating distributions, and individual remarks.
- There is also filter option available for filtering the data in table.
  

## Database Schema

The project uses a PostgreSQL database with the following schema:

- **feedback**: Stores feedback data, including course codes, student email, instructor email, feedback ratings, remarks, and submission dates.

## Scheduled Tasks

- **Automated Emails**: The system sends automated email reminders to students on Saturdays to submit feedback.



## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request. We welcome any contributions, including bug fixes, new features, and documentation improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
