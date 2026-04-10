from setuptools import setup
setup(
    name="py-exchange-rates",
    version="1.0.0",
    py_modules=["exchange_rates", "_cache"],
    install_requires=["requests"],
)
