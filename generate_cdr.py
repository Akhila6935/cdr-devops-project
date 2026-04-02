import random
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="cdr_db"
)

cursor = conn.cursor()

for _ in range(20):
    caller = "9" + str(random.randint(100000000, 999999999))
    receiver = "9" + str(random.randint(100000000, 999999999))
    duration = random.randint(1, 300)
    call_type = random.choice(["local", "std", "isd"])
    cost = duration * 0.5

    cursor.execute(
        "INSERT INTO cdr_records (caller, receiver, duration, call_type, cost) VALUES (%s,%s,%s,%s,%s)",
        (caller, receiver, duration, call_type, cost)
    )

conn.commit()
conn.close()

print("Data inserted!")
