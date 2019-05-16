# NER项目功能

识别文本中的实体

# 环境配置

python3.5以上
tensorflow-gpu1.4以上

# 使用方法
## 语料标注
采用BIO的标注方式，如下所示：
```
中	B-LOC
国	I-LOC
很	O
大	O
句	O
子	O
结	O
束	O
是	O
空	O
行	O
```

## How to run
### train
```
python3 main.py --mode=train
```

### test
```
python3 main.py --mode=test
```

### demo
```
python main.py --mode=demo --demo_model=1557817923
```
1557817923是存放训练得到的模型的文件夹

可根据需求在main.py中修改相应代码

# 注意事项
若报错可在运行代码之前，输入下面的命令
```
LD_LIBRARY_PATH="/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/cuda-9.0/lib64:/usr/local/cuda-9.0/extras/CUPTI/lib64"
```
