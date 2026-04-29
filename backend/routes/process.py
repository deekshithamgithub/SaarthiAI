from fastapi import APIRouter
from models.schemas import RequestModel
from services.auth_service import authenticate
from services.nlp_service import process_text
from services.risk_service import detect_risk
from services.insight_service import get_insights

router = APIRouter()

@router.post("/process")
def process(req: RequestModel):

    if not authenticate(req.user_id):
        return {"error": "Unauthorized"}

    intent = process_text(req.text)
    risk = detect_risk(req.user_id, intent)
    insights = get_insights(req.user_id)

    return {
        "intent": intent,
        "risk": risk,
        "insights": insights
    }
