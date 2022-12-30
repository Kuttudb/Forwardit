#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 8281168))
    API_HASH = os.environ.get("API_HASH", "445ff67ec34858448ac184c7479ce917")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2055718473:AAHGch-ioqCoYkzTkMtw0SDG1UkYK91IQWc") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", 1011394081)
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", -1001696546419))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
