from os import path


def get_query_string(file_path):
    with open(path.join(file_path), 'r', encoding='utf-8') as file:
        return file.read()


def make_query(context, query: str, variables: dict = None, file_path=None):
    if file_path is not None:
        query = get_query_string(file_path)

    if variables is None:
        variables = {}
    if hasattr(context, 'session'):
        return context.request.post(
            url=context.env_data['gql_url'],
            data={'query': query, 'variables': variables}

        )
    else:
        return context.session.post(
            context.env_data['gql_url'],
            json={
                'query': query,
                'variables': variables
            }
        )
