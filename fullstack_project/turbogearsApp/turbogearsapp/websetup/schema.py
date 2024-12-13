from turbogearsapp.model import metadata

def setup_schema(command, conf, vars):
    """
    Place any commands to setup your application's schema here.
    """
    print("Creating tables")
    metadata.create_all(bind=conf['tg.app_globals'].sa_engine)
