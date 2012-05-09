"""A python library for interacting with the Google Translate API.
"""

__author__ = "Dan Drinkard <dan.drinkard@gmail.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2012 Dan Drinkard"
__license__ = "BSD"

import urllib
import urllib2
try:
    import json
except ImportError:
    import simplejson as json


class GTranslatorError(Exception):
    """Exception for API errors"""


class GTranslatorAPIResponse(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.__dict__)


class GTranslation(GTranslatorAPIResponse):
    """Response object for translations"""


class GLanguage(GTranslatorAPIResponse):
    """Response object for language detection"""


class Translator(object):
    version = 'v2'
    base_uri = "https://www.googleapis.com/language/translate"

    def __init__(self, **kwargs):
        self.key = kwargs.get('key', None)

    def call(self, method, **kwargs):
        if self.key is None:
            raise GTranslatorError('Missing Google Services API key.')

        url = "%s/%s/%s" % (self.base_uri, self.version, method)
        kwargs.update(key=self.key)

        request_method = kwargs.get('method', 'GET')
        if 'method' in kwargs.keys():
            request_method = kwargs['method']
            del kwargs['method']

        if 'timeout' in kwargs.keys():
            timeout = kwargs['timeout']
            del kwargs['timeout']
        else:
            timeout = 3

        try:
            if request_method == 'GET':
                url = "%s?%s" % (url, urllib.urlencode(kwargs))
                if kwargs.get('debug'):
                    print 'calling %s' % url
                response = urllib2.urlopen(url, None, timeout).read()
            elif request_method == 'POST':
                print 'calling %s...' % url
                response = urllib2.urlopen(url, urllib.urlencode(kwargs), timeout).read()
            else:
                raise GTranslatorError('HTTP verbs other than GET and POST aren\'t implemented.')
        except urllib2.HTTPError, e:
            raise GTranslatorError(e)
        except ValueError, e:
            raise GTranslatorError(e)

        return response

    def translate(self, text, **kwargs):
        kwargs.update(q=text)
        response = json.loads(self.call('', **kwargs))
        results = [GTranslation(**translation) for translation in response['data']['translations']]
        if len(results) == 1:
            return results[0]
        return results

    def detect(self, text, **kwargs):
        kwargs.update(q=text)
        response = json.loads(self.call('detect', **kwargs))
        results = []
        # TODO: WHY does this method return a list of lists? In what circumstances are both dimensions used?
        for detections in response['data']['detections']:
            results += [GLanguage(**language) for language in detections]
        return results

    def languages(self, **kwargs):
        response = json.loads(self.call('languages', **kwargs))
        results = [GLanguage(**language) for language in response['data']['languages']]
        return results
