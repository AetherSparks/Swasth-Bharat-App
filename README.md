# Swastha Bharat App-Py

Swastha Bharat App-Py is a Python-based healthcare application designed to manage user registration, login, and patient records. This application ensures secure and efficient access to medical information for both users and administrators.

## Features

- **User Registration and Login**
  - Users can sign up by providing their username, password, and Aadhaar ID.
  - Users can log in with their credentials to access their medical records.

- **Admin Controls**
  - Admins can view and manage signup requests.
  - Admins can add and view patient records.
  - Admins have access to special login credentials.

- **Patient Records Management**
  - Users can view their medical records by logging in.
  - Admins can add new patient records including diseases and vaccinations.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `csv`
  - `sys`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/swastha-bharat-app-py.git
    ```

2. Navigate to the project directory:
    ```bash
    cd swastha-bharat-app-py
    ```

3. Run the application:
    ```bash
    python swastha_bharat_app.py
    ```

## Usage

### Running the Application

Upon running the script, you will be prompted with options to either log in or sign up.

#### Sign Up
1. Choose the sign-up option.
2. Enter the requested information (username, password, Aadhaar ID).
3. Your signup request will be sent to the administrator for approval.

#### Log In
1. Choose the log-in option.
2. Enter your username and password.
3. If the credentials match an existing account, you will be logged in and given further options.

### Admin Controls

Admins have additional functionalities:
1. **Check for pending signup requests**: Review and approve or deny user signup requests.
2. **View patient records**: Enter a patient's Aadhaar ID to view their medical records.
3. **Add patient records**: Enter patient details and medical information to add new records.

## File Structure

- `swastha_bharat_app.py`: Main application script.
- `databaseaccess.csv`: Stores approved user credentials.
- `signuprequest.csv`: Temporary storage for signup requests awaiting admin approval.
- `patientdiseaselist.csv`: Stores patient medical records.

## Author

Created by Abhiraj Ghose

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

