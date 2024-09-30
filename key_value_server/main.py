# A simple key-value store server using FastAPI.

from fastapi import FastAPI, HTTPException
from typing import Dict, Any
from threading import Lock

app = FastAPI()
db = {}
lock = Lock()


# Store/Update a report for a given source
@app.post("/v1/{source}")
def store_report(source: str, report: Dict[str, Any]):
    old = db.get(source, None)
    if old:
        report = {**old, **report}
    with lock:
        db[source] = report
    return {"message": "Report stored successfully"}


# Store/Update a single value for a given source
@app.post("/v1/{source}/{key}")
def store_report(source: str, key: str, value: Any):
    with lock:
        if source in db:
            db[source][key] = value
        else:
            db[source] = {key: value}
    return {"message": "Report stored successfully"}


# Retrieve a report for a given source
@app.get("/v1/{source}")
def get_report(source: str):
    report = db.get(source)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report


# Retrieve a single value for the given source and key
@app.get("/v1/{source}/{key}")
def get_report(source: str, key: str):
    report = db.get(source)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    value = report.get(key)
    if not value:
        raise HTTPException(status_code=404, detail="Key not found")
    return value


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)
