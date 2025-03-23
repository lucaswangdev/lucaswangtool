# 新建验证文件
try:
    from lucaswangtool.core import MathOperations
    print("✅ 模块导入成功")
except ImportError as e:
    print(f"❌ 导入失败: {e}")

