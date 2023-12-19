import mysql.connector, sys

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "bpp_prak_11"
}


def create_table_employees():
    cursor = connection.cursor()

    create_table_sql = """CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    salary DECIMAL(10,2) NOT NULL
    );"""

    cursor.execute(create_table_sql)
    connection.commit()

    print("Table 'employees' created successfully!")

def add_employees():
    employees = [
    {"name": "John Doe", "position": "Software Engineer", "salary": 50000.00},
    {"name": "Jane Doe", "position": "Marketing Manager", "salary": 75000.00},
    {"name": "Mike Smith", "position": "Accountant", "salary": 40000.00},
    ]

    insert_employee_sql = """INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)"""

    for employee in employees:
        cursor.execute(insert_employee_sql, (employee["name"], employee["position"], employee["salary"]))

    connection.commit()

    print("3 employees added successfully!")

def show_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    print("Employees data:")
    for employee in employees:
        print(f"\tID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: ${employee[3]:.2f}")

    cursor.close()
    connection.close()

# Connect to the database
try:
    flag = sys.argv[1]

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    print("connected")
    
    # Do something based on the flag
    if flag == "migrate":
        # create table employees: id(int), name(text), position(text), salary(int)
        create_table_employees()
        
        # add employees
        add_employees()

        # show employees
        show_employees()

        print("Migrate!")
    elif flag == "fresh":
        query = "DROP TABLE employees"
        cursor.execute(query)
        print("Fresh!")

    print(sys.argv)

except mysql.connector.Error as error:
    print(f"Error connecting to database: {error}")