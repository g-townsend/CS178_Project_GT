# CS178_Project_GT
# Country & City Info Web App 

This is a Flask-based web application that allows users to:
- Query the top 10 most populated cities in a selected country from a MySQL database.
- Store a city in a DynamoDB table

---

## Technologies Used

- **Python 3**
- **Flask** – Web framework
- **MySQL** – For querying countries and cities
- **AWS DynamoDB** – For storing selected city data
- **HTML** – For rendering user input forms

---

## Project Structure
- **cs178_flask-app2** - Main Folder 
- **templates** - Folder with HTML Templates 
- **projectflaskapp.py** - Flask App 
- **Projectdynamo.py** - DynamoDB File 


## Setup Instructions
- **Install** 
  - **Pymysql** 
  - **boto3** 
- **Credentials** 
  - **Create a creds.py file with MYSQL credentials** 
    - **Ex** 
        - **host = "your-mysql-host"**
        - **user = "your-username"**
        - **password = "your-password"**
        - **db = "your-database-name"**

## DynamoDB Setup:
  - **Make sure you have a DynamoDB table called Vacation with:**
  - **Primary key: City (String)**

## How to Run
- **python3 projectflaskapp.py**
- **Go to: http://44.222.227.48:8080//countryquerytextbox**


## Example Input/Output
- **Entry a Country:Spain**
- **City: Top 10 most populated cities in Spain are shown**



