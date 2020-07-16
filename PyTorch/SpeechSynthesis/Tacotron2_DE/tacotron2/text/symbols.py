""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from tacotron2.text import cmudict

#english symbols
_pad        = '_'
_punctuation = '!\'(),.:;? '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#german symbols
pad = ''
_punctuation = ',;:!?/.‘’“()[]&̈–'
_special = '-'
_letters = 'aAáäÄbBcCćçdDeEéêfFgGhHiIïjJkKlLmMnNoOôöÖpPqQrRřsSśßtTuUüÜvVwWxXyYzZ'
_digits = '0123456789'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:

#english 
#symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet

#german
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + list(_digits)

