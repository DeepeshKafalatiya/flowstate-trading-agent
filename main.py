from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import init_db, get_active_workflow, register_interaction
from agent import process_trading_strategy

app = FastAPI(title="FlowState Trading Agent backend API", version="1.0")

# Database Initialization during startup
init_db()

class StrategyRequest(BaseModel):
    prompt: str

@app.post("/api/v1/initialize-workflow")
def initialize_workflow(request: StrategyRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Strategy prompt cannot be blank.")
    success = process_trading_strategy(request.prompt)
    if success:
        return {"status": "success", "message": "Disciplined trading sequence established."}
    raise HTTPException(status_code=500, detail="Failed to parse workflow configuration.")

@app.get("/api/v1/current-workflow")
def current_workflow():
    workflow_steps = get_active_workflow()
    formatted_steps = []
    for step in workflow_steps:
        formatted_steps.append({
            "id": step[0],
            "step_name": step[1],
            "priority": step[2],
            "allocated_time": step[3],
            "status": step[4]
        })
    return {"workflow": formatted_steps}