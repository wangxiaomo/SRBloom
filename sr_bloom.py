#-*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

import numpy
from PIL import Image
import config
from helper import do_offset

#1: load the degraded images
logging.info('%2d degraded images' % config.IMAGE_COUNT)
input_images = []
for degrade_index in range(config.IMAGE_COUNT):
    image = Image.open('%s/saved_%02d.jpg' % (config.DEGRADED_IMG_PATH, degrade_index))
    input_images.append(image)
    logging.info('append %2d images into input_images' % degrade_index)

#2: sr bloom it.
scale = config.SCALE
high_res_size = [int(input_images[0].size[1]*scale), int(input_images[0].size[0]*scale), 3]
high_res_image = numpy.zeros(high_res_size).astype(numpy.float32)
for degrade_img in input_images:
    HR_arr = numpy.asarray(degrade_img.resize((high_res_size[1], high_res_size[0]), Image.ANTIALIAS))
    high_res_image += numpy.dstack(do_offset(HR_arr[:,:,0],))

for (offset, LR_img) in input_images:
        HR_arr = numpy.asarray(LR_img.resize((high_res_size[1],high_res_size[0]), Image.ANTIALIAS))
        high_res_image += numpy.dstack((camera.doOffset(HR_arr[:,:,0],(-dx,-dy)),
                                        camera.doOffset(HR_arr[:,:,1],(-dx,-dy)),
                                        camera.doOffset(HR_arr[:,:,2],(-dx,-dy))))
    high_res_image = high_res_image / len(input_images) # take average value
    high_res_image = Image.fromarray(numpy.uint8(high_res_image))
