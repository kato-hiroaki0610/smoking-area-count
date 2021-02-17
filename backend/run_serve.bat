@set PYTHONPATH=%PATH%;%~dp0\src
@call activate smoking-area-count
rem @call uvicorn src.fast_api:app --reload
@call uvicorn src.fast_api:app
