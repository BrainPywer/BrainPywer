"""
BrainPywer Gateway
testing implementation
"""
import urllib3
import certifi
from json import loads
from sys import version_info
from . import __version__ as brainpowerversion


class HttpClient:
    """
    HttpClient Class for things
    """

    BASE_URL = "https://discordapp.com"
    API_BASE = BASE_URL + '/api/v6'
    GATEWAY  = API_BASE + '/gateway/bot'
    USERS    = API_BASE + '/users'
    CHANNELS = API_BASE + '/channels'
    GUILDS   = API_BASE + '/guilds'

    def __init__(self, token: str):
        """

        :param token: Your bot token
        :type token: str
        """
        self.token = token

        agent = 'DiscordBot (https://github.com/BrainPywer/BrainPywer/ v{0}) urllib3/{1} Python/{2[0]}.{2[1]}.{2[2]}'
        self.user_agent = {'user-agent': agent.format(brainpowerversion, urllib3.__version__, version_info) }
        self.pool = urllib3.PoolManager(10, headers=self.user_agent, timeout=1, cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    def __get(self, url):
        """
        Internal function for urllib3 get requests.

        :param url: url to 'GET'
        :type url: str
        :return: decoded data from requested url
        :rtype: str
        :raises: IOError
        """
        try:
            r = self.pool.request(method='GET', url=url, redirect=False)
        except MaxRetryError as e:
            raise IOError('whoops: {}'.format(e))  # Raise some kind of error here
            pass
        else:
            if r.status == 200:
                return r.data.decode()
            else:
                raise IOError('whoops: {}'.format(r.status))  # Raise some other error here

    def __put(self, url, data):
        """
        Internal function for urllib3 put requests.

        :param url: url to 'PUT' at
        :type url: str
        :param data: data to put
        :type data: python dict
        :return:
        """
        try:
            r = self.pool.urlopen(method='PUT', url=url, fields=data, redirect=False)
        except MaxRetryError as e:
            raise IOError('whoops: {}'.format(e))  # Raise some kind of error here
            pass
        else:
            if r.status == 200:
                return r.data.decode()
            else:
                raise IOError('whoops: {}'.format(r.status))  # Raise some other error here

    def get_gateway(self):
        """
        Return the wss url to connect to.

        :return: wss url
        :rtype: str
        """
        gate = loads(self.__get(GATEWAY))
        return gate['url'] + '?encoding=json&v=6' #will be etf

    def get_channel(self, channel: str):
        """
        Get a channel by ID. Returns a guild channel or dm channel object.

        :param channel: channel id to get
        :type channel: str
        :return:
        """
        url = CHANNELS + '/' + channel
        chan = loads(self.__get(url=url))
        return chan

    def mod_channel(self, channel: str, *args):
        """

        :param channel:
        :param args:
        :return:
        """
        raise NotImplemented

    def del_channel(self, channel: str):
        """

        :param channel:
        :return:
        """
        raise NotImplemented

    def get_channel_message(self, channel: str, message: str):
        """

        :param channel:
        :param message:
        :return:
        """
        raise NotImplemented

    def get_channel_messages(self, channel: str):
        """

        :param channel:
        :return:
        """
        raise NotImplemented

    def send_message(self, channel: str, content: str, tts: bool = False):
        """

        :param channel:
        :param content:
        :param tts:
        :return:
        """
        raise NotImplemented

    def edit_message(self, channel: str, message: str):
        """

        :param channel:
        :param message:
        :return:
        """
        raise NotImplemented

    def send_file(self, channel: str, content: str, file: str, tts: bool = False):
        """

        :param channel:
        :param content:
        :param file:
        :param tts:
        :return:
        """
        raise NotImplemented

    def delete_message(self, channel: str, message: str):
        """

        :param channel:
        :param message:
        :return:
        """
        raise NotImplemented
