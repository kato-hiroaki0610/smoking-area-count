@set mypath=%~dp0
@call cd src
@call activate smoking-area-count
uvicorn fast_api:app --reload