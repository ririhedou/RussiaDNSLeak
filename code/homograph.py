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
        'a': [u'à', u'á', u'â', u'ã', u'ä', u'å', u'ɑ', u'а', u'ạ', u'ǎ', u'ă', u'ȧ', u'ӓ'],
        'b': ['d', 'lb', 'ib', u'ʙ', u'Ь', u'b̔', u'ɓ', u'Б'],
        'c': [u'ϲ', u'с', u'ƈ', u'ċ', u'ć', u'ç'],
        'd': ['b', 'cl', 'dl', 'di', u'ԁ', u'ժ', u'ɗ', u'đ'],
        'e': [u'é', u'ê', u'ë', u'ē', u'ĕ', u'ě', u'ė', u'е', u'ẹ', u'ę', u'є', u'ϵ', u'ҽ'],
        'f': [u'Ϝ', u'ƒ', u'Ғ'],
        'g': ['q', u'ɢ', u'ɡ', u'Ԍ', u'Ԍ', u'ġ', u'ğ', u'ց', u'ǵ', u'ģ'],
        'h': ['lh', 'ih', u'һ', u'հ', u'Ꮒ', u'н'],
        'i': ['1', 'l', u'Ꭵ', u'í', u'ï', u'ı', u'ɩ', u'ι', u'ꙇ', u'ǐ', u'ĭ'],
        'j': [u'ј', u'ʝ', u'ϳ', u'ɉ'],
        'k': ['lk', 'ik', 'lc', u'κ', u'ⲕ', u'κ'],
        'l': ['1', 'i', u'ɫ', u'ł'],
        'm': ['n', 'nn', 'rn', 'rr', u'ṃ', u'ᴍ', u'м', u'ɱ'],
        'n': ['m', 'r', u'ń'],
        'o': ['0', u'Ο', u'ο', u'О', u'о', u'Օ', u'ȯ', u'ọ', u'ỏ', u'ơ', u'ó', u'ö', u'ӧ'],
        'p': [u'ρ', u'р', u'ƿ', u'Ϸ', u'Þ'],
        'q': ['g', u'զ', u'ԛ', u'գ', u'ʠ'],
        'r': [u'ʀ', u'Г', u'ᴦ', u'ɼ', u'ɽ'],
        's': [u'Ⴝ', u'Ꮪ', u'ʂ', u'ś', u'ѕ'],
        't': [u'τ', u'т', u'ţ'],
        'u': [u'μ', u'υ', u'Ս', u'ս', u'ц', u'ᴜ', u'ǔ', u'ŭ'],
        'v': [u'ѵ', u'ν', u'v̇'],
        'w': ['vv', u'ѡ', u'ա', u'ԝ'],
        'x': [u'х', u'ҳ', u'ẋ'],
        'y': [u'ʏ', u'γ', u'у', u'Ү', u'ý'],
        'z': [u'ʐ', u'ż', u'ź', u'ʐ', u'ᴢ']
        }

#TODO extend Latin

#TODO
#TODO Greek and Coptic


if __name__ == "__main__":

    print (u"\u2145")
    pass

    idna_encoded_bytes = u'\u0e44\u0e17\u0e22'
    utf8_encoded_bytes = idna_encoded_bytes.encode('idna')
    print (utf8_encoded_bytes)

    #idna -> extract
