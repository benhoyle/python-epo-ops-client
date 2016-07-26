# -*- coding: utf-8 -*-

from datetime import datetime
import logging
import os

from six.moves import urllib

from dateutil.tz import tzutc

from .exceptions import InvalidDate

log = logging.getLogger(__name__)


def makedirs(path, mode=0o777):
    try:
        os.makedirs(path, mode)
    except OSError:
        pass


def now():
    return datetime.now(tzutc())


def quote(string):
    return urllib.parse.quote(string, safe='/\\')


def validate_date(date):
    if date is None or date == '':
        return ''
    try:
        datetime.strptime(date, '%Y%m%d')
        return date
    except ValueError:
        raise InvalidDate('{0} is not a valid YYYYMMDD date.'.format(date))

def check_list(listvar):
    if not isinstance(listvar, list):
        listvar = [listvar]
    return listvar
    
def safeget(dct, *keys):
    """ Recursive function to safely access nested dicts or return None. 
    param dict dct: dictionary to process
    param string keys: one or more keys"""
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct

def keysearch(d, key):
    """Recursive function to look for first occurence of key in multi-level dict. 
    param dict d: dictionary to process
    param string key: key to locate"""
 
    if isinstance(d, dict):
        if key in d:
            return d[key]
        else:
            if isinstance(d, dict):
                for k in d:
                    found = keysearch(d[k], key)
                    if found:
                        return found
            else:
                if isinstance(d, list):
                    for i in d:
                        found = keysearch(d[k], key)
                        if found:
                            return found