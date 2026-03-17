from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil

app = FastAPI()

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Ticket storage
tickets = []

@app.get("/")
def home():
    return {"message": "IT Support System Running"}

@app.get("/system")
def system_status():
    return {
        "CPU": psutil.cpu_percent(),
        "Memory": psutil.virtual_memory().percent,
        "Disk": psutil.disk_usage('/').percent
    }

@app.get("/alert")
def alerts():
    cpu = psutil.cpu_percent()
    alerts = []

    if cpu > 80:
        alerts.append("High CPU usage detected")

    return {"alerts": alerts}

@app.get("/tickets")
def get_tickets():
    return tickets

@app.post("/ticket")
def create_ticket(issue: str):
    ticket = {
        "id": len(tickets) + 1,
        "issue": issue,
        "status": "open"
    }
    tickets.append(ticket)
    return ticket
