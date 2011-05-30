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
    
    def __init__(self):
        
        # This represents members that don't have profiles in
        #   this group
        self.unreconciled_members = []

        # Members that are reconciled
        self.reconciled_members = []
        

    
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

    def get_events(self):
        """
        Get a blob of events data and return a recurisve DictObject of the same.
        """
        url = settings.BASE_URL + 'events.json'

        return self.make_request(url, request_data=REQUEST_DATA)
        
    def reconcile_members_profiles(self):
        """ profile values are given precedence over member values"""
        
        # resetting these values
        self.unreconciled_members = []
        self.reconciled_members = []

        # Create dict of profiles for fast searching
        profiles = {}
        for p in self.get_profiles():
            profiles[int(p.member_id)] = p

        # loop through the group members
        for member in self.get_members():

            # get the profile from the profiles dict
            profile = profiles.get(member.id, None)

            # If no profile available, add them to unreconciled
            if not profile:
                self.unreconciled_members.append(profile)
                continue

            # loop through the reconcile fields
            for field in settings.RECONCILE_FIELDS:
                value = getattr(profile, field, "")
                setattr(member, field, value)

            self.reconciled_members.append(member)

        return self.reconciled_members

if __name__ == "__main__":
    m = Meetup()
    print m.get_members()[0].bio
    print len(m.get_profiles())
