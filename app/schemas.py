from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    prompt: str

class AnalyzeResponse(BaseModel):
    risk_score: int
    category: str
    ml_category: str
    is_malicious: bool
    matched_rules: List[str]
