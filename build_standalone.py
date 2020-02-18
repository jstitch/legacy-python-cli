# -*- coding: utf-8 -*-

import platform
import subprocess
from pathlib import Path
from zipfile import ZipFile


CWD = Path(__file__).resolve().parent
OS = platform.system().lower().replace('darwin', 'mac')
MACHINE = platform.machine()


ABOUT = {}
with open(Path(CWD, "wakatime/__about__.py")) as f:
    exec(f.read(), ABOUT)


if __name__ == '__main__':
    dist = Path(CWD, 'dist')
    subprocess.run(
        [
            'pyinstaller',
            '--onefile',
            '--noconfirm',
            '--clean',
            '--name', 'wakatime',
            '--distpath', str(dist),
            '--hidden-import', 'pkg_resources.py2_warn',
            str(Path(CWD, 'wakatime', 'cli.py')),
        ],
        check=True,
    )

    filename = 'wakatime-{ver}-{os}-{machine}.zip'.format(
        ver=ABOUT["__version__"],
        os=OS,
        machine=MACHINE,
    )

    with ZipFile(str(Path(dist, filename)), 'w') as myzip:
        myzip.write(str(Path(CWD, 'dist', 'wakatime')), arcname='wakatime')