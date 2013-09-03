python-qredisqueue
==================

Simple redis-based queue.

[source](http://peter-hoffmann.com/2012/python-simple-queue-redis-queue.html)

Usage
-----

```python
from qredisqueue import RedisQueue
q = RedisQueue('test')
q.put('hello world')
```

```python
from qredisqueue import RedisQueue
q = RedisQueue('test')
q.get() # 'hello world'
```
