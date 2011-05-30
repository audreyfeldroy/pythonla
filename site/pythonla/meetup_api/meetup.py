# -*- coding: utf-8 -*-

import json
import requests

import utils
import settings

REQUEST_DATA = dict(
    group_urlname=settings.GROUP_NAME,
    key=settings.API_KEY,
)

# Exports
__all__ = ('Meetup', 'NotJSONContent',)


# Exceptions
class NotJSONContent(Exception):
    pass


# Classes
class Meetup(object):
    
    def make_request(self, url, request_data):
        """
        Boilerplate request fetcher that returns the "results" attribute from the API
        """
        r = requests.get(url, request_data)
        if r.status_code == 200:
            try:
                data = json.loads(r.content)
            except ValueError:
                raise NotJSONContent(r.content)
            obj = utils.recursive_dictobject(data)
        else:
            # TODO change to custom exception
            # TODO pass in proper message
            raise Exception()
        return obj.results        

    def get_members(self):
        """
        Get a blob of member data and return a recurisve DictObject of the
        same.
        """
        url = settings.BASE_URL + 'members.json'
        
        return self.make_request(url, request_data=REQUEST_DATA)
    
    def get_profiles(self):
        """
        Get a blob of profiles data and return a recurisve DictObject of the
        same.
        """
        url = settings.BASE_URL + '2/profiles.json'
            
        return self.make_request(url, request_data=REQUEST_DATA)            

    def get_events():
        """
        Get a blob of events data and return a recurisve DictObject of the same.
        """
        url = settings.BASE_URL + 'events.json'

        return self.make_request(url, request_data=REQUEST_DATA)


if __name__ == "__main__":
    m = Meetup()
    print m.get_members()[0].bio
    print len(m.get_profiles())
