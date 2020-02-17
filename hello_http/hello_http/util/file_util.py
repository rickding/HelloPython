from __future__ import absolute_import, unicode_literals

import logging
import os
from tempfile import NamedTemporaryFile

log = logging.getLogger(__name__)


def save(path, name, data):
    if data is None or name is None:
        return

    path = mk_dir(path)

    # Save file
    file = open(file_path(path, name), "wb")
    log.info('Save to file: %s, %s, %d' % (file.name, type(data), len(data)))

    file.write(data)
    file.flush()
    file.close()
    return file.name


def save_temp(data, ext=None, prefix=None):
    if data is None:
        return

    # Save to temp file
    temp = NamedTemporaryFile(delete=False, suffix=ext, prefix=prefix)
    log.info('Save to temp file: %s, %s, %d' % (temp.name, type(data), len(data)))

    temp.write(data)
    temp.close()
    return temp.name


def temp_path(sub_path=None):
    if sub_path is None:
        return './tmp'

    return os.path.join('./tmp', sub_path)


def mk_dir(path):
    if path is None:
        return

    path = path.strip()
    path = path.rstrip("\\")

    if not os.path.exists(path):
        os.makedirs(path)
    return path


def file_path(path, name):
    if path is None:
        return name

    if name is None or len(name) <= 0:
        return os.path.normpath(path)

    return os.path.normpath(os.path.join(path, name))


def exists(path):
    if path is None:
        return False

    return os.path.exists(path)
