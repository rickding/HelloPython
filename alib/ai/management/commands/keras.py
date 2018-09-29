import logging

import numpy
from django.core.management.base import BaseCommand
from keras.layers import Dense
from keras.models import Sequential

log = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed = 7
        numpy.random.seed(seed)

        dataset = numpy.loadtxt('a.csv', delimiter=',')
        X = dataset[:, 0:8]
        Y = dataset[:, 8]

        model = Sequential()
        model.add(Dense(16, input_dim=8, init='uniform', activation='relu'))
        model.add(Dense(8, init='uniform', activation='relu'))

        model.add(Dense(1, init='uniform', activation='sigmoid'))

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X, Y, nb_epoch=150, batch_size=10)

        scores = model.evaluate(X, Y)
        log.info('%s: %.2f%%' % (model.metrics_names[1], scores[1] * 100))
        return 'keras: %s' % str(scores)
