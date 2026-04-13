"""Environment configuration for API Test Automation Framework."""

import os

class Config:
    """Base configuration."""
    BASE_URL = os.getenv('BASE_URL', 'https://jsonplaceholder.typicode.com')
    DEBUG = False
    TIMEOUT = 10
    VERIFY_SSL = True


class DevelopmentConfig(Config):
    """Development environment configuration."""
    BASE_URL = os.getenv('BASE_URL', 'https://jsonplaceholder.typicode.com')
    DEBUG = True
    TIMEOUT = 15
    VERIFY_SSL = True
    LOG_LEVEL = 'DEBUG'


class StagingConfig(Config):
    """Staging environment configuration."""
    BASE_URL = os.getenv('BASE_URL', 'https://api-staging.example.com')
    DEBUG = False
    TIMEOUT = 10
    VERIFY_SSL = True
    LOG_LEVEL = 'INFO'


class ProductionConfig(Config):
    """Production environment configuration."""
    BASE_URL = os.getenv('BASE_URL', 'https://api.example.com')
    DEBUG = False
    TIMEOUT = 5
    VERIFY_SSL = True
    LOG_LEVEL = 'WARNING'


def get_config():
    """Get configuration based on environment variable."""
    env = os.getenv('ENV', 'dev').lower()
    
    config_map = {
        'dev': DevelopmentConfig,
        'development': DevelopmentConfig,
        'staging': StagingConfig,
        'prod': ProductionConfig,
        'production': ProductionConfig,
    }
    
    return config_map.get(env, DevelopmentConfig)()
