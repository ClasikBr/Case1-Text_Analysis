from typing import Any, Dict

from fastapi import FastAPI, HTTPException, Request

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, Any]:
  return {"ok": True}


@app.post("/analyze")
async def analyze(request: Request) -> Dict[str, Any]:
  try:
    payload = await request.json()
  except Exception:
    raise HTTPException(status_code=400, detail="Invalid JSON")
  text = payload.get("text", "")
  # Простая заглушка анализа. Замените на реальную логику позже.
  return {"language": "und", "polarity": 0.0, "subjectivity": 0.0, "text": text}
