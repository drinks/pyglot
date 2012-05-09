pyglot
======

A python library for interacting with the Google Translate API.

**Note: This uses the translate v2 API**

You will need a **server** key configured with Google, and a payment method on file,
as there is no courtesy limit for translations.

Usage:
------
See the [Google Translate docs](https://developers.google.com/translate/v2/using_rest) for more details.

    >>> from pyglot import Translator
    >>> lang = Translator(key='YOUR-KEY')

    # Translating text:
    >>> lang.translate('The quick brown fox jumped over the lazy dog', target='de')
    GTranslation({u'translatedText': u'Der schnelle braune Fuchs sprang \xfcber den faulen Hund', u'detectedSourceLanguage': u'en'})

    # Detecting the language of text:
    >>> lang.detect('The quick brown fox jumped over the lazy dog')
    [GLanguage({u'isReliable': False, u'confidence': 0.79904306, u'language': u'en'})]

    # Getting a list of language codes, with names in english:
    >>> lang.languages(target='en')
    [GLanguage({u'name': u'Afrikaans', u'language': u'af'}), GLanguage({u'name': u'Albanian', u'language': u'sq'}), ... ]

