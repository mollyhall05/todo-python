from setuptools import setup

APP=['main.py']
DATA_FILES=[('resources',['tasks.json'])]
OPTIONS = {'argv_emulation': True,
           'includes': [],
           'resources': ['tasks.json'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)