import sqlite3
from datetime import datetime
from typing import Optional
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
import requests
from assistance import Assistant, primary_assistant_prompt, llm

DB_PATH = "dentist.db"


@tool
def create_appointment(dentist_name: str, appointment_time: str, reason: str, *, config: RunnableConfig) -> str:
    """Create a new appointment for the configured patient."""
    configuration = config.get("configurable", {})
    patient_id = configuration.get("patient_id", None)
    if not patient_id:
        raise ValueError("No patient_id configured.")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO appointments (patient_id, dentist_name, appointment_time, reason) VALUES (?, ?, ?, ?)",
        (patient_id, dentist_name, appointment_time, reason)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return "Appointment successfully created."


@tool
def fetch_patient_appointments(*, config: RunnableConfig) -> list[dict]:
    """Fetch all appointments for the configured patient."""
    configuration = config.get("configurable", {})
    patient_id = configuration.get("patient_id", None)
    if not patient_id:
        raise ValueError("No patient_id configured.")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM appointments WHERE patient_id = ?", (patient_id,))
    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    results = [dict(zip(column_names, row)) for row in rows]

    cursor.close()
    conn.close()
    return results


@tool
def update_appointment_time(appointment_id: int, new_time: str, *, config: RunnableConfig) -> str:
    """Update an appointment's time for the configured patient."""
    configuration = config.get("configurable", {})
    patient_id = configuration.get("patient_id", None)
    if not patient_id:
        raise ValueError("No patient_id configured.")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM appointments WHERE appointment_id = ? AND patient_id = ?",
        (appointment_id, patient_id)
    )
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return f"No appointment found with ID {appointment_id} for this patient."

    cursor.execute(
        "UPDATE appointments SET appointment_time = ? WHERE appointment_id = ?",
        (new_time, appointment_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return f"Appointment ID {appointment_id} successfully updated."

@tool
def display_doctors() -> str:
    """Display all available dentists with their specialties."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, specialty FROM dentists")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No doctors found."

    result = "Available Dentists and Their Specialties:\n"
    for name, specialty in rows:
        result += f"- {name} ({specialty})\n"
    return result

@tool
def check_doctor_availability(dentist_name: str, appointment_time: str) -> str:
    """Check if the given dentist is available at the specified appointment time."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if dentist has any appointment at this time
    cursor.execute("""
        SELECT * FROM appointments
        WHERE dentist_name = ? AND appointment_time = ? AND status = 'booked'
    """, (dentist_name, appointment_time))

    conflict = cursor.fetchone()

    cursor.close()
    conn.close()

    if conflict:
        return f"{dentist_name} is already booked at {appointment_time}. Please choose another time."
    return f"{dentist_name} is available at {appointment_time}."


@tool
def display_doctor_slots() -> str:
    """Show each dentist's available days and their time slots."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, available_days, available_time_start, available_time_end FROM dentists")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No doctor schedule information available."

    result = "Doctor Availability:\n"
    for name, days, time_start, time_end in rows:
        result += f"- {name} is available on {days} from {time_start} to {time_end}\n"
    return result

@tool
def cancel_appointment(appointment_id: int, *, config: RunnableConfig) -> str:
    """Cancel an appointment for the configured patient."""
    configuration = config.get("configurable", {})
    patient_id = configuration.get("patient_id", None)
    if not patient_id:
        raise ValueError("No patient_id configured.")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM appointments WHERE appointment_id = ? AND patient_id = ?",
        (appointment_id, patient_id)
    )

    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return f"No appointment found with ID {appointment_id} for this patient."

    cursor.execute("DELETE FROM appointments WHERE appointment_id = ?", (appointment_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Appointment ID {appointment_id} successfully cancelled."


@tool
def confirm_appointment_call(phone_number: str, instructions: str, *, config: RunnableConfig) -> str:
    """Makes a confirmation call to the patient's phone number with specific instructions."""
    configuration = config.get("configurable", {})
    patient_id = configuration.get("patient_id", None)
    if not patient_id:
        raise ValueError("No patient_id configured.")

    url = "https://api.bland.ai/v1/calls"
    payload = {
        "phone_number": phone_number,
        "wait_for_greeting": True,
        "record": True,
        "task": instructions
    }

    headers = {
        "authorization": "org_c21a9b6b1776c061b19475a0c6e8bb878dc62641d2dc0e23e09a786be56225ae7d1b8195f57e3ec34c6c69",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return f"Call initiated. Response: {result}"
    except requests.RequestException as e:
        return f"Call failed: {str(e)}"

dental_tools = [
    create_appointment,
    fetch_patient_appointments,
    update_appointment_time,
    cancel_appointment,
    confirm_appointment_call,
    display_doctors,
    check_doctor_availability,
    display_doctor_slots
   
]
dental_assistant_runnable = primary_assistant_prompt | llm.bind_tools(dental_tools)