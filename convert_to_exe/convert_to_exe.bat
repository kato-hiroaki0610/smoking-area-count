@call activate pyinstaller
@call pyinstaller --distpath ../release fast_api.spec
@call rm -rf dist
@call cp -r ../backend/src/setting ../release
rem @call rm -rf build
