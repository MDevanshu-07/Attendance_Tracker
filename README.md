# Attendance_Tracker

# 📊 Student Attendance Tracker (Python)

## 🚀 Overview

This project is a simple **Python-based attendance tracker** that demonstrates **scripting, automation and File Handling**.
It allows users to record daily student attendance and automatically updates attendance records using a JSON file.

---
## Problem:
* Manually maintaining attendance using notes apps or paper registers is time-consuming and error-prone.
It requires repeatedly searching for student names and marking their attendance, which becomes inefficient for large classes.

---
## Solution

* I developed a simple Python-based system to automate attendance tracking.
The program takes student names as input, processes them efficiently, and stores attendance data in a structured format.

--- 

## Features

* Add multiple student names at once
* Automatically creates and updates a JSON dataset
* Tracks total working days
* Counts number of days present
* Automatically calculates absences
* Handles errors like:
  * Missing file
  * Corrupted JSON data

---

## Technologies Used

* Python
* JSON (for data storage)

---

## Project Structure

```
Attendance_Tracker/
│── attendance.py
│── student_dataset.json (auto-generated)
|── Readme.md (for understanding)
```

---

## Run it from your Terminal

1. Run the code
2. Enter student names in the following format (firstname_lastname) to avoid same name conflicts.
3. Only enter the names of students present.
4. The program:

   * Updates attendance
   * Saves data automatically
   * Calculates absences

---

## Usage

```terminal
python App.py
```

### Example Input

```
Day 1:
Shyam Rahul Priya

Day 2:
Rahul Vansh Shyam

Day 3:
Priya Rahul
```

### Example Output

```
Attendance updated successfully
```

---

## 📄 Sample JSON Output

```json
{
    "Students": {
        "Shyam": {
            "Present": 2,
            "Absent": 1
        },
        "Rahul": {
            "Present": 3,
            "Absent": 0
        },
        "Priya": {
            "Present": 2,
            "Absent": 1
        },
        "Vansh": {
            "Present": 1,
            "Absent": 2
        },
    },
    "total_days": 3
}
```

---

## My Learnings

* Python scripting
* Task automation
* File handling
* Exception handling (`FileNotFoundError`, `JSONDecodeError`)
* Data persistence using JSON

---

## Future Improvements

* Add date-wise attendance tracking
* Generate Attendance Reports with graphs and percentange.
* Separate UI for Admins and Users.
* 
