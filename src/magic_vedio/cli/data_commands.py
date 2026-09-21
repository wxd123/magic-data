#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magic_model/cli/data_commands.py

import csv
from pathlib import Path
import sys
import traceback
from typing import Dict, Any, Optional, Callable
from datetime import datetime, date

sys.path.insert(0, str(Path(__file__).parent.parent))
from magic_vedio.vedio.data_access.models import Storyboard, Shot
from magic_vedio.vedio.data_access.repositorys import StoryboardRepository, ShotRepository
from magic_vedio.context import MagicVedioContext
from magic_base.data_access.util.base_data_command import BaseDataImportCommand

class DataCommand(BaseDataImportCommand):
    """数据导入器"""
    
    def __init__(self, data_dir: Optional[Path] = None):
        """初始化导入器"""
        if data_dir is None:
            data_dir = Path(__file__).parent.parent.parent.parent / "data"
        self.data_dir = Path(data_dir)
        self.stats = {}

        # 初始化数据库连接
        MagicVedioContext.init_context()
    
    def import_all(self) -> bool:
        """导入所有数据"""
        importers = [
            ("Storyboard", self.import_storyboard),
            ("Shot", self.import_shot),
            
            
        ]
        
        print("=" * 60)
        print("Starting data import...")
        print("=" * 60)
        
        success_count = 0
        for i, (name, importer) in enumerate(importers, 1):
            print(f"\n[{i}/{len(importers)}] Importing {name}...")
            print("-" * 40)
            try:
                if importer():
                    success_count += 1
            except Exception as e:
                print(f"✗ Failed to import {name}: {e}")
                traceback.print_exc()
        
        print("\n" + "=" * 60)
        print(f"Import completed: {success_count}/{len(importers)} succeeded")
        print("=" * 60)
        
        return success_count == len(importers)
    
    # ========== 辅助方法 ==========
    
    
    # ========== 具体导入方法 ==========
    
    def import_storyboard(self) -> bool:
        """导入分镜表数据"""
        storyboard = []
        
        def process_row(row):
            
                _storyboard_data = {
                    'name': row['name'],
                    'full_name':row['full_name'],
                    'website': row.get('website') or None
                }
                return _storyboard_data
            
        
        is_success, results = self._import_csv_batch("storyboards.csv", process_row)
        if results :
            storyboard_repo = StoryboardRepository()
            storyboard_repo.batch_create_from_dict(results)
            print(f"✓ Batch created {len(results)} vendors")
        return is_success
    
    def import_shot(self) -> bool:
        """导入厂商数据"""
        shots = []
        
        def provider_row(row):
            
            _shot_data = {
                'name': row['name'],
                'code': row['code'],
                'version': row['version'],
                'description': row.get('description') or None,
                'api_type': row['api_type'],
                'base_url': row['base_url'],
                'api_key_required': bool(row['api_key_required']) if row.get('api_key_required') else False,
                'api_key_placeholder': row.get('api_key_placeholder') or '',
                'start_command': row.get('start_command') or None,
                'stop_command': row.get('stop_command') or None,
                'health_check_path': row['health_check_path'],
                'health_check_interval': int(row['health_check_interval']) if row.get('health_check_interval') else 30,
                'status': row.get('status') or 'stopped',
                'last_health_check': row.get('last_health_check') or None,
                'error_message': row.get('error_message') or None,
                'pid': int(row['pid']) if row.get('pid') and row['pid'] else None,
                'port': int(row['port']) if row.get('port') and row['port'] else None
            }
            return _shot_data
            
        
        is_success, results = self._import_csv_batch("providers.csv", provider_row)
        if results :
            shot_repo = ShotRepository()
            shot_repo.batch_create_from_dict(results)
            print(f"✓ Batch created {len(results)} providers")
        return is_success
    
    

def main():
    """命令行入口"""
    import argparse
    
    parser = argparse.ArgumentParser(description='数据导入工具')
    parser.add_argument('--data-dir', type=str, help='数据目录路径')
    parser.add_argument('--import-type', choices=['all', 'vendors', 'gpus', 'cpus'], 
                       default='all', help='导入类型')
    
    args = parser.parse_args()
    
    importer = DataCommand(data_dir=args.data_dir if args.data_dir else None)
    
    if args.import_type == 'all':
        success = importer.import_all()
    elif args.import_type == 'vendors':
        success = importer.import_vendors()
    elif args.import_type == 'gpus':
        success = importer.import_gpus()
    elif args.import_type == 'cpus':
        success = importer.import_cpus()
    else:
        success = False
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()