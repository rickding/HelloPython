import logging

log = logging.getLogger(__name__)


class Face:
    index = 0
    locations = None
    landmarks = None
    encoding = None
    image = None

    def __init__(self, index, locations, landmarks, encoding, image):
        self.index = index
        self.locations = locations
        self.landmarks = landmarks
        self.encoding = encoding
        self.image = image
