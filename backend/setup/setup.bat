@set mypath=%~dp0

call conda create -n smoking-area-count python=3.8.5
call conda smoking-area-count
call pip install -r requirements
call pip install -r formatter-requirements