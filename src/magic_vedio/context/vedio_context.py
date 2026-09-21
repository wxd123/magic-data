# shared/context.py
from magic_base.context.application_context import ApplicationContext
from magic_base import  MagicDatabaseConfig, MagicDatabaseManager
from ..constants import PROJECT_CODE
# 各模块的类定义



class MagicVedioContext():

    _project_name = PROJECT_CODE
    
    @classmethod
    def init_context(cls, db_config=None, db_manager=None):        

        if db_config is None:
            db_config = MagicDatabaseConfig()
        if db_manager is None:
            db_manager = MagicDatabaseManager(db_config)
        ApplicationContext.initialize(cls._project_name,db_config, db_manager)
    
    