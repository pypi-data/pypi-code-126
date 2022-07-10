from re import findall

class Tools(object):
	def __init__(self) -> int:
		...

	def textAnalysis(self , text : str) -> list:
		Results : list = []

		realText : str = text.replace("**","").replace("__","").replace("``","")
		bolds : list = findall(r"\*\*(.*?)\*\*" , text)
		italics : list = findall(r"\_\_(.*?)\_\_" , text)
		monos : list = findall(r"\`\`(.*?)\`\`" , text)

		bResult : list = [realText.index(i) for i in bolds]
		iResult : list = [realText.index(i) for i in italics]
		mResult : list = [realText.index(i) for i in monos]

		for bIndex , bWord in zip(bResult , bolds):
			Results.append({
				"from_index" : bIndex,
				"length" : len(bWord),
				"type" : "Bold"
			})

		for iIndex , iWord in zip(iResult , italics):
			Results.append({
				"from_index" : iIndex,
				"length" : len(iWord),
				"type" : "Italic"
			})

		for mIndex , mWord in zip(mResult , monos):
			Results.append({
				"from_index" : mIndex,
				"length" : len(mWord),
				"type" : "Mono"
			})

		return Results , realText