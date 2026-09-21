# coder/data_access/repository/task_repo.py

"""
Magic Vedio Storyboard Repository

为 Magic Vedio Storyboard 模块提供数据访问层实现。
"""

from magic_base.data_access.repository.base_repository import MagicBaseRepository

from ..models import Storyboard


class StoryboardRepository(MagicBaseRepository[Storyboard]):
    """
    任务数据仓库
    """
    pass