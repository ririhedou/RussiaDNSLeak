#!/usr/bin/env python
# -*- coding: utf-8 -*-

#depenence
"""
https://goo.gl/X3Uenw

wget url_to_download_snappy;
tar xf snappy-x.y.z.tar.gz;
cd snappy-x.y.z; ./configure;
make install;
pip install python-snappy


chrome idn policy:
https://www.chromium.org/developers/design-documents/idn-in-google-chrome

"""
__author__ = 'ketian'
__version__ = '1.04b'
__email__ = 'ririhedou@gmail.com'

import pprint
#import snappy
import fastavro as avro
#from avro import schema, datafile, io
#import squatting_detect
from  squatting_detect import compare_with_a_base_domain


#TODO for the reference
schema = {
    "namespace": "astrolavos.avro",
    "type": "record",
    "name": "ActiveDns",
    "fields": [
        {"name": "date", "type": "string"},
        {"name": "qname", "type": "string"},
        {"name": "qtype", "type": "int"},
        {"name": "rdata", "type": ["string", "null"]},
        {"name": "ttl", "type": ["int", "null"]},
        {"name": "authority_ips", "type": "string"},
        {"name": "count", "type": "long"},
        {"name": "hours", "type": "int"},
        {"name": "source", "type": "string"},
        {"name": "sensor", "type": "string"}
    ]
}


def analyze_avro(avro_file):

    with open(avro_file, 'r') as fo:
        reader = avro.reader(fo)
        # will raise a fastavro.reader.SchemaResolutionError in case of
        # incompatible schema
        schema = reader.schema
        print ("Schema is")

        base_domain = u'facebook'
        base_domain = u'paypal'
        c = 0

        pp = pprint.PrettyPrinter(indent=4)
        for record in reader:

            pp.pprint(record)
            raw_input()
            old_qname = record['qname']
            qname = record['qname']
            #print (qname)
            if len(qname) > 1:
                try:
                    qname = qname[:-1].decode('idna')
                    compare_with_a_base_domain(qname,base_domain,old_qname)
                except:
                    f = open('unicode-log-error.log','a')
                    f.write(qname)
                    f.write('\n')
                    f.flush()
                    f.close()
            else:
                print ('WARNING')
                print (qname)
            c += 1

        print ("total",c)


if __name__ == "__main__":
    active_dns_file = "/home/datashare/dns/2week/20170820"
    active_dns_file_local_test_data = "../data/part-r-00001.avro"
    analyze_avro(active_dns_file_local_test_data)
