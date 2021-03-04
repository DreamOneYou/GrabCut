# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
block_cipher = None
hiddenimports_numpy = collect_submodules('numpy')
hidden_imports_cv2 = collect_submodules('cv2')
hidden_imports_PyQt5 = collect_submodules('PyQt5')

block_cipher = None

all_hidden_imports = hiddenimports_numpy + hidden_imports_cv2 + hidden_imports_PyQt5

a = Analysis(['GMM.py'],
             pathex=['E:\\项目\\GraphCut\\graph_cut'],
             binaries=[],
             datas=[],
             hiddenimports=all_hidden_imports,
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
          name='GMM',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
