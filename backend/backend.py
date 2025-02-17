from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, Grievance, LostItem
from faiss_handler import add_grievance_to_faiss, retrieve_similar_grievance
from grievance_classifier import classify_grievance
from mistral_chat import generate_chat_response
from yolo_detect import detect_objects

app = FastAPI()

class GrievanceRequest(BaseModel):
    name: str
    roll_number: str
    category: str
    description: str

@app.post("/submit_grievance/")
async def submit_grievance(grievance: GrievanceRequest, db: Session = Depends(SessionLocal)):
    new_grievance = Grievance(**grievance.dict(), status="Pending")
    db.add(new_grievance)
    db.commit()
    add_grievance_to_faiss(grievance.description, new_grievance.id)
    return new_grievance

@app.post("/grievance_suggestion/")
async def grievance_suggestion(description: str):
    return {"suggested_category": classify_grievance(description)}

class ChatMessage(BaseModel):
    user_query: str

@app.post("/chat/")
async def chat(message: ChatMessage):
    matched_grievance = retrieve_similar_grievance(message.user_query)
    if matched_grievance:
        return {"reply": f"Based on past grievances: {matched_grievance['text']}"}
    return {"reply": generate_chat_response(message.user_query)}

@app.get("/track/{ticket_id}")
async def track_grievance(ticket_id: int, db: Session = Depends(SessionLocal)):
    grievance = db.query(Grievance).filter(Grievance.id == ticket_id).first()
    return grievance or {"error": "Ticket not found"}

class ImageRequest(BaseModel):
    image_url: str

@app.post("/detect_lost_item/")
async def detect_lost_item(request: ImageRequest):
    return {"detected_objects": detect_objects(request.image_url)}