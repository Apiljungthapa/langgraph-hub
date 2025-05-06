import sqlite3

def create_dentist_db():
    conn = sqlite3.connect("dentist.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        dentist_name TEXT,
        appointment_date TEXT,
        appointment_time TEXT,
        status TEXT DEFAULT 'booked',
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
    );
    """)

    conn.commit()
    conn.close()

create_dentist_db()


def create_dentist_db():
    conn = sqlite3.connect("dentist.db")
    cursor = conn.cursor()

    # Create patients table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact TEXT NOT NULL
    );
    """)

    # Create dentists table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dentists (
        dentist_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialty TEXT,
        available_days TEXT,      -- e.g., "Mon,Tue,Thu"
        available_time_start TEXT,  -- e.g., "09:00"
        available_time_end TEXT     -- e.g., "17:00"
    );
    """)

    # Create appointments table with reference to dentist_id
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        dentist_id INTEGER,
        appointment_date TEXT,
        appointment_time TEXT,
        status TEXT DEFAULT 'booked',
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
        FOREIGN KEY(dentist_id) REFERENCES dentists(dentist_id)
    );
    """)

    conn.commit()
    conn.close()

create_dentist_db()


# import sqlite3

# def create_dentist_db():
#     conn = sqlite3.connect("dentist.db")
#     cursor = conn.cursor()

#     # Create patients table
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS patients (
#         patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         contact TEXT NOT NULL
#     );
#     """)

#     # Create dentists table
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS dentists (
#         dentist_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         specialty TEXT,
#         available_days TEXT,
#         available_time_start TEXT,
#         available_time_end TEXT
#     );
#     """)

#     # Create appointments table
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS appointments (
#         appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         patient_id INTEGER,
#         dentist_id INTEGER,
#         appointment_date TEXT,
#         appointment_time TEXT,
#         status TEXT DEFAULT 'booked',
#         FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
#         FOREIGN KEY(dentist_id) REFERENCES dentists(dentist_id)
#     );
#     """)

#     # Insert dentist values
#     cursor.executemany("""
#     INSERT INTO dentists (name, specialty, available_days, available_time_start, available_time_end)
#     VALUES (?, ?, ?, ?, ?)
#     """, [
#         ("Dr. Ayush Aryal", "General Dentistry", "Mon,Wed,Fri", "09:00", "13:00"),
#         ("Dr. Shishir Shrestha", "Orthodontist", "Tue,Thu,Sat", "10:00", "16:00"),
#         ("Dr. Milan Simkhada", "Oral Surgeon", "Mon,Tue,Fri", "12:00", "17:00")
#     ])

#     conn.commit()
#     conn.close()

# create_dentist_db()


# def alter_appointments_table():
#     conn = sqlite3.connect("dentist.db")
#     cursor = conn.cursor()

#     # Add a new column 'reason' to store the purpose of the appointment
#     cursor.execute("""
#     ALTER TABLE appointments
#     ADD COLUMN reason TEXT;
#     """)

#     conn.commit()
#     conn.close()

# alter_appointments_table()