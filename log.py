#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
""" 
 @desc:  
 @author: dayinfinte
 @date: 2018/01/05
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49 
 """

import logging
from logging.config import fileConfig
from config import log_config_file


fileConfig(log_config_file)
logger = logging.getLogger()