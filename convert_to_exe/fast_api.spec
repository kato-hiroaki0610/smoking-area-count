# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
   ('.\\..\\..\\frontend\\dist\\smoking-area-count\\index.html', '.\\web\\index.html')
]

paths = [
   'E:\\project\\smoking-area-count\\backend\\src'
]

a = Analysis(['E:\\project\\smoking-area-count\\backend\\src\\fast_api.py'],
             pathex=paths,
             binaries=[],
             datas=added_files,
             hiddenimports=[
                'uvicorn.logging',

                # LOOP_SETUPS
                'uvicorn.loops',
                'uvicorn.loops.auto',
                'uvicorn.loops.asyncio',
                'uvicorn.loops.uvloop',

                # HTTP_PROTOCOLS
                'uvicorn.protocols',
                'uvicorn.protocols.http',
                'uvicorn.protocols.http.auto',
                'uvicorn.protocols.http.h11_impl',
                'uvicorn.protocols.http.httptools_impl',

                # WS_PROTOCOLS
                'uvicorn.protocols.websockets',
                'uvicorn.protocols.websockets.auto',
                'uvicorn.protocols.websockets.websockets_impl',
                'uvicorn.protocols.websockets.wsproto_impl',

                # LIFESPAN
                'uvicorn.lifespan',
                'uvicorn.lifespan.on',
                'uvicorn.lifespan.off',

                'fast_api',
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='fast_api',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
