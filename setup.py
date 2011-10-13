import os
import glob
from distutils.core import setup
import py2exe
import PyQt4
pyqt4_dir = os.path.dirname(PyQt4.__file__)

setup(
    options = {'py2exe': {'compressed': 1,
                          'optimize': 2,
                          'bundle_files': 3,
                          'includes': ['sip']}},
    zipfile = None,
    windows = [{'script': 'pydemowindow.py' }],
    data_files=[('imageformats', glob.glob(os.path.join(pyqt4_dir, 'plugins', 'imageformats', '*.dll')))]
    )

