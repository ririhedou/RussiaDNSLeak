# used for data processing
# -*- coding: utf-8 -*-
# this is python 2.7

__author__ = "ketian"
__time__ = "Jun 2017"

import os
import pickle

def saveintopickle(obj, filename="obj.pickle"):
    with open(filename, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print ("[Pickle]: save object into {}".format(filename))
    return


def loadfrompickle(filename="obj.pickle"):
    with open(filename, 'rb') as handle:
        b = pickle.load(handle)

    print ("done the loading")
    return b


def read_zone_files_from_a_dir(cwd=None):
    #get current cwd
    if cwd is None:
        cwd = os.getcwd()

    files = os.listdir(cwd)
    files_absolute_paths = []
    for i in files:
        if (str(i).endswith('.zone')):
            files_absolute_paths.append(cwd+'/'+str(i))
    return files_absolute_paths


def analyze_zone_files(zonefiles):
    for zonefile in zonefiles:
        open_and_parse_file_to_get_domains(zonefile)


def open_and_parse_file_to_get_domains(zonefile):
    domains =list()
    if zonefile.endswith('.zone'):
       tldName = zonefile.split('/')[-1][:-5]
       f = open(zonefile, 'r')
       for line in f.readlines():
           domain_array = line.strip().split() #by tab or space
           if len(domain_array) > 0:
               domain = domain_array[0].lower()
               if len(domain) == 0 or not domain.endswith('.'):
                    continue

               domain = domain[:-1]
               if domain == tldName:
                   continue

               domains.append(domain)
       f.close()
       unique = set(domains)
       print ("{}: length of lines: {}, unique domains {}".format(tldName,len(domains),len(unique)))
       saveintopickle(unique, tldName+'.pickle')


def load_from_pickle_and_analyse(pickle):
    print ('Loading........')
    ru = loadfrompickle(pickle)
    print (type(ru))
    for i in ru:
        print i
        print type(i)
        raw_input('input any to continue')
    #TODO implement your own analysis here

def specify_filtering_rule():
    pass

def analyze_domains_for_squatting(picklefile):
    sets = loadfrompickle(picklefile)
    for i in sets:
        if "facebook" in str(i):
            print (i)

    pass


"""
Please extract ru.zone.gz before analyzed
Analyzed:
/Users/ketian/Desktop/RussiaDNSLeak/ru.zone
/Users/ketian/Desktop/RussiaDNSLeak/su.zone
/Users/ketian/Desktop/RussiaDNSLeak/tatar.zone
/Users/ketian/Desktop/RussiaDNSLeak/дети.zone
/Users/ketian/Desktop/RussiaDNSLeak/рф.zone

Stored example:
'0--0--0.RU
"""
if __name__=="__main__":
    #load_from_pickle_and_analyse('su.pickle')
    #test()
    #open_and_parse_file_to_get_domains('ru.zone')
    #open_and_parse_file_to_get_domains('рф.zone')
    #load_from_pickle_and_analyse('дети.pickle')
    #analyze_domains_for_squatting("pickleFile/ru.pickle")
    for i in range(0x80, 0xFF):
        print unichr(i)