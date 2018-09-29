# -*-coding: utf-8-*-
import logging
import os
from tempfile import NamedTemporaryFile

from django.conf import settings

log = logging.getLogger(__name__)


def del_path(path):
    if not exists(path):
        return

    if os.path.isfile(path):
        os.remove(path)
    else:
        os.rmdir(path)


def read(path, name):
    if name is None:
        return

    return open(full_path(path, name), 'rb')


def save(path, name, data):
    if data is None or name is None:
        return

    path = mk_dir(path)

    # Save file
    file = open(full_path(path, name), "wb")
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


def get_path(sub_path=None):
    if sub_path is None:
        return settings.BASE_DIR
    return os.path.join(settings.BASE_DIR, sub_path)


def temp_path(sub_path=None):
    if sub_path is None:
        return settings.TEMP_DIR
    return os.path.join(settings.TEMP_DIR, sub_path)


def full_path(path, name):
    if name is None:
        return

    if path is None:
        return name
    return os.path.normpath(os.path.join(path, name))


def mk_dir(path):
    if path is None:
        return

    path = path.strip()
    path = path.rstrip("\\")

    if not os.path.exists(path):
        os.makedirs(path)
    return path


def exists(path):
    if path is None:
        return False
    return os.path.exists(path)


def file_list(src_path):
    if src_path is None or len(src_path) <= 0:
        return None

    files = []
    if os.path.isfile(src_path):
        files.append(src_path)
    else:
        for root, dirs, names in os.walk(src_path):
            for file in names:
                files.append(os.path.join(root, file))

    return files


def is_ext(path, ext):
    if path is None or len(path) <= 0 or ext is None or len(ext) <= 0:
        return False
    return path.lower().endswith(ext.lower())
