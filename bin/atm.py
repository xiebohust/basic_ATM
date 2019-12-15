#!/usr/bin/env python3
import os
import sys

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)
print(BaseDir)
print(sys.path)


# 添加完跟路径后，才能导入模块
from core import main



if __name__ == "__main__":
    main.main()