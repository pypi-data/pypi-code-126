from decouple import config
import pytest

from twitter_threader.threader import Thread, connect_api

consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
access_token_key = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')

username = config('TWITTER_USERNAME')
username_id = config('TWITTER_USERNAME_ID')
tweet_text_id = '266367358078169089'
tweet_text = 'RT @TwitterEng: Bolstering our infrastructure. "As  usage patterns change, Twitter can remain resilient." http://t.co/uML86B6s'

api = connect_api(consumer_key, consumer_secret, access_token_key, access_token_secret)
threader = Thread(api)


@pytest.mark.vcr
def test_connect_api():
    api = connect_api(consumer_key, consumer_secret, access_token_key, access_token_secret)
    assert str(api.me().id) == username_id


@pytest.mark.vcr
def test_get_thread():
    tweet = threader.get_thread(tweet_text_id)
    assert tweet == [tweet_text]


@pytest.mark.vcr
def test_convert_to_post():
    post = threader.convert_to_post(tweet_text_id)
    assert post == tweet_text


@pytest.mark.vcr
def test_post_thread():
    response = threader.post_thread('Lorem ipsum dolor sit amet,', username=username)
    assert response is None
