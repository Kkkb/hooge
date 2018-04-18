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

从 flask 包中导入 Flask 类，创建一个名为 `app` 的 [Flask](https://github.com/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L68) 对象

`app` 的 [`route`](https://github.com/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L1222) 的装饰器作用于 `index` 函数，从而保存了 URL 与 Python 函数的映射关系

这种关系是由装饰器封装的 [`add_url_rule`](https://github.com/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L1123) 方法实现的：

* 将 URL 和 `endpoint` 传入 `Rule` 类从而构造一个 `rule` 对象，将 `rule` 对象添加到 `Map` 类的对象 `url_map` 中
* 向 `view_functions` 字典中添加 `{endpoint: view_func}`

像 **index** 这样的函数称为视图函数（view function），它保存在实例 `app` 的名为 [`view_functions`](https://github.com/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L399)字典中，其键为 endpoint ，值为 view function ，而 URL 则以列表形式保存在 [`url_map`](https://github.com/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L1214) 对象中，这个列表的值是 [`Rule`](https://github.cm/pallets/flask/blob/3a0ea726bd45280de3eb3042784613a676f68200/flask/app.py#L1211) 类的对象


