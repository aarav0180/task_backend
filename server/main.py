import os
import uuid
import shutil
import subprocess
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from threading import Thread
import time

app = FastAPI()
jobs_dir = "/tmp/jobs"
os.makedirs(jobs_dir, exist_ok=True)
jobs = {}

class ScheduleRequest(BaseModel):
    task: str

@app.post("/schedule")
def schedule(req: ScheduleRequest):
    job_id = str(uuid.uuid4())
    job_dir = os.path.join(jobs_dir, job_id)
    os.makedirs(job_dir)
    jobs[job_id] = {"status": "pending", "dir": job_dir, "result": None}
    Thread(target=run_job, args=(job_id, req.task, job_dir)).start()
    return {"job_id": job_id}

@app.get("/status/{job_id}")
def status(job_id: str):
    job = jobs.get(job_id)
    if not job:
        return JSONResponse(status_code=404, content={"error": "Job not found"})
    resp = {"status": job["status"]}
    if job["status"] == "complete":
        resp["download_url"] = f"/download/{job_id}"
    return resp

@app.get("/download/{job_id}")
def download(job_id: str):
    job = jobs.get(job_id)
    if not job or job["status"] != "complete":
        return JSONResponse(status_code=404, content={"error": "Not ready"})
    zip_path = os.path.join(jobs_dir, f"{job_id}.zip")
    shutil.make_archive(zip_path[:-4], 'zip', job["dir"])
    return FileResponse(zip_path, filename=f"{job_id}.zip")

def run_job(job_id, task, job_dir):
    jobs[job_id]["status"] = "running"
    with open(os.path.join(job_dir, "task.txt"), "w") as f:
        f.write(task)
    time.sleep(10)
    jobs[job_id]["status"] = "complete"
