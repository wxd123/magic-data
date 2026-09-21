# src/magic_vedio/video/models/storyboards.py
"""分镜表实体 - 只定义字段"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from magic_base import MagicBaseEntity
from magic_vedio.constants.constants import STORYBOARD_TABLE


class Storyboard(MagicBaseEntity):
    """
    分镜表实体 - 只负责数据映射
    业务逻辑在 Service 层实现
    """
    __tablename__ = STORYBOARD_TABLE
    

    # ==================== 基本信息 ====================
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    version = Column(String(50), default="1.0")
    description = Column(Text, nullable=True)
    author = Column(String(100), nullable=True)  

    

    # ==================== 关系 ====================
    # shots = relationship(
    #     "Shot",
    #     back_populates="storyboard",
    #     cascade="all, delete-orphan",
    #     lazy="select",
    #     order_by="Shot.order_index"
    # )