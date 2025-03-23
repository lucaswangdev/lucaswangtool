```python tests/test_core.py（添加路径处理）
import sys
import os
# 关键路径处理：将项目根目录加入Python路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lucaswangtool.core import MathOperations, MathError
```

```text 项目结构验证
正确结构：
your_project/
├── lucaswangtool/
│   ├── __init__.py
│   └── core.py
└── tests/
    └── test_core.py

错误结构：
your_project/
└── tests/
    ├── lucaswangtool/  # 错误！模块目录不应在tests内
    │   └── core.py
    └── test_core.py
```

**本地模块加载解决方案**：

1. **临时路径修正（推荐快速调试）**：
```python
# 在测试文件顶部添加（需import sys和os）
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)
```

2. **开发模式安装（长期解决方案）**：
```bash
# 项目根目录执行（需pyproject.toml或setup.py）
pip install -e .
```

3. **命令行指定路径**：
```bash
# 在项目根目录执行
PYTHONPATH=. python tests/test_core.py
```

4. **创建最小化setup.py（若无构建配置）**：
```python setup.py
from setuptools import setup

setup(
    name="lucaswangtool",
    version="0.1",
    packages=["lucaswangtool"],
)
```

**验证方法**：
```python tests/validate_import.py
# 新建验证文件
try:
    from lucaswangtool.core import MathOperations
    print("✅ 模块导入成功")
except ImportError as e:
    print(f"❌ 导入失败: {e}")
```