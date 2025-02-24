
# PySide6 - QtAds - Nuitka example

This repo contains a minimal example to demonstrate the build problem for
https://github.com/Nuitka/Nuitka-commercial/issues/188.

The problem exists with:

- Python 3.13.2
- Nuitka commercial 2.6.7
- PySide6 6.8.2.1
- PySide6-QtAds 4.3.1.4


## Instructions

1. Install Python 3.13.2 for Windows 11.
2. Open PowerShell and type:
```PowerShell
python -m venv c:\venv\nuitka
c:\venv\nuitka\Scripts\Activate.ps1
python -m pip install nuitka PySide6-QtAds qtpy
python main.py
```

Confirm that the window appears.

Now build and test using Nuitka:

```PowerShell
python nuitka_build.py
.\main.dist\pyside6_qtads_example.exe
```

I see this:

```PowerShell
(nuitka) PS C:\repos\Jetperch\pyside6_qtads_example> .\main.dist\pyside6_qtads_example.exe
['__main__', '_abc', '_ast', '_codecs', '_collections', '_collections_abc', '_frozen_importlib', '_frozen_importlib_external', '_functools', '_imp', '_io', '_opcode', '_opcode_metadata', '_operator', '_signal', '_sre', '_stat', '_thread', '_tokenize', '_warnings', '_weakref', '_weakrefset', '_winapi', 'abc', 'ast', 'builtins', 'codecs', 'collections', 'collections.abc', 'contextlib', 'copyreg', 'dis', 'encodings', 'encodings.aliases', 'encodings.cp1252', 'encodings.utf_8', 'enum', 'functools', 'genericpath', 'importlib', 'importlib._bootstrap', 'importlib._bootstrap_external', 'importlib.machinery', 'inspect', 'io', 'itertools', 'keyword', 'linecache', 'marshal', 'nt', 'ntpath', 'opcode', 'operator', 'os', 'os.path', 're', 're._casefix', 're._compiler', 're._constants', 're._parser', 'reprlib', 'stat', 'sys', 'time', 'token', 'tokenize', 'types', 'weakref', 'winreg', 'zipimport']
Traceback (most recent call last):
  File "C:\repos\Jetperch\PYSIDE~4\MAIN~1.DIS\main.py", line 9, in <module>
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "C:\repos\Jetperch\PYSIDE~4\MAIN~1.DIS\PySide6QtAds\__init__.py", line 7, in <module PySide6QtAds>
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
SystemError: <built-in method exec_module of type object at 0x00007FF7AD726C20> returned NULL without setting an exception
(nuitka) PS C:\repos\Jetperch\pyside6_qtads_example>
```

Can "fix" this by renaming `c:\venv\nuitka\lib\site-package\PySide6-QtAds` folder to MyPySide6-QtAds and
changing main.py line 9 to:

```
from MyPySide6QtAds import CDockManager, CDockWidget, TopDockWidgetArea
```

I think that the presence of both `PySide6QtAds.\_\_init\_\_.py` and `PySide6QtAds.PySide6QtAds.pyd` is confusing the Nuitka import system.
