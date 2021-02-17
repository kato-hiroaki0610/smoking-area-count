@set PYTHONPATH=%PATH%;%~dp0\src
@call activate smoking-area-count
@call uvicorn src.fast_api:app --reload