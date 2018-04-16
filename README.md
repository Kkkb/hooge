# hooge

Flask web development

Focus on Flask ``source`` code

## A simple example
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"
```

从 flask 包中导入 Flask 类，创建一个名为 `app` 的 [Flask](https://github.com/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L68)对象

`app` 的 `route` 的装饰器作用于 `index` 函数，从而保存了 URL 与 Python 函数的映射关系

像 **index** 这样的函数称为视图函数（view function），它保存在实例 `app` 的名为 [`view_functions`](https://github.com/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L399)字典中，其键为 endpoint ，值为 view function ，而 URL 则以列表形式保存在 [`url_map`](https://github.com/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L1214) 对象中，这个列表的值是 [`Rule`](https://github.com/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L1211) 类的对象
