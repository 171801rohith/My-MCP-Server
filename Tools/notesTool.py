from models import MyNotes
from database import SessionLocal
from typing import List


def get_my_notes() -> List[dict]:
    with SessionLocal() as db:
        notes = db.query(MyNotes).all()
        if notes:
            return [
                {"id": note.id, "note": note.note, "date_time": note.date_time}
                for note in notes
            ]
        else:
            return f"No notes to return."


def add_note(content: str) -> str:
    try:
        db = SessionLocal()
        note = MyNotes(note=content)
        db.add(note)
        db.commit()
        db.refresh(note)
        return f"{note} with note_id: {note.id} added successfully at time: {note.date_time}."

    except Exception as e:
        db.rollback()
        print("Error:", e)
        return f"Failed to add - {note}."
