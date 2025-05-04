from typing import Optional, Dict, Any, List
from pydantic import BaseModel

class HRHiringState(BaseModel):
    input: Optional[str] = None
    memory: Optional[Dict[str, Any]] = {}
    proceed: Optional[bool] = False
    output: Optional[str] = None

    job_descriptions: Optional[Dict[str, str]] = None
    checklist: Optional[List[str]] = None
    salary_estimates: Optional[str] = None
