from setuptools import setup, Extension
setup(
    name="py-exchange-rates",
    version="1.0.1",
    py_modules=["exchange_rates"],
    ext_modules=[Extension("_cache", sources=["_cache.c"])],
    install_requires=["requests"],
    description="Exchange rate conversion utilities with native rate limiter",
)
