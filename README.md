# lucaswangtool

This is a demonstration math operations library.

## How to use
```bash
pip install lucaswangtool
```

```python
from lucaswangtool.core import MathOperations

myInstance = MathOperations()
result = myInstance.add(1,2)
print(result)
```

# 在项目根目录执行
python -m venv .venv  # 创建名为 .venv 的虚拟环境

# Linux/macOS
source .venv/bin/activate

pip install build

pip install -e .  # 会自动读取 setup.py/setup.cfg 的配置

# Windows
.\.venv\Scripts\activate

# 打包
rm -rf dist/ build/ 
python -m build
twine check dist/* 
# 上传到 PyPI（使用默认配置）
twine upload dist/*   

