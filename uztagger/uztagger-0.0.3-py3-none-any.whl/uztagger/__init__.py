from UzMorphAnalyser import UzMorphAnalyser
import re

class Tagger:
    def predict_pos(self, sentence: str):
        uzmorph = UzMorphAnalyser.UzMorphAnalyser()
        uzmorph.lemmatize('maktabimizni')
        return [('maktabimda', 'N'), ('kitoblar', 'N')]

    def help(self):
        return "help of usage of metoding"

    def pos_tags(self):
        return [
            ('NOUN', 'Noun',     'Ot'),
            ('ADJ',  'Adjective','Sifat'),
            ('NUM',  'Number',   'Son'),
            ('PRON', 'Pronoun',  'Olmosh'),
            ('ADV',  'Adverb',   'Ravish'),
            ('VERB', 'Verb',     'Fel'),

            ('CNJ', 'Conjuction', 'Bog`lovchi'),
            ('ADP',  'Adposition', 'Ko`makchi'),
            ('PRT',  'Particle',   'Yuklama'),

            ('INTJ', 'Interjection', 'Undov'),
            ('MOD',  'Modal',        'Modal'),
            ('IMIT', 'Imitation',    'Taqlid'),

            ('AUX',  'Auxilary verb', 'Yodamchi fel'),
            ('PPN',  'Proper Noun',   'Atoqli ot'),
            ('PUNC', 'Punctuation',   'Tinish belgi'),
            ('SYM',  'Symbol',        'Belgi')
        ]