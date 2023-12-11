class Config:
    TESTING = False
    PYTHONDONTWRITEBYCODE = 1
    CSRF_ENABLED = 'this-really-needs-to-br-changed'


class ProductionConfig(Config):
    ENV = 'production'


class StagingConfig(Config):
    DEVELOPMENT = True
    ENV = 'staging'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    ENV = 'development'
