@set PYTHONPATH=%PATH%;%~dp0\src
@call uvicorn src.fast_api:app
