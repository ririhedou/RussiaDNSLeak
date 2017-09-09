#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ketian'
__version__ = '1.04b'
__email__ = 'ririhedou@gmail.com'

import sys,re
from os import path
import pickle
import editdistance

import sys
reload(sys)
sys.setdefaultencoding('utf8')

EDIT_DISTANCE_THRESHOLD = 2
HYPHEN_DISTANCE_THRESHOLD = 4
DOMAIN_LENGTH_THRESHOLD = 20


candidates =[u'facebook', u'youtube', u'paypal', u'bankofamerica.com', u'chase', u'wellsfargo', u'citi' ]

FUZZER_CATEGORY = ['typo-squatting','homo-squatting','bits-squatting','combo-squatting', 'various']

DIR = path.abspath(path.dirname(sys.argv[0]))
DIR_DB = 'database'
FILE_TLD = path.join(DIR, DIR_DB, 'effective_tld_names.dat')
DB_TLD = path.exists(FILE_TLD)


def __domain_tld(domain):
    domain = domain.rsplit('.', 2)

    if len(domain) == 2:
        return domain[0], domain[1]

    if DB_TLD:
        cc_tld = {}
        re_tld = re.compile('^[a-z]{2,4}\.[a-z]{2}$', re.IGNORECASE)

        for line in open(FILE_TLD):
            line = line[:-1]
            if re_tld.match(line):
                sld, tld = line.split('.')
                if not tld in cc_tld:
                    cc_tld[tld] = []
                cc_tld[tld].append(sld)

        sld_tld = cc_tld.get(domain[2])
        if sld_tld:
            if domain[1] in sld_tld:
                return domain[0], domain[1] + '.' + domain[2]

    return domain[0] + '.' + domain[1], domain[2]

def compare_with_a_base_domain(input_domain,base_domain):

    #print (input_domain)

    try:
        small_edit_distance(input_domain,base_domain)
        direct_contain_basename_with_larger_distance(input_domain,base_domain)
        long_hyphens_identify(input_domain,base_domain)

    except:
        f = open('log-error.log','a')
        f.write(input_domain)
        f.write('\n')
        f.flush()
        f.close()


def long_hyphens_identify(input_domain, base_domain):
    # long hyphens
    domain, tld = __domain_tld(input_domain)
    def count_continous_hypens(domain):
        count = 0
        for i in domain:
            if i == u'-':
                count += 1
                if count > HYPHEN_DISTANCE_THRESHOLD:
                    return True
            else:
                count = 0
        if count > HYPHEN_DISTANCE_THRESHOLD:
            return True
        return False

    if count_continous_hypens(domain):
        print (input_domain, domain, tld)
        f = open(base_domain + '.log', 'a')
        f.write(input_domain)
        f.write('\n')
        f.flush()
        f.close()
        return True

    return False


def direct_contain_basename_with_larger_distance(input_domain, base_domain):

    # contain the keyword of the basename
    domain, tld = __domain_tld(input_domain)
    if base_domain in domain:
        distance = editdistance.eval(domain, base_domain)
        if distance > EDIT_DISTANCE_THRESHOLD:
            print (input_domain, domain, tld)
            f = open(base_domain + '.log', 'a')
            f.write(input_domain)
            f.write('\n')
            f.flush()
            f.close()
            return True

    return False

def small_edit_distance(input_domain, base_domain):

    # a small edit-distance
    domain, tld = __domain_tld(input_domain)
    distance = editdistance.eval(domain, base_domain)
    if distance <= EDIT_DISTANCE_THRESHOLD:
        print (input_domain, domain, tld)
        f = open(base_domain + '.log', 'a')
        f.write(input_domain)
        f.write('\n')
        f.flush()
        f.close()
        return True

    return False

def long_domain_name(inputdomain):

    if len(inputdomain) > DOMAIN_LENGTH_THRESHOLD:
        return True

    return False


def loadfrompickle(filename="obj.pickle"):
    with open(filename, 'rb') as handle:
        b = pickle.load(handle)
    print ("done the loading")
    return b

def test(pickle):
    print ('Loading........')
    domainSets = loadfrompickle(pickle)

    print (type(domainSets))
    for i in domainSets:
        i = i.decode("idna")
        compare_with_a_base_domain(i,u'facebook')



if __name__ == "__main__":

    #test("../pickleFile/дети.pickle")
    #test("../pickleFile/ru.pickle")
    #test("../pickleFile/рф.pickle")

    #print (u'facebook' in u'facebook------------------------')
    #print (editdistance.eval(u'facebook',u'facebook------------------------'))
    domain  = 'xn--pfarmer-t2a.com'.decode("idna")
    #domain = 'fabooke'.decode('utf-8')
    print (domain)
    #domain = 'facebook'.decode("idna")
    #print domain

    print (__domain_tld("loging.facebook.----------sub-------------.malicious-domain.com"))
    print (__domain_tld("loging.facebook.----------sub-------------.facebook.com.cn"))
    #print (count_continous_hypens(domain))
    #print (editdistance.eval(domain,u'pfarmer.com'))