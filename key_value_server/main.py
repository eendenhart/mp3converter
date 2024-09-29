# A simple key-value store server using FastAPI.

from fastapi import FastAPI, HTTPException
from typing import Dict
from threading import Lock

app = FastAPI()
db = {}
lock = Lock()

# POST /v1/{source} - Store a report for a given source
@app.post("/v1/{source}")
def store_report(source: str, report: Dict[str, str]):
    old = db.get(source, None)
    if old:
        report = {**old, **report}
    with lock:
        db[source] = report
    return {"message": "Report stored successfully"}


# GET /v1/{source} - Retrieve a report for a given source
@app.get("/v1/{source}")
def get_report(source: str):
    report = db.get(source)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)
