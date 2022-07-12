import requests
import sys
import requests
import json
from pprint import pprint


class ValdDashboardAPI:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        scope: str = "api.dashbord",
        auth_url: str = "https://security.valdperformance.com/connect/token",
        base_url: str = "https://dbapi.valdperformance.com/v2018q3",
    ):
        """Python class to work with VALD Dashboard API.

        Args:
            client_id (str): The API client_id provided by Vald customer support.
            client_secret (str): The API client_secret provided by Vald customer support.
            scope (str): Scope of the Oauth2 request. Default is api.dashbord. Yes there's a typo in dashboard.
            auth_url (str): URL for authentication with OAuth2. Defaults to https://security.valdperformance.com/connect/token.
            base_url (str): Base URL for all API requests. Defaults to https://dbapi.valdperformance.com/v2018q3/.
        """
        self.scope = scope
        self.auth_url = auth_url
        self.base_url = base_url

        self.token = self._get_token(client_id, client_secret)

    def _get_token(self, client_id: str, client_secret: str):
        """Get a new Oauth2 bearer token.

        Args:
            client_id (str): The API client_id provided by Vald customer support.
            client_secret (str): The API client_secret provided by Vald customer support.
        """

        token_req_payload = {"grant_type": "client_credentials", "scope": self.scope}
        token_response = requests.post(
            self.auth_url,
            data=token_req_payload,
            auth=(client_id, client_secret),
        )
        if token_response.status_code != 200:
            print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        else:
            print("Successfuly obtained a new token")
            tokens = json.loads(token_response.text)
            return tokens["access_token"]

    def _make_request(self, method: str, path: str, parameters=None):
        """Function to standardize requests made to the API.

        Args:
            method (str): Method to use. GET, POST, etc.
            path (str): API path to query.
            parameters (dict, optional): Parameters to pass the queried path. See the official API documentation here: https://dbapi.valdperformance.com/index.html
        """

        url = self.base_url + path
        params = {}
        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }

        s = requests.Session()
        if parameters:
            params.update(parameters)
        response = s.request(method, url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(
                str(response.status_code)
                + ": "
                + response.reason
                + ": "
                + str(response.content)
            )
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    def get_teams(self):
        """Teams endpoint provides a list of all Teams available to a client."""
        return self._make_request("GET", "/teams")

    def get_team_detail(self, team_id: int = 4842):
        """Provides detailed information for the provided Team Id."""
        return self._make_request("GET", f"/teams/{team_id}")

    def get_team_athletes(self, team_id: int = 4842):
        """Returns the complete list of all athletes in a given team."""
        return self._make_request("GET", f"/teams/{team_id}/athletes")

    def get_athlete_detail(self, team_id: int = 4842, athlete_id: int = 821168):
        """Returns detailed information for the provided Athlete Id."""
        return self._make_request("GET", f"/teams/{team_id}/athletes/{athlete_id}")

    def get_athlete_groups(self, team_id: int = 4842):
        """Provides a list of all of the Groups associated with a give Team."""
        return self._make_request("GET", f"/teams/{team_id}/groups")

    def get_athlete_in_groups(self, team_id: int = 4842, group_id: int = 1234):
        """Provides a list of all of the athletes in the provided Group Id."""
        return self._make_request("GET", f"/teams/{team_id}/groups/{group_id}/athletes")

    def get_athlete_tests(
        self, team_id: int = 4842, athlete_id: int = 821168, page_number: int = 1
    ):
        """Lists all known Tests for an Athlete at the time of the request.
        Tests are ordered in descending order, by Start Time."""
        return self._make_request(
            "GET", f"/teams/{team_id}/athletes/{athlete_id}/tests/{page_number}"
        )

    def get_athlete_tests_by_date(
        self,
        team_id: int = 4842,
        athlete_id: int = 821168,
        page_number: int = 1,
        date_from: str = "2022-01-01",
        date_to: str = "2022-12-31",
    ):
        """Returns all of the Tests for a given Athlete within the specified date range.
        Tests are ordered in descending order, by Start Time. Dates should be in the ISO8601 format e.g yyyy-mm-dd"""
        return self._make_request(
            "GET",
            f"/teams/{team_id}/athletes/{athlete_id}/tests/{date_from}/{date_to}/{page_number}",
        )

    def get_team_tests(self, team_id: int = 4842, page_number: int = 1):
        """Returns all of the Test for a given team. Tests are ordered in descending order, by Start Time."""
        return self._make_request("GET", f"/teams/{team_id}/tests/{page_number}")

    def get_team_tests_by_date(
        self,
        team_id: int = 4842,
        page_number: int = 1,
        date_from: str = "2022-01-01",
        date_to: str = "2022-12-31",
    ):
        """Returns all of the Test for a given team within the specified date range.
        Tests are ordered in descending order, by Start Time. Dates should be in the ISO8601 format e.g yyyy-mm-dd."""
        return self._make_request(
            "GET", f"/teams/{team_id}/tests/{date_from}/{date_to}/{page_number}"
        )
