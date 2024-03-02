import json
import csv
import os

NOTES_JSON_FILE = "notes.json"
NOTES_CSV_FILE = "notes.csv"

def load_notes_from_json():
    if os.path.exists(NOTES_JSON_FILE):
        with open(NOTES_JSON_FILE, "r") as f:
            return json.load(f)
    return []

def load_notes_from_csv():
    if os.path.exists(NOTES_CSV_FILE):
        with open(NOTES_CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f, delimiter=';')
            return list(reader)
    return []

def save_notes_to_json(notes):
    with open(NOTES_JSON_FILE, "w") as f:
        json.dump(notes, f, indent=4)

def save_notes_to_csv(notes):
    with open(NOTES_CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "content", "date_created", "last_modified"], delimiter=';')
        writer.writeheader()
        writer.writerows(notes)
