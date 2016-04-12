# -*- coding: utf-8 -*-

# python imports
from urllib import parse
import requests as rq
import simplejson as json

# django imports
from django.conf import settings

# fb docs, tools
# https://developers.facebook.com/tools/explorer
# https://developers.facebook.com/docs/apps/changelog#v2_5
# https://developers.facebook.com/docs/graph-api/reference/v2.5/user
# https://developers.facebook.com/docs/facebook-login/permissions
# https://developers.facebook.com/docs/facebook-login/reauthentication
# https://developers.facebook.com/docs/facebook-login/access-tokens

class FacebookAuth(object):
    access_token = None
    perm_request_url = None

    def __init__(self, client_id, client_secret, scope=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorize_url = settings.AUTHORIZE_URL
        self.access_token_url = settings.ACCESS_TOKEN_URL
        self.api_url = settings.API_URL
        self.request_perms_url = settings.REQUEST_PERMISSIONS_URL
        self.graph_me_url = settings.GRAPH_ME_URL
        self.callback_url = settings.CALLBACK_URL
        self.scope_list = settings.FACEBOOK_SCOPE

    def _urlencode(self,params={}):
        if not isinstance(params, dict): 
            raise Exception("You must pass in a dictionary!")
        params_list = []
        for k,v in params.items():
            if isinstance(v, list):
                params_list.extend([(k, x) for x in v])
            else:
                params_list.append((k, v))
        return parse.urlencode(params_list)

    def _authorize_url(self):
        _kvp_hash = {'redirect_uri': self.callback_url,
                        'client_id': self.client_id,
                        'scopes': self.scope_list}
        params = self._urlencode(_kvp_hash)
        return self.authorize_url + '?' + params

    def _access_token(self, code):
        _kvp_hash = {'code': code,
                        'redirect_uri': self.callback_url,
                        'client_secret': self.client_secret,
                        'client_id': self.client_id}
        params = parse.urlencode(_kvp_hash)
        response = rq.get(self.access_token_url + '?' + params)
        if response.status_code != 200:
            raise (Exception('Invalid response,response code: {e}'.format(e=response.status_code)))

        response_array = str(response.text).split('&')
        self.access_token = str(response_array[0][13:])

    def _user_info(self):
        response = rq.get("{u}?fields=id,email,first_name,last_name,birthday,gender,picture&access_token={at}"\
                                .format(u=self.graph_me_url,at=self.access_token))
        if response.status_code != 200:
            raise (Exception('Invalid response,response code: {e}'.format(e=response.status_code)))

        return response.json()

    def _user_likes(self):
        if not self.check_perms('user_likes'):
            requestedPermissionUrl = self.request_perms('user_likes')

        response = rq.get(self.api_url + 'me/likes?access_token={at}'.format(at=self.access_token))
        return response.json()['data']

    def check_perms(self, perm):
        permDict = {'status': 'granted', 'permission': perm}
        response = rq.get(self.api_url + 'me/permissions?access_token={at}'.format(at=self.access_token))
        if response.status_code != 200:
            raise (Exception('Invalid response,response code: {e}'.format(e=response.status_code)))

        currPerms = response.json()['data']
        if permDict in currPerms:
            return True
        return False

    def request_perms(self, perm):
        _kvp_hash = {'client_id': self.client_id,
                        'redirect_uri': self.callback_url,
                        'auth_type': 'rerequest',
                        'scope': perm,
                        'access_token': self.access_token}
        params = parse.urlencode(_kvp_hash)
        self.perm_request_url = self.request_perms_url + '?' + params
