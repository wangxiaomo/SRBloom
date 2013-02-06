#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

import random
from PIL import Image

import config

random.seed()
im = Image.open('samples/stars.jpg')

for degrade_index in range(config.IMAGE_COUNT):
    logging.info("degrade the file of %2d" % degrade_index)
    shift_x = random.uniform(0.0, config.RFACTOR)
    shift_y = random.uniform(0.0, config.RFACTOR)
    #TODO:hack method
    logging.info("shift_x %5f shift_y %5f" % (shift_x, shift_y))
    shift_x, shift_y = map(int, (shift_x, shift_y))
    degraded_im = im.offset(shift_x, shift_y)
    # add noise into the img file
    degraded_im.save('%s/saved_%02d.jpg' % (config.DEGRADED_IMG_PATH, degrade_index), 'JPEG')
    logging.info('save %s/saved_%02d.jpg' % (config.DEGRADED_IMG_PATH, degrade_index))
