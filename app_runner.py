import requests
import json
import time
import pandas as pd

# 1. Define the local API endpoint addresses
CHOICE_URL = "http://localhost:8000/v1/choice"
NOUL_URL = "http://localhost:8000/v1/noul"

# 2. Incoming customer messages array
incoming_tickets = [
    "Hey, my login screen is throwing a 500 error code and I cannot access my files!",
    "Can someone help me clear a double charge from my credit card bill?",
    "Where can I find a list of your product pricing tiers for enterprises?",
    "YOU ABSOLUTELY RUINED MY EVENT, YOUR PRODUCT CRASHED AND I WANT MY MONEY BACK RIGHT NOW!!!",
    "Just wanted to say thank you for the quick help last week, great job team."
]

print("🚀 Starting Local 7B Automation Agent Pipeline...\n")
start_time = time.time()

# Array to hold row dictionaries for our CSV export
processed_data = []

# 3. Loop through each ticket sequentially
for idx, ticket in enumerate(incoming_tickets, 1):
    print(f"📄 Processing Ticket #{idx}...")
    
    # --- Task A: Route the Ticket (Choice Primitive) ---
    choice_payload = {
        "state": ticket,
        "options": ["billing_dept", "tech_support", "sales_dept", "general_inquiry"]
    }
    choice_resp = requests.post(CHOICE_URL, json=choice_payload).json()
    route = choice_resp["choice"]
    confidence = choice_resp["confidence"]
    
    # --- Task B: Audit for Aggression (Noul Primitive) ---
    noul_payload = {
        "state": ticket,
        "statement": "The ticket content uses angry phrasing, ALL CAPS, or demands a refund."
    }
    noul_resp = requests.post(NOUL_URL, json=noul_payload).json()
    anger_probability = noul_resp["noul"]
    
    # --- Task C: Set Action Status Rule ---
    if anger_probability > 0.65:
        action = "Escalated to Manager Queue"
    elif route == "tech_support" and confidence > 0.80:
        action = "Generated Tech Diagnostics Token"
    else:
        action = f"Assigned to {route}"
        
    print(f"   🎯 Route: {route} | 🔥 Escalation Risk: {anger_probability:.1%}")
    print(f"   ⚙️ Triggered Action: {action}\n")
    
    # Append structured metrics to our list
    processed_data.append({
        "Ticket_ID": idx,
        "Message": ticket,
        "Assigned_Route": route,
        "Routing_Confidence": round(confidence, 4),
        "Escalation_Risk": round(anger_probability, 4),
        "System_Action": action
    })

# 4. Process and Save to a Local Spreadsheet File
df = pd.DataFrame(processed_data)
csv_filename = "ticket_routing_results.csv"
df.to_csv(csv_filename, index=False)

total_duration = time.time() - start_time
print(f"🏆 Batch completed successfully in {total_duration:.2f} seconds!")
print(f"📊 Matrix saved to local spreadsheet -> {csv_filename}")
