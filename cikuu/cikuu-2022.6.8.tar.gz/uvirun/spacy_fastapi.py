# 2022.6.29  
from uvirun import *
import spacy
if not hasattr(spacy, 'nlp'): spacy.nlp  = spacy.load('en_core_web_sm')

@app.get('/spacy/tok', tags=["spacy"])
def spacy_tok(text:str='The quick fox jumped over the lazy dog.',chunks:bool=False, morph:bool=False): 
	''' select * from url('http://cpu76.wrask.com:8000/spacy/tok', JSONEachRow, 'i UInt32, head UInt32, off UInt32, lex String, text_with_ws String,lem String, pos String, tag String, dep String, gov String') ''' 
	doc = spacy.nlp(text) 
	dic = { t.i: {'i':t.i, "head":t.head.i, 'off':t.idx, 'lex':t.text, 'text_with_ws':t.text_with_ws, 'lem':t.lemma_, 'pos':t.pos_, 'tag':t.tag_, 'dep':t.dep_, "gov":t.head.lemma_ + "_" + t.head.pos_ }  for t in doc }
	if morph: [v.update({"morph":json.dumps(doc[i].morph.to_dict())}) for i,v in dic.items()]
	if chunks: 
		[v.update({"chunks":[]}) for k,v in dic.items()]
		[ dic[ sp.end - 1 ]['chunks'].append( {'lempos': doc[sp.end - 1].lemma_ + "_NOUN", "type":"NP", "chunk":sp.text.lower() } ) for sp in doc.noun_chunks]   ## start/end ? 
	return [ v for v in dic.values()]  # colored VERB html

@app.get('/spacy/chunks', tags=["spacy"])
def spacy_chunks(text:str='The quick fox jumped over the lazy dog.'): 
	''' add vp_matcher,  the fox:NP-DET NOUN ''' 
	doc = spacy.nlp(text) 
	return [{"chunk":sp.text.lower() +":NP-" + " ".join([ doc[i].pos_ for i in range(sp.start, sp.end)])} for sp in doc.noun_chunks if sp.end - sp.start > 1] 

@app.get('/spacy/trp', tags=["spacy"])
def spacy_trp(text:str='The boy is happy. The quick fox jumped over the lazy dog.'): 
	''' select * from url('http://cpu76.wrask.com:8000/spacy/trp', JSONEachRow, 'rel String, gov String, dep String') ''' 
	return [{'rel':f"{t.dep_}_{t.head.pos_}_{t.pos_}", "gov":t.head.lemma_, 'dep':t.lemma_}  for t in spacy.nlp(text)  ]

@app.get('/spacy/snt', tags=["spacy"])
def spacy_snt(text:str='I think I plan to go swimming.', funcs:str="vp,verbnet,clause"): 
	''' select * from url('http://cpu76.wrask.com:8000/spacy/snt?text=I%20think%20I%20plan%20to%20go%20swimming.&func=vp%2Cverbnet%2Cclause', LineAsString )  ''' 
	import en 
	mapf = { 
	"clause":	lambda doc	: [ {"verb":v.lemma_, "type":type, "start":start, "end":end, "chunk":chunk } for v,type, start, end, chunk in en.clause(doc)],
	"verbnet":	lambda doc	: [ {"verb":doc[verb_i].lemma_,  "start":start, "end":end, "chunk":chunk } for verb_i, start, end, chunk in en.verbnet_matcher(doc)],
	"vp":	lambda doc		: [ {"verb":doc[start].lemma_,  "start":start, "end":end, "chunk":chunk } for vp, chunk, start, end in en.vp_matcher(doc)],
	}
	doc = spacy.nlp(text)
	return { f: mapf.get(f, lambda doc: [])(doc)  for f in funcs.strip().split(',') }

@app.get('/spacy/meta', tags=["spacy"])
def doc_meta(text:str='She is happy.'): 
	''' {"pred":"jumped", "sub": "fox", "obj":"dog" } ''' 
	try:
		doc		= spacy.nlp(text) 
		predi	= [ t.i for t in doc if t.dep_ == 'ROOT'][0]
		meta	= {	t.dep_: t.text	for t in doc if t.dep_ not in ('punct') and t.head.i == predi } #if t.dep_ in ('nsubj','dobj','acomp') and t.head.i == predi:  meta[t.dep_] = t.text 
		return meta
	except Exception as e:
		print("ex:", e) 

