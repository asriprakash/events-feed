class Base():
    DEBUG = False
    TESTING = False
    BUCKET = "events-feed-deloitte"
    PROJECT = "events-feed-deloitte"


class DevelopmentConfig(Base):
    DEBUG = True
    DEVELOPMENT = True
    BUCKET = "events-feed-deloitte"
    PROJECT = "events-feed-deloitte"
    API = "http://localhost:8080"


class AppEngineConfig(Base):
    DEBUG = False
    TESTING = False
    BUCKET = "events-feed-deloitte"
    PROJECT = "events-feed-deloitte"
    API = "https://backend-dot-events-feed-deloitte.appspot.com/"


class KubernetesConfig(Base):
    DEBUG = False
    TESTING = False
    BUCKET = "events-feed-deloitte"
    PROJECT = "events-feed-deloitte"
    API = "http://hip-local-api-svc:8085"