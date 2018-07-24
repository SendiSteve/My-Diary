import os

"""
    This file contains the different settings depending on the
    application environment.
"""


class ConfigBase(object):
    """Settings common to all configurations"""
    SECRETE_KEY = os.urandom(24)
    DEBUG = False
    TESTING = False


class ProductionConfig(ConfigBase):
    """Production configurations"""
    DEBUG = False  # should be set to false always


class DevelopmentConfig(ConfigBase):
    """Development configurations"""
    DEBUG = True


class TestingConfig(ConfigBase):
    """Testing configurations"""
    DEBUG = True


app_config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
