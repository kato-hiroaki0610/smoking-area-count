@call activate pyinstaller
@call pyinstaller fast_api.spec
@call mv dist/fast_api.exe ../release
@call rm -rf dist
@call cp -r ../backend/src/setting ../release
rem @call rm -rf build
