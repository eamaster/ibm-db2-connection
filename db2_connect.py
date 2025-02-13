import ibm_db

# Database connection details
DATABASE = "bludb"
HOSTNAME = "815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
PORT = "30367"
USER = "tsc33074"
PASSWORD = "1Pl51P1ZhjhPKiUA"
SSL = "SSL"

# Connection string
conn_str = (
    f"DATABASE={DATABASE};HOSTNAME={HOSTNAME};PORT={PORT};PROTOCOL=TCPIP;UID={USER};PWD={PASSWORD};SECURITY={SSL};"
)

# Establish connection
try:
    conn = ibm_db.connect(conn_str, "", "")
    print("Connected to IBM Db2 successfully!")
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

# Create table
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
"""
try:
    ibm_db.exec_immediate(conn, create_table_sql)
    print("Table created successfully or already exists.")
except Exception as e:
    print(f"Error creating table: {e}")

# Insert data
insert_sql = "INSERT INTO users (name, email) VALUES (?, ?)"
params = ("John Doe", "john.doe@example.com")
try:
    stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.execute(stmt, params)
    print("Data inserted successfully.")
except Exception as e:
    print(f"Error inserting data: {e}")

# Close connection
ibm_db.close(conn)
