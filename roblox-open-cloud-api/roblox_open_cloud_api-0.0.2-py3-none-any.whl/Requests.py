# Imports
from requests import Session, Response

# Class
class RequestsClass:
	# variables
	_REQUESTS_SESSION = Session()

	_API_KEY = None
	_COOKIES = {}
	_HEADERS = {
		"Content-Type" : "application/json",
		"User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36",
		"x-api-key" : "not-set"
	}

	# Set a cookie for the requests instance cookies
	def setCookie(self, cookie_name : str, cookie_value : str, domain : str) -> None:
		print(cookie_name, cookie_value, domain)
		self._COOKIES[cookie_name] = {
			"name": cookie_name,
			"value": cookie_value,
			"domain": domain
		}

	# Set a header for the requests instance headers
	def setHeader(self, header_name, header_value) -> None:
		print(header_name, header_value)
		self._HEADERS[header_name] = header_value

	# update cookies, headers, etc
	def updateSessionInfo(self):
		for cookie in self._COOKIES:
			self._REQUESTS_SESSION.cookies.set_cookie(cookie)
		for headerName, headerValue in self._HEADERS.items():
			self._REQUESTS_SESSION.headers[headerName] = headerValue
		self._REQUESTS_SESSION.headers['x-api-key'] = self._API_KEY

	# methods
	def get(self, url : str) -> Response:
		self.updateSessionInfo()
		return self._REQUESTS_SESSION.get(url)

	def post(self, url : str, data : any) -> Response:
		self.updateSessionInfo()
		return self._REQUESTS_SESSION.post(url, data)

	def delete(self, url : str) -> Response:
		self.updateSessionInfo()
		return self._REQUESTS_SESSION.delete(url)

	def request(self, method : str, url : str, params : any, data : any) -> Response:
		self.updateSessionInfo()
		return self._REQUESTS_SESSION.request(method, url, params, data)

	def patch(self, url : str, data : any) -> Response:
		self.updateSessionInfo()
		return self._REQUESTS_SESSION.patch(url, data)

	# Init
	def __init__(self, api_key=None, cookies=None, headers=None):
		self._API_KEY = api_key
		if cookies != None:
			self._COOKIES = cookies
		if headers != None:
			self._HEADERS = headers
