import requests


class OAuth2:
    """Authorization object using OAuth2 to define API info."""

    def __init__(self, base_url: str, client_id: str, client_secret: str, scope: str):
        """
        A constructor function. It is called when an object of the class is created.
        
        :param base_url: https://api.box.com/2.0
        :type base_url: str
        :param client_id: The client ID of the application you registered in Azure AD
        :type client_id: str
        :param client_secret: The client secret you received from the developer portal
        :type client_secret: str
        :param scope: The scope of the access request expressed as a list of space-delimited,
        case-sensitive strings. The strings are defined by the host server
        :type scope: str
        """
        self.base_url = base_url
        self.auth_token = self._authenticate(client_id, client_secret, scope)

    def _authenticate(self, client_id: str, client_secret: str, scope: str) -> str:
        """
        It takes in a client_id, client_secret, and scope, and returns an access token.
        
        :param client_id: The client ID of the application you created in the developer portal
        :type client_id: str
        :param client_secret: The client secret for the application
        :type client_secret: str
        :param scope: 'https://api.ebay.com/oauth/api_scope'
        :type scope: str
        :return: The access token
        """

        url = self.base_url + '/identity/connect/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        payload = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': scope
        }

        r = requests.post(url=url, headers=headers, data=payload)

        if r.status_code == 200:
            print('Authenticated Successfully')
            return_value = r.json()
            auth = f"{return_value['token_type']} {return_value['access_token']}"
            return auth

        else:
            raise ValueError(
                "Server Error: " + str(r.status_code) +
                '.  ' + r.json()['error']
            )