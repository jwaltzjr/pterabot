from collections import defaultdict

import requests

from config import config

class Stream(object):

    API_URL = 'https://api.twitch.tv/helix/streams?'
    CLIENT_ID = config['TWITCH_API_KEY']

    def __init__(self, user):
        self.user = user
        self.refresh_stream_data()

    def refresh_stream_data(self):
        response = requests.get(
            self.API_URL,
            headers={'Client-ID': self.CLIENT_ID},
            params={'user_login': self.user}
        )
        try:
            self.stream_data = defaultdict(int, response.json()['data'][0])
        except IndexError:
            self.stream_data = defaultdict(int)

    @property
    def title(self):
        return self.stream_data['title']

    @property
    def viewers(self):
        return self.stream_data['viewer_count']

    @property
    def stream_start(self):
        return self.stream_data['started_at']

    @property
    def thumbnail(self, width=1280, height=720):
        raw_thumbnail_url = self.stream_data['thumbnail_url']
        sized_thumbnail_url = raw_thumbnail_url.replace('{width}', str(width)).replace('{height}', str(height))
        return sized_thumbnail_url

    @property
    def is_live(self):
        self.refresh_stream_data()
        if self.stream_data['type'] == 'live':
            return True
        else:
            return False
