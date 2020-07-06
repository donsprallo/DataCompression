# flake8: noqa: F401
from .bwt import bwt, ibwt
from .mtf import mtf, imtf
from .rle import rle, irle

""" This dictionary contains the possible encoder and decoder functions as values in a tuple (encoder, decoder). """
compressors = {
    'rle': (rle, irle),
    'mtf': (mtf, imtf),
    'bwt': (bwt, ibwt)
}


def encode(data: bytes, encoder: str) -> bytes:
    """ Encodes the data with the selected encoder. """

    if encoder in compressors:
        return compressors[encoder][0](data)
    else:
        raise Exception('No valid encoder.')


def decode(data: bytes, decoder: str) -> bytes:
    """ Decodes the data with the selected decoder. """

    if decoder in compressors:
        return compressors[decoder][1](data)
    else:
        raise Exception('No valid decoder.')
