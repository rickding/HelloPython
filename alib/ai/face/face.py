import json
import logging

log = logging.getLogger(__name__)


class Face:
    index = 0
    locations = None
    landmarks = None
    encoding = None
    image = None
    image_file = None

    def __init__(self, index, locations, landmarks, encoding, image):
        self.index = index
        self.locations = locations
        self.landmarks = landmarks
        self.encoding = encoding
        self.image = image


class FaceEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Face):
            return face2dict(o)
        super(FaceEncoder, self).default(o)


def face2dict(obj):
    return {
        'index': obj.index,
        # 'locations': obj.locations,
        # 'landmarks': obj.landmarks,
        # 'encoding': obj.encoding,
        'image_file': obj.image_file,
    }


def dict2face(dict_parse):
    obj = Face(
        dict_parse.get('index'), dict_parse.get('locations'),
        dict_parse.get('landmarks'), dict_parse.get('encoding'),
        dict_parse.get('image')
    )
    obj.image_file = dict_parse.get('image_file')
    return obj
