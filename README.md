# Contact Book Application

## Overview
This Django project is a simple Contact Book application. It allows users to manage their contacts through three main pages: Home, Contact, and Display. 
The application uses SQLite as the database and includes functionalities for adding, updating, and deleting contact details.

## Features

- **Home Page**: 
  - Users can log in by entering their name.
  - On successful login, users are redirected to the Contact Page.

- **Contact Page**:
  - Users can add or update contact details (Name, Phone, Email, Address).
  - Contact details are displayed.
  - Users can update or delete contact details.
  - A "View All" button directs users to the Display Page.
  - A "Logout" button directs users to the Home Page.

- **Display Page**:
  - Displays all contacts related to the logged-in user.
  - A "Back to Contact Page" button allows users to return to the Contact Page.
  - A "Logout" button redirects users to the Home Page.

## Technologies Used

- **Django**: Web framework for building the application.
- **SQLite**: Database used for storing contact information.
- **Bootstrap**: CSS framework for styling the pages.
- **HTML/CSS**: For front-end design and layout.

## Installation
1. Clone the Repository:
   ```
   git clone https://github.com/Bhuvneshjai/Contact-Book-Application.git
   cd Contact_Book_Project

2. Create and Activate a Virtual Environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use Contact_Book_Venv\Scripts\activate

3. Install Dependencies:
    ```
    pip install -r requirements.txt

4. Apply Migrations:
    ```
    python manage.py migrate

4. Run the Development Server:
    ```
    python manage.py runserver

5. Access the Application:
    Open your web browser and navigate to http://127.0.0.1:8000/.

## Usage
1. Home Page: Enter your name to log in and be redirected to the Contact Page.
    * Image:
        ![image](https://github.com/user-attachments/assets/55cb9bf2-aa96-4c95-b089-861e852b6b5d)

3. Contact Page:
  * Fill out the form to add or update contact details.
  * Contacts will appear in the right box with options to update or delete.
  * Use the pagination controls to navigate through multiple contacts.
  * Click "View All" to see all contacts on the Display Page.
    
    * Image:
        ![image](https://github.com/user-attachments/assets/d7bc2801-4dd5-4559-b665-bf08102a9619)

3. Display Page: View all your contacts and use the "Back to Contact Page" button to return.
    * Image:
        ![image](https://github.com/user-attachments/assets/cdb3aadd-74ef-4ddd-bd80-0e21e6663c59)

5. Logout: Click the "Logout" button to return to the Home Page.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with any changes or improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
