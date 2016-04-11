# -*- coding: utf-8 -*-
#__author__ = 'daniel'
#__email__ = 'daniel_001@126.com'

import logging

from user_agent import generate_user_agent



class RandomUserAgentMiddleware(object):

    def __init__(self,settings):
        super(RandomUserAgentMiddleware, self).__init__()

        self.platform= settings['USERAGENT_PLATFORM']


    @classmethod
    def from_crawler(cls, crawler):
        obj = cls(crawler.settings)
        return obj




    def process_request(self, request, spider):
        user_agent = generate_user_agent(platform=self.platform)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)