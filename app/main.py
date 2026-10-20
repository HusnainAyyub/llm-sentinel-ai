from fastapi import FastAPI
from app.rules import rule_score
from app.classifier import predict
from app.schemas import AnalyzeRequest, AnalyzeResponse

app = FastAPI(title="LLM Sentinel AI", version="0.1.0")

@app.get("/")
def home():
    return {"project": "LLM Sentinel AI", "status": "running"}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
    score, category, matched = rule_score(req.prompt)
    try:
        ml_category = predict(req.prompt)
    except Exception:
        ml_category = category
    final_category = category if category != "benign" else ml_category
    return AnalyzeResponse(
        risk_score=score,
        category=final_category,
        ml_category=ml_category,
        is_malicious=score >= 40 or (ml_category != "benign" and score >= 20),
        matched_rules=matched,
    )
