import subprocess
import json
import os
from app.llm import extract_email, extract_text_from_image
from datetime import datetime

def execute_task(task: str):
    try:
        if "install uv" in task.lower():
            subprocess.run(["pip", "install", "uv"], check=True)
            return {"message": "uv installed successfully"}

        elif "format" in task.lower():
            subprocess.run(["npx", "prettier", "--write", "/data/format.md"], check=True)
            return {"message": "File formatted"}

        elif "count wednesdays" in task.lower():
            with open("/data/dates.txt") as f:
                dates = f.readlines()
            count = sum(1 for date in dates if datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2)
            with open("/data/dates-wednesdays.txt", "w") as f:
                f.write(str(count))
            return {"message": "Wednesdays counted", "count": count}

        elif "extract email" in task.lower():
            with open("/data/email.txt") as f:
                email_content = f.read()
            sender_email = extract_email(email_content)
            with open("/data/email-sender.txt", "w") as f:
                f.write(sender_email)
            return {"message": "Email extracted", "email": sender_email}

        elif "extract credit card" in task.lower():
            card_number = extract_text_from_image("/data/credit-card.png")
            with open("/data/credit-card.txt", "w") as f:
                f.write(card_number.replace(" ", ""))
            return {"message": "Credit card number extracted"}

        else:
            return {"error": "Task not recognized"}

    except Exception as e:
        return {"error": str(e)}
