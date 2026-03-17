from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tickets = []

@app.get("/")
def home():
    return {"message": "IT Support API running"}

@app.get("/system")
def system_status():
    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }

@app.get("/alert")
def alerts():
    return {"alerts": []}

@app.get("/tickets")
def get_tickets():
    return tickets

@app.post("/ticket")
def create_ticket(issue: str):
    ticket = {"id": len(tickets) + 1, "issue": issue}
    tickets.append(ticket)
    return ticket
