@call activate pyinstaller
@call pyinstaller fast_api.spec
@call cp -r dist/fast_api.exe ../release
@call cp -r ../backend/src/setting dist
rem @call rm -rf build
