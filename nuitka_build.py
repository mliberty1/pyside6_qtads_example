# Copyright 2023-2025 Jetperch LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil
import subprocess
import sys


def nuitka():
    # https://nuitka.net/index.html
    rc = subprocess.run(
        [
            sys.executable,
            '-m',
            'nuitka',
            '--standalone',
            '--company-name=Jetperch LLC',
            '--product-name=Joulescope UI',
            '--file-version=1.0.0',
            '--product-version=1.0.0',
            '--file-description=PySide6 QtAds Example',
            '--copyright=2025 Jetperch LLC',
            '--assume-yes-for-downloads',
            '--enable-plugin=pyside6',
            '--python-flag=no_docstrings',
            '--python-flag=isolated',
            '--msvc=latest',  # for Windows
            '--windows-console-mode=force',  # todo remove
            '--embed-debug-qt-resources',
            '--report=nuitka_report.xml',
            '--output-filename=pyside6_qtads_example',
            'main.py',
        ],
    )
    rc.check_returncode()
    return 0


if __name__ == '__main__':
    try:
        sys.exit(nuitka())
    except Exception as ex:
        print(ex)
        sys.exit(1)
