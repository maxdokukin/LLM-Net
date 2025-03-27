import sqlite3

# Connect to (or create) the SQLite database file
conn = sqlite3.connect("university.sqlite")
cursor = conn.cursor()

# Create the departments table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        dept_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        building TEXT
    )
""")
# Create the professors table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS professors (
        prof_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        dept_id INTEGER,
        title TEXT,
        FOREIGN KEY(dept_id) REFERENCES departments(dept_id)
    )
""")
# Create the students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        major_dept_id INTEGER,
        enrollment_year INTEGER,
        FOREIGN KEY(major_dept_id) REFERENCES departments(dept_id)
    )
""")
# Create the courses table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        dept_id INTEGER,
        credits INTEGER,
        professor_id INTEGER,
        FOREIGN KEY(dept_id) REFERENCES departments(dept_id),
        FOREIGN KEY(professor_id) REFERENCES professors(prof_id)
    )
""")
# Create the enrollments table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        grade TEXT,
        FOREIGN KEY(student_id) REFERENCES students(student_id),
        FOREIGN KEY(course_id) REFERENCES courses(course_id)
    )
""")
print("Tables created.")

# Insert data into departments (5 entries)
cursor.execute("INSERT INTO departments (dept_id, name, building) VALUES (?, ?, ?)", (1, "Computer Science", "Engineering Hall"))
print("Inserted department: (1, 'Computer Science', 'Engineering Hall')")
cursor.execute("INSERT INTO departments (dept_id, name, building) VALUES (?, ?, ?)", (2, "Mathematics", "Math Building"))
print("Inserted department: (2, 'Mathematics', 'Math Building')")
cursor.execute("INSERT INTO departments (dept_id, name, building) VALUES (?, ?, ?)", (3, "Physics", "Science Center"))
print("Inserted department: (3, 'Physics', 'Science Center')")
cursor.execute("INSERT INTO departments (dept_id, name, building) VALUES (?, ?, ?)", (4, "English", "Liberal Arts"))
print("Inserted department: (4, 'English', 'Liberal Arts')")
cursor.execute("INSERT INTO departments (dept_id, name, building) VALUES (?, ?, ?)", (5, "Biology", "Life Sciences"))
print("Inserted department: (5, 'Biology', 'Life Sciences')")

# Insert data into professors (20 entries) with realistic names
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (1, "Dr. John Smith", 1, "Professor"))
print("Inserted professor: (1, 'Dr. John Smith', 1, 'Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (2, "Dr. Emily Johnson", 2, "Associate Professor"))
print("Inserted professor: (2, 'Dr. Emily Johnson', 2, 'Associate Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (3, "Dr. Robert Williams", 3, "Assistant Professor"))
print("Inserted professor: (3, 'Dr. Robert Williams', 3, 'Assistant Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (4, "Dr. Linda Brown", 4, "Professor"))
print("Inserted professor: (4, 'Dr. Linda Brown', 4, 'Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (5, "Dr. Michael Jones", 5, "Associate Professor"))
print("Inserted professor: (5, 'Dr. Michael Jones', 5, 'Associate Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (6, "Dr. Elizabeth Garcia", 1, "Assistant Professor"))
print("Inserted professor: (6, 'Dr. Elizabeth Garcia', 1, 'Assistant Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (7, "Dr. David Miller", 2, "Professor"))
print("Inserted professor: (7, 'Dr. David Miller', 2, 'Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (8, "Dr. Barbara Davis", 3, "Associate Professor"))
print("Inserted professor: (8, 'Dr. Barbara Davis', 3, 'Associate Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (9, "Dr. William Rodriguez", 4, "Assistant Professor"))
print("Inserted professor: (9, 'Dr. William Rodriguez', 4, 'Assistant Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (10, "Dr. Jennifer Martinez", 5, "Professor"))
print("Inserted professor: (10, 'Dr. Jennifer Martinez', 5, 'Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (11, "Dr. Richard Hernandez", 1, "Associate Professor"))
print("Inserted professor: (11, 'Dr. Richard Hernandez', 1, 'Associate Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (12, "Dr. Susan Lopez", 2, "Assistant Professor"))
print("Inserted professor: (12, 'Dr. Susan Lopez', 2, 'Assistant Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (13, "Dr. Joseph Gonzalez", 3, "Professor"))
print("Inserted professor: (13, 'Dr. Joseph Gonzalez', 3, 'Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (14, "Dr. Sarah Wilson", 4, "Associate Professor"))
print("Inserted professor: (14, 'Dr. Sarah Wilson', 4, 'Associate Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (15, "Dr. Thomas Anderson", 5, "Assistant Professor"))
print("Inserted professor: (15, 'Dr. Thomas Anderson', 5, 'Assistant Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (16, "Dr. Karen Thomas", 1, "Professor"))
print("Inserted professor: (16, 'Dr. Karen Thomas', 1, 'Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (17, "Dr. Charles Taylor", 2, "Associate Professor"))
print("Inserted professor: (17, 'Dr. Charles Taylor', 2, 'Associate Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (18, "Dr. Nancy Moore", 3, "Assistant Professor"))
print("Inserted professor: (18, 'Dr. Nancy Moore', 3, 'Assistant Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (19, "Dr. Christopher Jackson", 4, "Professor"))
print("Inserted professor: (19, 'Dr. Christopher Jackson', 4, 'Professor')")
cursor.execute("INSERT INTO professors (prof_id, name, dept_id, title) VALUES (?, ?, ?, ?)", (20, "Dr. Lisa Martin", 5, "Associate Professor"))
print("Inserted professor: (20, 'Dr. Lisa Martin', 5, 'Associate Professor')")

# Insert data into students (20 entries) with realistic names
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (1, "Alice Johnson", 1, 2020))
print("Inserted student: (1, 'Alice Johnson', 1, 2020)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (2, "Brian Lee", 2, 2021))
print("Inserted student: (2, 'Brian Lee', 2, 2021)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (3, "Catherine Miller", 3, 2022))
print("Inserted student: (3, 'Catherine Miller', 3, 2022)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (4, "Daniel Garcia", 4, 2023))
print("Inserted student: (4, 'Daniel Garcia', 4, 2023)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (5, "Eva Martinez", 5, 2020))
print("Inserted student: (5, 'Eva Martinez', 5, 2020)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (6, "Frank Wilson", 1, 2021))
print("Inserted student: (6, 'Frank Wilson', 1, 2021)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (7, "Grace Anderson", 2, 2022))
print("Inserted student: (7, 'Grace Anderson', 2, 2022)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (8, "Henry Thomas", 3, 2023))
print("Inserted student: (8, 'Henry Thomas', 3, 2023)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (9, "Irene Moore", 4, 2020))
print("Inserted student: (9, 'Irene Moore', 4, 2020)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (10, "Jack Taylor", 5, 2021))
print("Inserted student: (10, 'Jack Taylor', 5, 2021)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (11, "Katherine Jackson", 1, 2022))
print("Inserted student: (11, 'Katherine Jackson', 1, 2022)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (12, "Leonard White", 2, 2023))
print("Inserted student: (12, 'Leonard White', 2, 2023)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (13, "Megan Harris", 3, 2020))
print("Inserted student: (13, 'Megan Harris', 3, 2020)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (14, "Nathan Clark", 4, 2021))
print("Inserted student: (14, 'Nathan Clark', 4, 2021)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (15, "Olivia Lewis", 5, 2022))
print("Inserted student: (15, 'Olivia Lewis', 5, 2022)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (16, "Patrick Robinson", 1, 2023))
print("Inserted student: (16, 'Patrick Robinson', 1, 2023)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (17, "Quinn Walker", 2, 2020))
print("Inserted student: (17, 'Quinn Walker', 2, 2020)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (18, "Rachel Young", 3, 2021))
print("Inserted student: (18, 'Rachel Young', 3, 2021)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (19, "Samuel King", 4, 2022))
print("Inserted student: (19, 'Samuel King', 4, 2022)")
cursor.execute("INSERT INTO students (student_id, name, major_dept_id, enrollment_year) VALUES (?, ?, ?, ?)", (20, "Tina Scott", 5, 2023))
print("Inserted student: (20, 'Tina Scott', 5, 2023)")

# Insert data into courses (5 entries)
cursor.execute("INSERT INTO courses (course_id, name, dept_id, credits, professor_id) VALUES (?, ?, ?, ?, ?)", (1, "Introduction to Programming", 1, 3, 1))
print("Inserted course: (1, 'Introduction to Programming', 1, 3, 1)")
cursor.execute("INSERT INTO courses (course_id, name, dept_id, credits, professor_id) VALUES (?, ?, ?, ?, ?)", (2, "Calculus I", 2, 4, 2))
print("Inserted course: (2, 'Calculus I', 2, 4, 2)")
cursor.execute("INSERT INTO courses (course_id, name, dept_id, credits, professor_id) VALUES (?, ?, ?, ?, ?)", (3, "Physics I", 3, 4, 3))
print("Inserted course: (3, 'Physics I', 3, 4, 3)")
cursor.execute("INSERT INTO courses (course_id, name, dept_id, credits, professor_id) VALUES (?, ?, ?, ?, ?)", (4, "English Literature", 4, 3, 4))
print("Inserted course: (4, 'English Literature', 4, 3, 4)")
cursor.execute("INSERT INTO courses (course_id, name, dept_id, credits, professor_id) VALUES (?, ?, ?, ?, ?)", (5, "Biology Basics", 5, 3, 5))
print("Inserted course: (5, 'Biology Basics', 5, 3, 5)")

# Insert data into enrollments (5 entries)
cursor.execute("INSERT INTO enrollments (enrollment_id, student_id, course_id, grade) VALUES (?, ?, ?, ?)", (1, 1, 1, "A"))
print("Inserted enrollment: (1, 1, 1, 'A')")
cursor.execute("INSERT INTO enrollments (enrollment_id, student_id, course_id, grade) VALUES (?, ?, ?, ?)", (2, 2, 2, "B"))
print("Inserted enrollment: (2, 2, 2, 'B')")
cursor.execute("INSERT INTO enrollments (enrollment_id, student_id, course_id, grade) VALUES (?, ?, ?, ?)", (3, 3, 3, "C"))
print("Inserted enrollment: (3, 3, 3, 'C')")
cursor.execute("INSERT INTO enrollments (enrollment_id, student_id, course_id, grade) VALUES (?, ?, ?, ?)", (4, 4, 4, "B+"))
print("Inserted enrollment: (4, 4, 4, 'B+')")
cursor.execute("INSERT INTO enrollments (enrollment_id, student_id, course_id, grade) VALUES (?, ?, ?, ?)", (5, 5, 5, "A-"))
print("Inserted enrollment: (5, 5, 5, 'A-')")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database 'university.db' created with all sample entries.")
