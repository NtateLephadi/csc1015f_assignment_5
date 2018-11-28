"""
>>> from timeutil import validate
>>> validate('12::00 am')
False
>>> validate('012:00 am')
False
>>> validate('12:00 aa')
False
>>> validate('12:000 am')
False
>>> validate('14:00 am')
False
>>> validate('1:15 pm')
True

"""
import doctest
doctest.testmod(verbose=True)