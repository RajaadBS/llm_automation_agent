from fastapi import FastAPI, HTTPException
from app.tasks import execute_task
from app.security import validate_task

app = FastAPI()

@app.post("/run")
def run_task(task: str):
    if not validate_task(task):
        raise HTTPException(status_code=400, detail="Invalid or unsafe task")

    result = execute_task(task)
    if result.get("error"):
        raise HTTPException(status_code=500, detail=result["error"])
    
    return {"status": "success", "result": result}

@app.get("/read")
def read_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
