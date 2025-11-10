-----

## 🚂 E-Ticket Train Reservation System

A command-line interface (CLI) application developed in Python to manage train schedules and user bookings. This system uses MySQL to store and retrieve all transactional and static train data.

### ✨ Features

The application provides a structured portal system with distinct functionalities for both administrators and general users.

#### **Admin Portal (Access via pin `1234`)**

  * **Add Train:** Allows adding new trains with details like number, name, departure, intersection, arrival, and fare.
  * **Display Trains:** Shows all current train details.
  * **Delete Train:** Removes a train record from the database.
  * **Update Train:** Modifies existing train details (e.g., fare, schedule).
  * **Display Users:** Shows details of all users who have booked tickets.

#### **User Portal**

  * **Display All Trains:** Allows users to view available train routes and fares.
  * **Booking Ticket:** Allows users to input their name, destination, date of journey, and book a ticket.
  * **Search Details:** Enables users to search for specific train or booking information.
  * **Delete Ticket:** Allows a user to cancel an existing reservation.

-----

### 🛠️ Technology Stack

| Component | Technology | Details |
| :--- | :--- | :--- |
| **Backend/Logic** | **Python** | The core application logic is implemented in `trainreservation.py`. |
| **Database** | **MySQL** | Used for persistent data storage (Schema in `database.mysql`). |
| **Connector** | `mysql.connector` | Python library for connecting to the MySQL database. |
| **Development DB Version** | MySQL 8.0.31 | The provided schema dump was created with this version. |

-----

### 🚀 Getting Started

Follow these steps to set up and run the application on your local machine.

#### Prerequisites

  * **Python 3.x**
  * **MySQL Server** (The project was tested with version 8.0.31)
  * **Required Python Library:** You must install the MySQL Connector for Python.
    ```bash
    pip install mysql-connector-python
    ```

#### Database Setup

1.  **Configure MySQL:** Ensure your MySQL server is running.
2.  **Connection Details:** The Python script connects using the following hardcoded credentials:
      * **Host:** `localhost`
      * **User:** `root`
      * **Password:** `8547`
      * **Database Name:** `train_reservation_system`
        ***Note: You must change the `host`, `user`, and `passwd` in `trainreservation.py` to match your local MySQL configuration.***
3.  **Import Schema and Data:** Create the database and import the tables using the provided SQL dump file:
    ```bash
    mysql -u root -p < database.mysql
    # Use the password '8547' if you haven't changed it in the script/local setup.
    ```

#### Application Execution

1.  **Run the Python Script:**
    ```bash
    python trainreservation.py
    ```
2.  Follow the prompts in the command line to navigate the Admin or User portals.

-----

### 💻 Database Schema

The system uses a simple relational structure with two primary tables:

| Table Name | Purpose | Key Columns (from dump) |
| :--- | :--- | :--- |
| **`train_details`** | Stores train schedules and fare information. | `Trainno`, `Train_name`, `Source`, `Destination`, `Fare` |
| **`user_details`** | Stores customer booking records. | `User_id`, `User_name`, `Trainno`, `Dat_of_jour`, `Departure`, `Arrival` |

-----

### ✍️ Author

  * **Arjun Dipunath** - (@arjundipunath)
  * **Mathew Joseph** - (@mathewjosephta)
