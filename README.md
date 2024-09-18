# Student Management System

This is a simple Student Management System built with Flask. It allows administrators to manage student information through a web interface.

## Features

- User authentication (login/logout)
- View all students
- Add new students
- Edit existing student information
- Delete students

## Technologies Used

- Python 3
- Flask
- Flask-Login
- Werkzeug
- HTML/CSS
- Bootstrap 5
- Font Awesome 5

## Project Structure

The main components of the project are:

- `app.py`: The main Flask application file
- `templates/`: Directory containing HTML templates
  - `admin.html`: Admin dashboard to view and manage students
  - `login.html`: Login page
  - `add.html`: Page to add new students
  - `edit.html`: Page to edit existing student information

## Setup and Installation

1. Ensure you have Python 3 installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies:
   ```
   pip install flask flask-login werkzeug
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Open a web browser and navigate to `http://localhost:5000` to access the application.

## Usage

1. Log in using the credentials:
   - Username: admin
   - Password: password

2. Once logged in, you'll be directed to the admin dashboard where you can view all students.

3. Use the "新增学生" button to add a new student.

4. Each student entry has "编辑" and "删除" options for modifying or removing student information.

5. Use the "登出" button to log out of the system.

## Security Notes

- This is a basic implementation and should not be used in production without further security enhancements.
- The secret key and user credentials are hardcoded for demonstration purposes. In a real application, these should be stored securely and not in the source code.
- Consider using a database for storing user and student information instead of in-memory storage.

## Future Improvements

- Implement proper database integration (e.g., SQLAlchemy with SQLite or PostgreSQL)
- Add user registration functionality
- Implement role-based access control
- Add more robust error handling and input validation
- Enhance the UI/UX with more advanced CSS and JavaScript

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open-source and available under the MIT License.
