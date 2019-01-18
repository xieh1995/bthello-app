#!/usr/bin/env python3
# encoding: utf-8

import os


class Config(object):

    ################入库程序配置###################
    #任务执行时间(秒)
    #STORAGE_TASK_TIME = 10
    ################redis配置##################
    # redis key
    REDIS_KEY = "infohash"
    # redis 地址
    REDIS_HOST = "39.108.218.149"
    # redis 端口
    REDIS_PORT = 6379
    # redis 密码
    REDIS_PASSWORD = None
    # redis 连接池最大连接量
    REDIS_MAX_CONNECTION = 20

    ################elasticsearch配置##################
    # elastics 地址
    ELASTICS_HOST = "39.108.218.149"
    # elastics 端口
    ELASTICS_PORT = 9200
    # elastics 密码
    ELASTICS_PASSWORD = None
    # elastics 连接池最大连接量
    ELASTICS_MAX_CONNECTION = 20