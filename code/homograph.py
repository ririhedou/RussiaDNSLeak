# -*- coding: utf-8 -*-
import codecs

"""
This is more of visual translation also avoiding multiple char translation
e.g. £ may be written as {pound}
"""

#http://jrgraphix.net/r/Unicode/0020-007F
# The Punycode is an ASCII representation of the Unicode characters and symbols.

#a language-specific script or alphabet, such as Arabic, Chinese, Cyrillic, Tamil, Hebrew
#or the Latin alphabet-based characters with diacritics or ligatures, such as French

import string

#TODO Basic Latin
glyphs_basic_latin = {
        'a': [u'\u0061'],
        'b': [u'\u0062'],
        'c': [u'\u0063'],
        'd': ['b', u'\u0064'],
        'e': [u'\u0065'],
        'f': [ u'\u0066'],
        'g': ['q',u'\u0067'],
        'h': ['lh', 'ih', u'\u0068'],
        'i': ['1', 'l', u'\u0069'],
        'j': [u'\u006A'],
        'k': ['lk', 'ik', 'lc',u'\u006B'],
        'l': ['1', 'i', u'\u006C'],
        'm': ['n', 'nn', 'rn', 'rr', u'\u006D'],
        'n': ['m', 'r', u'\u006E'],
        'o': ['0', 'O', u'\u006F'],
        'p': [u'\u0070'],
        'q': [u'\u0071'],
        'r': [u'\u0072'],
        's': [u'\u0053', u'\u0073' ],
        't': [u'\u0074'],
        'u': [u'\u0075'],
        'v': [u'\u0075'],
        'w': ['vv', u'\u0077'],
        'x': [u'\u0078'],
        'y': [u'\u0079'],
        'z': [u'ʐ', u'ż', u'ź', u'ʐ', u'ᴢ']
        }

#TODO extend Latin

#TODO
#TODO Greek and Coptic


if __name__ == "__main__":

    print (u"\u2145")
    pass

    idna_encoded_bytes = u'xn--b-web'
    utf8_encoded_bytes = idna_encoded_bytes.decode('idna')
    print (utf8_encoded_bytes)

    #idna -> extract
    #print ("----Unicode----")
    #test = u'a'
    #for i in glyphs_basic_latin[test]:
    #        print i
    print (u'\u0062\u0335')
    print (u'\u0180')