@app.post('/spacy/desc', tags=["spacy"])
def doc_desc(dic:dict = { "Person=1": "第一人称",
  "Person=3": "第三人称",
  "Person=2": "第二人称",
  "Number=Sing": "单数",
  "Gender=Fem": "阴性",
  "Gender=Masc": "阳性",
  "auxpass":"被动",
  "AUX": "助动词",
  "VERB": "动词",
  "NOUN": "名词",
  "ADJ": "形容词",
  "JJR": "比较级",
  "JJS": "最高级", 
  "ADV": "副词",
  "RBR": "比较级",
  "RBS": "最高级", 
  "PRON": "代词",
  "dobj": "宾语",
  "nsubj": "主语",
  "ROOT": "谓语",
  "acomp": "表语",
  "Tense=Pres": "现在时",
  "Tense=Past": "过去时"}
			, text:str='She is happy.', debug:bool=True): 
	''' 句子成分描述, 2022.7.10 '''
	doc		= spacy.nlp(text) #t.morph.to_json():  'Case=Nom|Number=Sing|Person=1|PronType=Prs'
	predi	= [ t.i for t in doc if t.dep_ == 'ROOT'][0]
	lat = { t.i: [ f"单词<span class='{t.pos_} {t.tag_}'>{t.text}</span>是 {dic[t.pos_]}"] if t.pos_ in dic else []  for t in doc  } 
	[ lat[t.i].append( dic[t.dep_] if t.dep_  in ('ROOT','auxpass') else f"单词<span class='{t.head.pos_} {t.head.tag_}'>{t.head.text}</span>的{dic[t.dep_]}" )  for t in doc if t.dep_ in dic and t.head.i == predi ] # only show the first level, the direct child of pred 
	[ lat[t.i].append( dic[t.tag_]) for t in doc if t.tag_ in dic ] # JJR
	[ lat[t.i].append( dic[pair])  for t in doc for pair in t.morph if pair in dic ] # Person=1
	res =  {"result": ["，".join(v) for v in lat.values() if v]}
	if debug: res['tok'] = { t.i: (t.text, t.pos_, t.tag_, t.dep_, t.head.i, t.morph.to_json()) for t in doc}
	return res

@app.get('/spacy/highlight', tags=["spacy"])
def doc_highlight(text:str='And the quick fox hit the lazy dog.', as_html:bool=False): #, pos:str='ADJ'
	''' return html, with pos highlighted ''' 
	doc = spacy.nlp(text) 
	color = {'ROOT': 'red', 'dobj': 'gray', 'nsubj':'darkgray', 'cc':'orange'}
	dic = { t.i:  f"<span class='{t.pos_}' style='color:{color.get(t.dep_, 'black')}'>{t.text_with_ws}</span>" for t in doc }
	for sp in doc.noun_chunks :
		if sp.end - sp.start > 1 : 
			dic[sp.start] = "<u>" + dic[sp.start]
			dic[sp.end-1] = dic[sp.end-1] + "</u>"
	html = "<h1>"  + "".join([ v for v in dic.values()]) + "</h1>"
	return HTMLResponse(content=html) if as_html else [{"html": html }]

