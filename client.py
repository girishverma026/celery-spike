from tasks import add, mul, build_insight
from celery import chain

res = (add.s(4, 4) | mul.s(4)).apply_async()
# build_insight.delay()

