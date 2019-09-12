import numpy as np
import pandas as pd
from datetime import datetime
from collections import Counter
from itertools import chain

import vk_api


class MyVKParser:
    '''This is a class for parsing the list of friends of a given VK user.
    Parses name, id, age, gender and university fields.
    Connection to VK is established by a simple login-password authentication via vk_api.
    '''


    def __init__(self, login, password):
        session = vk_api.VkApi(login, password)
        try:
            session.auth()
            self.__api = session.get_api()
        except vk_api.AuthError as auth_error:
            print("An error occurred: ", auth_error)
            self.__api = None
        
    def get_friends_info(self, user_id=None):
        '''Gets info that VK API returns via friends.get method with 
        "first_name", "last_name", "id", "bdate", "sex", and "universities" fields.
        '''

        if self.__api is not None:
            friends_info = self.__api.friends.get(user_id = user_id, fields = ['id', 'first_name', 'last_name',
                                                                               'bdate', 'sex', 'universities'])
            return friends_info
        else:
            return None
        
    @staticmethod
    def parse_ids(friends_info):
        '''Parses info that VK API returns via friends.get method. 
        Returns {name:id} dict for all friends.
        '''

        id_list = [a.get('id') for a in friends_info['items']]
        name_list = [a.get('first_name') + ' ' + a.get('last_name') for a in friends_info['items']]
        return dict(zip(name_list, id_list))
    
    @staticmethod
    def parse_genders(friends_info):
        '''Parses info that VK API returns via friends.get method. 
        Returns genders for all friends except where the "sex" field is None.
        '''
        gender_dict = {1: 'Female', 2: 'Male', 0: 'No info'}
        gender_list = [gender_dict.get(a.get('sex')) for a in friends_info['items']]
        return gender_list
    
    @staticmethod
    def parse_ages(friends_info):
        '''Parses info that VK API returns via friends.get method. 
        Returns ages for all friends except where the "bdate" field or year is None.
        '''
        
        bdate_list = [a.get('bdate') for a in friends_info['items']]
        year_list = [a.split('.')[-1] for a in bdate_list if a is not None and len(a)>=8]
        ages_list = [(datetime.now().year - int(a)) for a in year_list]
        return ages_list
    
    @staticmethod
    def parse_univers(friends_info):
        '''Parses info that VK API returns via friends.get method. 
        Returns universities for all friends except where the "universities" field is None.
        '''

        univer_soup = [a.get('universities') for a in friends_info['items']]
        univer_soup = list(chain.from_iterable([a for a in univer_soup if a is not None]))
        univer_list = [a.get('name') for a in univer_soup]
        return univer_list
    
    def get_friends_stats(self, friends_info=None, user_id=None):
        '''Returns dict with sex, bdate, and universities counters for a user.
        Parses friends_info or gets it by get_friends_info method and parses.
        '''
        
        if friends_info is None:
            friends_info = self.get_friends_info(user_id=user_id)
        if friends_info is not None:
            gender_counter = self.parse_genders(friends_info)
            age_counter = self.parse_ages(friends_info)
            univer_counter = self.parse_univers(friends_info)
            return {'gender': gender_counter, 'age': age_counter, 'univer': univer_counter}
        else:
            return None
        
if __name__ == '__main__':
    print(MyVKParser.__doc__)