@app.get('/spacy/toks', tags=["spacy"])
def spacy_toks(text:str='The boy is happy. The quick fox jumped over the lazy dog.',chunks:bool=False, sino:str='sino', native:str='dic'): 
	''' [{'i': 0, 'head': 1, 'lex': 'The', 'lem': 'the', 'pos': 'DET', 'tag': 'DT', 'dep': 'det', 'gov': 'boy_NOUN', 'chunks': []}, {'i': 1, 'head': 2, 'lex': 'boy', 'lem': 'boy', 'pos': 'NOUN', 'tag': 'NN', 'dep': 'nsubj', 'gov': 'be_AUX', 'chunks': [{'lempos': 'boy_NOUN', 'type': 'NP', 'chunk': 'the boy'}]}, {'i': 2, 'head': 2, 'lex': 'is', 'lem': 'be', 'pos': 'AUX', 'tag': 'VBZ', 'dep': 'ROOT', 'gov': 'be_AUX', 'chunks': []}, {'i': 3, 'head': 2, 'lex': 'happy', 'lem': 'happy', 'pos': 'ADJ', 'tag': 'JJ', 'dep': 'acomp', 'gov': 'be_AUX', 'chunks': []}, {'i': 4, 'head': 2, 'lex': '.', 'lem': '.', 'pos': 'PUNCT', 'tag': '.', 'dep': 'punct', 'gov': 'be_AUX', 'chunks': []}] JSONEachRow format , added 2022.6.25 ''' 
	from dic.word_idf import word_idf 
	from dic.word_awl import word_awl
	from cos_fastapi  import cos_lemma_keyness
	doc = spacy.nlp(text) 
	dic = { t.i: {'i':t.i, "head":t.head.i, 'off':t.idx, 'idf': word_idf.get(t.text.lower(), 0),'awl': 1 if t.text.lower() in word_awl else 0, 
		'keyness': cos_lemma_keyness(t.pos_, t.lemma_, sino, native) if t.pos_ in ('NOUN','VERB','ADJ','ADV') else 0 , 
		'lex':t.text, 'text_with_ws':t.text_with_ws, 'lem':t.lemma_, 'pos':t.pos_, 'tag':t.tag_, 'dep':t.dep_, "gov":t.head.lemma_ + "_" + t.head.pos_ }  for t in doc}
	if chunks: 
		[v.update({"chunks":[]}) for k,v in dic.items()]
		[ dic[ sp.end - 1 ]['chunks'].append( {'lempos': doc[sp.end - 1].lemma_ + "_NOUN", "type":"NP", "chunk":sp.text.lower() } ) for sp in doc.noun_chunks]   ## start/end ? 
	return [ v for v in dic.values()]  # colored VERB html

@app.get("/spacy/terms", tags=["spacy"])
def nlp_terms(text:str="The quick fox jumped over the lazy dog. The justice delayed is justice denied."):
	''' for sqlite indexing, 2022.3.4 '''
	tdoc = spacy.nlp(text)
	arr = []
	for sent in tdoc.sents: 
		doc = sent.as_doc()
		arr.append( { "snt": sent.text, 
		"tokens": [ {"id": t.i,"offset":t.idx, "word": t.text, "lemma":t.lemma_, "is_stop":t.is_stop, "parent": -1, "np_root": False, "pos": t.pos_, "tag": t.tag_, "dep": t.dep_,"text_with_ws": t.text_with_ws, "head": t.head.i , "sent_start": t.is_sent_start, "sent_end":t.is_sent_end}  for t in doc], 
		"triples": [ {"id":t.i,"offset":t.idx, "rel": t.dep_, "govlem":t.head.lemma_, "govpos": t.head.pos_, "deplem": t.lemma_, "deppos": t.pos_} for t in doc], 
		"chunk": [ {"id": np.start, "offset": doc[np.start].idx, "lem": doc[np.end-1].lemma_, "chunk":np.text, "end":np.end} for np in doc.noun_chunks], 
		} )
	return arr 

@app.get("/spacy/sntbr", tags=["spacy"])
def nlp_sntbr(text:str="The quick fox jumped over the lazy dog. The justice delayed is justice denied.", trim:bool=True):
	'''  '''
	return spacy.sntbr(text, trim) 

@app.get("/spacy/wordidf", tags=["spacy"])
def nlp_wordidf(snt:str="The quick fox jumped over the lazy dog.", topk:int=3):
	'''  '''
	from dic.word_idf import word_idf 
	from collections import Counter
	doc = spacy.nlp(snt)
	si  = Counter()
	[  si.update({t.text.lower() : word_idf.get(t.text.lower(), 0)}) for t in doc ]
	return [{"word":w, "idf":idf} for w , idf in si.most_common(topk) if idf > 0  ]

@app.get("/spacy/ecdic", tags=["spacy"])
def nlp_ecdic(snt:str="The quick fox jumped over the lazy dog."):
	'''  '''
	from dic.ecdic import ecdic
	doc = spacy.nlp(snt)
	return [  { "word": t.lemma_, "trans": ecdic[t.lemma_]} for t in doc if not t.is_stop and t.lemma_ in ecdic ]

if __name__ == "__main__":  #uvicorn.run(app, host='0.0.0.0', port=19200)
	#print (spacy_tok(morph=True))	
	print ( doc_desc()) 