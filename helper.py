#-*- coding: utf-8 -*-

import numpy

def do_offset(data, offset, val=255):
    if offset[1]>0: data = numpy.concatenate((numpy.ones((offset[1],data.shape[1]))*val, data[0:-offset[1],:]), axis=0)
    if offset[1]<0: data = numpy.concatenate((data[-offset[1]:,:], numpy.ones((-offset[1],data.shape[1]))*val), axis=0)
    if offset[0]>0: data = numpy.concatenate((numpy.ones((data.shape[0],offset[0]))*val, data[:,0:-offset[0]]), axis=1)
    if offset[0]<0: data = numpy.concatenate((data[:,-offset[0]:], numpy.ones((data.shape[0],-offset[0]))*val), axis=1)
    return data
