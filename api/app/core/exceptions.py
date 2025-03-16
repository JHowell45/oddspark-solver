from fastapi.exceptions import HTTPException

not_found_exception = HTTPException(status_code=404, detail="Model not found")
