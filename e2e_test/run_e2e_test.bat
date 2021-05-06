rem @set PYTHONPATH=%PATH%;%~dp0\src
@set PATH=%PATH%;%~dp0
@call activate e2e_test
@call pytest