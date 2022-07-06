import os

from spt_factory import MongoFactory


if __name__ == '__main__':
    f = MongoFactory(
        mongo_url=os.getenv('MONGO_URL'),
        tlsCAFile=os.getenv('SSLROOT'),
    )

    print(f'moniback-telegram = {f.get_any_creds_credentials(type="moniback-telegram")}')
    print(f'moniback-mlg = {f.get_any_creds_credentials(type="moniback-mlg")}')
    print(f'postgres = {f.get_postgres_credentials()}')


    print(f.get_postgres_credentials(**{
        'host': 'localhost',
        'port': '5432',
        'dbname': 'moniback'
    }))

    with f.get_postgres(dbname='moniback') as conn:
        print("Happy coding")