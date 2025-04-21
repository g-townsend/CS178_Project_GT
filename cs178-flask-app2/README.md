# CS178_Project_GT
# Country & City Info Web App 🌍

This is a simple Flask-based web application that allows users to:
- Query the top 10 most populated cities in a selected country from a MySQL database.
- Submit a city name via a web form and store it in a DynamoDB table.

---

## 🛠 Technologies Used

- **Python 3**
- **Flask** – Web framework
- **MySQL (via PyMySQL)** – For querying countries and cities
- **AWS DynamoDB (via Boto3)** – For storing selected city data
- **HTML (Jinja2 templates)** – For rendering user input forms

---

## 📁 Project Structure

```bash
.
├── app.py               # Main Flask application
├── creds.py             # MySQL credentials (host, user, password, db)
├── templates/
│   └── textbox.html     # HTML form for user input
└── README.md            # You're here!
🔧 Setup Instructions
Install dependencies:

bash
Copy
Edit
pip install flask pymysql boto3
Configure credentials:

Create a creds.py file with your MySQL credentials:

python
Copy
Edit
# creds.py
host = "your-mysql-host"
user = "your-username"
password = "your-password"
db = "your-database-name"
Make sure your AWS credentials are configured either via:

~/.aws/credentials

Environment variables

IAM role (if using EC2 or Lambda)

DynamoDB Setup:

Make sure you have a DynamoDB table called Vacation with:

Primary key: City (String)

You can optionally add a Cost attribute (either a number or list).

🚀 How to Run
bash
Copy
Edit
python app.py
Then go to: http://localhost:8080/countryquerytextbox

🌐 App Routes
GET /countryquerytextbox
Displays a form where users can enter:

A country name

A city name

POST /countryquerytextbox
Submits the city to DynamoDB (table: Vacation)

Displays top 10 populated cities in the given country from MySQL

GET /countryquery/<country>
Direct route to view top cities in a country

✅ Example Input
Form:

Country: France

City: Nice

Result:

The city “Nice” is added to DynamoDB

Top 10 most populated cities in France are shown

🧪 Debug Tips
Check Flask terminal logs for print() output.

Confirm DynamoDB region is set correctly (us-east-1).

Make sure City is the partition key in your DynamoDB table.

Add extra print() or use Postman to inspect POST requests.

