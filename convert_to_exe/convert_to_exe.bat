@call activate pyinstaller
@call pyinstaller --distpath ../release fast_api.spec
@call cp -r ../backend/src/setting ../release
@call rm -rf build
