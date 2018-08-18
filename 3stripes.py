#!/usr/bin/python3
import uuid
import requests


class ThreeStripes:
    def __init__(self):
        self.session = requests.session()
        self.authorization_header = None
        self.api_root = 'https://api.3stripes.net/gw-api/v1'
        self.device_fingerprint = str(uuid.uuid4()).upper()
        self.client_id = str(uuid.uuid4())
        self.device_token = str(uuid.uuid4()).upper()
    
    def lookup_account(self, email):
        headers = {
            'Host':             'api.3stripes.net',
            'x-device-info':    f'app/adidas; os/iOS; os-version/10.2; app-version/2.0.1; buildnumber/944; type/iPhone6,1; fingerprint/{self.device_fingerprint}',
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'Accept':           'application/hal+json',
            'Accept-Language':  'en-US',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Accept-Encoding':  'gzip, deflate',
            'Connection':       'keep-alive'
        }
        return self.session.get(f'{self.api_root}/profile/lookup', params={'id':email}, headers=headers).json()

    def login(self, username_email, password):
        headers = {
            'Host':             'api.3stripes.net',
            'Accept':           'application/hal+json',
            'x-device-info':    f'app/adidas; os/iOS; os-version/10.2; app-version/2.0.1; buildnumber/944; type/iPhone6,1; fingerprint/{self.device_fingerprint}',
            'Accept-Language':  'en-US',
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'Accept-Encoding':  'gzip, deflate',
            'Content-Type':     'application/json; charset=UTF-8',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection':       'keep-alive'
        }
        payload = {
            "grant_type": "login",
            "password": password,
            "username": username_email
        }
        response = self.session.post(f'{self.api_root}/token', json=payload, headers=headers).json()
        self.authorization_header = f'{response["token_type"]} {response["access_token"]}'
        return response

    def get_account_stats(self):
        if self.authorization_header is None:
            print('Access token not found please login first')
            return
        headers = {
            'Host':             'srs.adidas.com',
            'Content-Type':     'application/json; charset=UTF-8',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection':       'keep-alive',
            'Accept':           'application/json',
            'Accept-Language':  'en-us',
            'Authorization':    self.authorization_header,
            'Accept-Encoding':  'gzip, deflate'
        }
        payload = {
            "countryOfSite": "US",
            "includeLoyaltyInformation": "Y",
            "includePersonalInformation": "Y",
            "includeSocialApplication": "Y",
            "loyaltyType": "GLOBAL",
            "source": "90901",
            "version": "13.0"
        }
        return self.session.post('https://srs.adidas.com/scvRESTServices/account/lookUpAccount', json=payload, headers=headers).json()


    def get_chat(self):
        headers = {
            'Host':             'api.3stripes.net',
            'x-device-info':    f'app/adidas; os/iOS; os-version/10.2; app-version/2.0.1; buildnumber/944; type/iPhone6,1; fingerprint/{self.device_fingerprint}',
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'Accept':           'application/hal+json',
            'Accept-Language':  'en-US',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Accept-Encoding':  'gzip, deflate',
            'Connection':       'keep-alive'
        }
        return self.session.post(f'{self.api_root}/chat/config', headers=headers).json()

    def get_server_time(self):
        headers = {
            'Host':             'api.3stripes.net',
            'Content-Type':     'application/json',
            'Connection':       'keep-alive',
            'x-devicetoken':    self.device_token,
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'x-clientid':       self.client_id,
            'Accept':           'application/json',
            'Accept-Language':  'en-us',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Accept-Encoding':  'gzip, deflate'
        }
        return self.session.post('https://api.3stripes.net/_manage/time', headers=headers).json()

    def get_location_products(self):
        headers = {
            'Host':             'api.3stripes.net',
            'x-device-info':    f'app/adidas; os/iOS; os-version/10.2; app-version/2.0.1; buildnumber/944; type/iPhone6,1; fingerprint/{self.device_fingerprint}',
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'Accept':           'application/hal+json',
            'Accept-Language':  'en-US',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Accept-Encoding':  'gzip, deflate',
            'Connection':       'keep-alive'
        }
        return self.session.get(f'{self.api_root}/products/location-based', headers=headers).json()

    def get_interests(self):
        headers = {
            'Host':             'api.3stripes.net',
            'x-device-info':    f'app/adidas; os/iOS; os-version/10.2; app-version/2.0.1; buildnumber/944; type/iPhone6,1; fingerprint/{self.device_fingerprint}',
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'Accept':           'application/hal+json',
            'Accept-Language':  'en-US',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Accept-Encoding':  'gzip, deflate',
            'Connection':       'keep-alive'
        }
        return self.session.get(f'{self.api_root}/interests', headers=headers).json()

    def get_basket(self):
        headers = {
            'Host':             'api.3stripes.net',
            'x-device-info':    f'app/adidas; os/iOS; os-version/10.2; app-version/2.0.1; buildnumber/944; type/iPhone6,1; fingerprint/{self.device_fingerprint}',
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'Accept':           'application/hal+json',
            'Accept-Language':  'en-US',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Accept-Encoding':  'gzip, deflate',
            'Connection':       'keep-alive'
        }
        return self.session.get(f'{self.api_root}/basket/info?', headers=headers).json()

    def get_navigation(self):
        headers = {
            'Host':             'api.3stripes.net',
            'x-device-info':    f'app/adidas; os/iOS; os-version/10.2; app-version/2.0.1; buildnumber/944; type/iPhone6,1; fingerprint/{self.device_fingerprint}',
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'Accept':           'application/hal+json',
            'Accept-Language':  'en-US',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Accept-Encoding':  'gzip, deflate',
            'Connection':       'keep-alive'
        }
        return self.session.get(f'{self.api_root}/navigation', headers=headers).json()

    def get_page_feed(self, page_number):
        headers = {
            'Host':             'api.3stripes.net',
            'x-device-info':    f'app/adidas; os/iOS; os-version/10.2; app-version/2.0.1; buildnumber/944; type/iPhone6,1; fingerprint/{self.device_fingerprint}',
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'Accept':           'application/hal+json',
            'Accept-Language':  'en-US',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Accept-Encoding':  'gzip, deflate',
            'Connection':       'keep-alive'
        }
        return self.session.get(f'{self.api_root}/feed', params={'page':page_number}, headers=headers).json()

    def get_product(self, product_id):
        headers = {
            'Host':             'api.3stripes.net',
            'x-device-info':    f'app/adidas; os/iOS; os-version/10.2; app-version/2.0.1; buildnumber/944; type/iPhone6,1; fingerprint/{self.device_fingerprint}',
            'x-api-key':        'm79qyapn2kbucuv96ednvh22',
            'Accept':           'application/hal+json',
            'Accept-Language':  'en-US',
            'User-Agent':       'adidas/944 CFNetwork/808.2.16 Darwin/16.3.0',
            'Accept-Encoding':  'gzip, deflate',
            'Connection':       'keep-alive'
        }
        return self.session.get(f'{self.api_root}/products', params={'product_id':product_id}, headers=headers).json()
