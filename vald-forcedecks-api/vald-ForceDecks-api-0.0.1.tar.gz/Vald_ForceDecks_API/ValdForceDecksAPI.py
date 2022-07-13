import requests
import sys
import requests
import json
from pprint import pprint


class ValdForceDecksAPI:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        scope: str = "api.forcedecks",
        auth_url: str = "https://security.valdperformance.com/connect/token",
        base_url: str = "https://fdapi.valdperformance.com/v2019q3",
    ):
        """Python class to work with VALD Dashboard API.

        Args:
            client_id (str): The API client_id provided by Vald customer support.
            client_secret (str): The API client_secret provided by Vald customer support.
            scope (str): Scope of the Oauth2 request. Default is api.forcedecks. Yes there's a typo in dashboard.
            auth_url (str): URL for authentication with OAuth2. Defaults to https://security.valdperformance.com/connect/token.
            base_url (str): Base URL for all API requests. Defaults to https://fdapi.valdperformance.com/v2019q3.
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

    def _make_request(self, method: str, path: str, parameters: dict = None):
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
        """Returns a collection of Teams."""
        return self._make_request("GET", "/teams")

    def get_team_athletes(self, team_id: str = "a9f999be-249f-466a-b98e-b70605adee6d"):
        """Returns the complete list of all athletes of a given team.

        Args:
            team_id (str): The ID of the team. Defaults to 'a9f999be-249f-466a-b98e-b70605adee6d'.
        """
        return self._make_request("GET", f"/teams/{team_id}/athletes")

    def get_athlete_tests(
        self,
        team_id: str = "a9f999be-249f-466a-b98e-b70605adee6d",
        athlete_id: str = "5b054239-93c4-43db-8793-4264c352d6ff",
        page_number: int = 1,
    ):
        """Provides all of the Tests for the provided Team and Athlete Ids, optionally filtered by test last modified date/time. Tests are ordered in descending order, by Record Time. Dates should be specified as UTC in the ISO8601 format e.g yyyy-mm-ddThh:mm:ssZ This endpoint is paged.

        Args:
            team_id (str): The ID of the team. Defaults to 'a9f999be-249f-466a-b98e-b70605adee6d'.
            athlete_id (str): The ID of the athlete. Defaults to '5b054239-93c4-43db-8793-4264c352d6ff'.
            page_number (int): The page number to request. Defaults to 1.
        """
        return self._make_request(
            "GET", f"/teams/{team_id}/athlete/{athlete_id}/tests/{page_number}"
        )

    def get_athlete_tests_by_date(
        self,
        team_id: str = "a9f999be-249f-466a-b98e-b70605adee6d",
        athlete_id: str = "5b054239-93c4-43db-8793-4264c352d6ff",
        page_number: int = 1,
        date_from: str = "2022-01-01",
        date_to: str = "2022-12-31",
    ):
        """Returns all of the Tests for a given Athlete within the specified date range.
        Tests are ordered in descending order, by Start Time. Dates should be in the ISO8601 format e.g yyyy-mm-dd,

        Args:
            team_id (str): The ID of the team. Defaults to 'a9f999be-249f-466a-b98e-b70605adee6d'.
            athlete_id (str): The ID of the athlete. Defaults to '5b054239-93c4-43db-8793-4264c352d6ff'.
            page_number (int): The page number to request. Defaults to 1.
            date_from (str): The start date in ISO8601 format (yyyy-mm-dd). Defauls to 2022-01-01.
            date_to (str): The end date in ISO8601 format (yyyy-mm-dd). Defauls to 2022-12-31.
        """
        return self._make_request(
            "GET",
            f"/teams/{team_id}/athletes/{athlete_id}/tests/{date_from}/{date_to}/{page_number}",
        )

    def get_team_tests(
        self,
        team_id: str = "a9f999be-249f-466a-b98e-b70605adee6d",
        page_number: int = 1,
        modified_from: str = None,
    ):
        """Provides all of the Tests for the provided Team Id, optionally filtered by test last modified date/time. Tests are ordered in descending order, by Record Time. Dates should be specified as UTC in the ISO8601 format e.g yyyy-mm-ddThh:mm:ssZ This endpoint is paged.

        Args:
            team_id (str): The ID of the team. Defaults to 'a9f999be-249f-466a-b98e-b70605adee6d'.
            page_number (int): The page number to request. Defaults to 1.
            modified_from (str): The datetime to start filter results with. Defaults to None.
        """
        if modified_from:
            return self._make_request(
                "GET",
                f"/teams/{team_id}/tests/{page_number}",
                parameters={"modifiedFrom": modified_from},
            )
        else:
            return self._make_request("GET", f"/teams/{team_id}/tests/{page_number}")


if __name__ == "__main__":
    v = ValdForceDecksAPI("Vw3OPqaSdBCe5UkA==", "aeSwC1V9VxyAZuD4D4vyFG6zchcSzYEgA=")
    pprint(v.get_team_tests(modified_from="2022-07-08T00:00:00"))
