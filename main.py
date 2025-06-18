from fastapi import FastAPI
from pydantic import BaseModel
from agents.intent_classifier import classify_intent
from agents.router import route_query          # ✅ Add this line
from agents.notify_agent import notify_user
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class Query(BaseModel):
    user_id: str
    message: str

# Chat endpoint
@app.post("/chat")
def chat_handler(query: Query):
    intent = classify_intent(query.message)
    response = route_query(intent, query)
    notify_user(query.user_id, intent)
    return {"response": response}