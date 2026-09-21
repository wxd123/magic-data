
# magic_model/data_access/services/cpu_service
from magic_base.data_access.service.base_service import BaseService
from ..repositorys import StoryboardRepository
from ..models import  Storyboard


class StoryboardService(BaseService[Storyboard]):
    def __init__(self):
        super().__init__(StoryboardRepository())


storyboard_serivce: StoryboardService = StoryboardService()