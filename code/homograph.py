# -*- coding: utf-8 -*-
import codecs


"""
This is more of visual translation also avoiding multiple char translation
e.g. £ may be written as {pound}
"""

#http://jrgraphix.net/r/Unicode/0020-007F

#a language-specific script or alphabet, such as Arabic, Chinese, Cyrillic, Tamil, Hebrew
# or the Latin alphabet-based characters with diacritics or ligatures, such as French

import string
if __name__ == "__main__":
    print (u"\u2145")
    pass

    idna_encoded_bytes = u'\u0e44\u0e17\u0e22'
    utf8_encoded_bytes = idna_encoded_bytes.encode('idna')
    print (utf8_encoded_bytes)

    #idna -> extract
