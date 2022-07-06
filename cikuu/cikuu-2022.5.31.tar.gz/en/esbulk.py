# 2022-6-18 rename to esbulk.py 
import json,fire,sys, os, hashlib ,time 
import warnings
warnings.filterwarnings("ignore")

import en  
from en import terms,verbnet,spacybs
from en.dims import docs_to_dims
attach = lambda doc: ( terms.lempos_type(doc), verbnet.attach(doc), doc.user_data )[-1]  # return ssv, defaultdict(dict)

def sntdoc_idsour(sid, snt, doc, actions): 
	''' 2022.6.18 '''
	actions.append( {'_id': sid, '_source': 
		{'type':'snt', 'snt':snt, 'pred_offset': en.pred_offset(doc), 'src': sid,  'tc': len(doc), 
		'kp': [ f"{t.lemma_}_{t.pos_}" for t in doc if t.pos_ not in ('PUNCT')] + [ f"{t.dep_}_{t.head.pos_}_{t.pos_}/{t.head.lemma_} {t.lemma_}" for t in doc if t.pos_ not in ('PUNCT')],  #added 2022.6.23 | "select snt from gzjc where type = 'snt' and kp = 'book_VERB' limit 2"
		'postag':' '.join([f"{t.text}_{t.lemma_}_{t.pos_}_{t.tag_}" if t.text == t.text.lower() else f"{t.text}_{t.text.lower()}_{t.lemma_}_{t.pos_}_{t.tag_}" for t in doc]),
		} } )
	[ actions.append( {'_id': f"{sid}-tok-{t.i}", '_source': 
		{"type":"tok", "src":sid, 'i':t.i, "head":t.head.i, 'lex':t.text, 'lem':t.lemma_, 'pos':t.pos_, 'tag':t.tag_, 'dep':t.dep_, "gov":t.head.lemma_ + "_" + t.head.pos_} }) for t in doc ] #"gpos":t.head.pos_, "glem":t.head.lemma_
	[ actions.append( {'_id': f"{sid}-np-{sp.start}", '_source': 
		{"type":"np", "src":sid,  'lempos':doc[sp.end-1].lemma_  + "_" + doc[sp.end-1].pos_, 'chunk':sp.text.lower(), 'start':sp.start, 'end':sp.end} }) for sp in doc.noun_chunks ]
	[ actions.append( {'_id': f"{sid}-{id}", '_source': dict(sour, **{"src":sid}) } ) 
		for id, sour in attach(doc).items() if not id.startswith('tok-') and not id.startswith('trp-')]
	actions.append( { '_id': f"{sid}-stype", '_source': {"type":"stype", "tag": "simple_snt" if en.simple_sent(doc) else "complex_snt", "src":sid} } )
	if en.compound_snt(doc) : actions.append( { '_id': f"{sid}-stype-compound", '_source': {"type":"stype", "tag": "compound_snt", "src":sid} } )

from so import * # config
def submit(infile, idxname=None, host='127.0.0.1',port=9200, refresh:bool=True, batch:int=500000,topk:int=None):
	''' submit gzjc.spacybs to ES , 2022.6.1 '''
	if idxname is None : idxname = infile.split('.')[0] 
	es = Elasticsearch([ f"http://{host}:{port}" ])  
	if refresh and es.indices.exists(index=idxname) : es.indices.delete(index=idxname)
	if not es.indices.exists(index=idxname): es.indices.create(index=idxname, body=config)
	print ('start to load :', infile, flush=True)
	start = time.time()
	actions=[]
	for rowid, snt, bs in spacybs.Spacybs(infile).items() :
		doc		= en.from_docbin(bs) 
		sid		= rowid # to connect with: SELECT dictGet('snt_gzjc', 'snt', 7000), | f"{idxname}-{rowid}"
		if topk and rowid > topk : break  # added 2022.6.20 
		sntdoc_idsour(sid, snt, doc, actions)
		if len(actions) >= batch: 
			helpers.bulk(client=es,actions=[ dict(ar, **{'_op_type':'index', '_index':idxname}) for ar in actions], raise_on_error=False)
			print ( actions[-1], flush=True)
			actions = []
	if actions : helpers.bulk(client=es,actions=[ dict(ar, **{'_op_type':'index', '_index':idxname}) for ar in actions], raise_on_error=False)
	print(f"{infile} is finished, \t| using: ", time.time() - start) 
	
if __name__ == '__main__':
	fire.Fire(submit)