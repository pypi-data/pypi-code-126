import ast
from threading import Thread
import flask
from flask import request, jsonify, Response, send_file
from .gdc_agent_utils import getQuery, serializeDtype
import pandas as pd
from typing import List, Tuple

class GDCAgent:
	agent_dfs = dict() # This will have all the dataframes

	schema = None

	# Constructor method. This will do the following:
	#	1. populate `agent_dfs`
	# 	2. constrct schema based on dataframes
	def __init__(self, data:List[Tuple[str, pd.DataFrame]]) -> None:
		tables = []
		for (t_name, df) in data:
			df.dropna(axis=0, inplace=True)
			df_index_name = df.index.name
			df.reset_index(inplace=True)
			cols = []
			for col in df.columns.tolist():
				col_dict = {
					"name": col,
					"type": serializeDtype(df[col].dtype),
					"nullable": True,
					"description": "get column " + col + " from " + t_name
				}
				cols.append(col_dict)
			t_dict = {
				"name" : t_name,
				"primary_key": [df_index_name],
				"description": "get data from " + t_name,
				"columns": cols
			}
			tables.append(t_dict)
			self.agent_dfs[t_name] = df
		print(self.schema)
		self.schema = {"tables": tables}

	# This is the flask app that will be used in `run_agent`
	app = flask.Flask(__name__)

	# This will run the flask app
	def run_agent(self):

		@self.app.route('/')
		def home():
			return "<h1>Hello World</h1>"

		@self.app.route('/capabilities', methods=['GET'])
		def capabilities():
			return send_file('capabilities.json')

		@self.app.route('/schema', methods=['GET'])
		def schema():
			return jsonify(self.schema)

		@self.app.route('/health', methods=['GET'])
		def health():
			return Response(status=204)

		@self.app.route('/query', methods=['POST'])
		def query():
			req = request.data
			req = ast.literal_eval(req.decode('utf-8'))
			table_name = req['table']
			df = self.agent_dfs[table_name]
			table_relationships = req["table_relationships"] if "table_relationships" in req else []
			query_request = req['query']
			query_output = getQuery(df, query_request, table_relationships, self.agent_dfs)
			return jsonify(query_output)
		
		t = Thread(target=self.app.run)
		t.start()
