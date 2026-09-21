# src/magic_vedio/video/models/shot.py
"""镜头实体 - 只定义字段"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey, Index

from magic_base import MagicBaseEntity
from magic_vedio.constants.constants import SHOT_TABLE


class Shot(MagicBaseEntity):
    """
    镜头实体 - 只负责数据映射
    业务逻辑在 Service 层实现
    """
    __tablename__ = SHOT_TABLE
    __table_args__ = (
        Index("idx_shot_storyboard_id", "storyboard_id"),           
    )

    # ==================== 关联 ====================
    id = Column(Integer, primary_key=True, autoincrement=True)
    storyboard_id = Column(Integer, nullable=False)

    # ==================== 基本信息 ====================
    scene_code = Column(String(50), nullable=False)
    time_range = Column(String(100), nullable=True)
    shot_type = Column(String(50), nullable=True)
    content = Column(Text, nullable=True)

    # ==================== 脚本信息 ====================
    dialogue = Column(Text, nullable=True)
    sound_effect = Column(String(500), nullable=True)

    # ==================== 生成参数 ====================
    gen_method = Column(String(50), nullable=False, default="后期制作")
    width = Column(Integer, default=1280)
    height = Column(Integer, default=736)
    prompt = Column(Text, nullable=True)
    duration = Column(Float, default=5.0)
    fps = Column(Integer, default=24)

    # ==================== 执行状态 ====================
    status = Column(String(50), default="pending")
    result = Column(Text, nullable=True)
    error = Column(Text, nullable=True)
    retry_count = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)

    # ==================== 输出信息 ====================
    output_file = Column(String(500), nullable=True)
    output_filename = Column(String(255), nullable=True)
    file_size = Column(Integer, nullable=True)
    thumbnail = Column(String(500), nullable=True)
    duration_actual = Column(Float, nullable=True)

    # ==================== 元数据 ====================
    notes = Column(Text, nullable=True)
    tags = Column(Text, nullable=True)
    order_index = Column(Integer, nullable=False, default=0)

    # ==================== 时间戳 ====================    
    executed_at = Column(DateTime, nullable=True)

    # ==================== 关系 ====================
    # storyboard = relationship("Storyboard", back_populates="shots")