# -*- mode: python -*-


import os
from pmagpy import version
app_name = "magic_gui_{}".format(version.version[7:])
current_dir = os.getcwd()


block_cipher = None

files = [('{}/pmagpy/data_model/data_model.json'.format(current_dir), './pmagpy/data_model/'),
         ('{}/pmagpy/data_model/data_model.json'.format(current_dir), '.'),
         ('{}/pmagpy/data_model/*.json'.format(current_dir), './pmagpy/data_model/'),
         ('{}/dialogs/help_files'.format(current_dir), './dialogs/help_files/*.html')
]

a = Analysis(['programs/magic_gui.py'],
             pathex=[current_dir],
             binaries=[],
             datas=files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='magic_gui',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='{}/programs/images/PmagPy.ico'.format(current_dir))
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=app_name)
app = BUNDLE(coll,
             name='{}.app'.format(app_name),
             icon='{}/programs/images/PmagPy.ico'.format(current_dir),
             bundle_identifier=None)