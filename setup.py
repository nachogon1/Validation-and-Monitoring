from setuptools import setup

setup(
    name="app",
    version="0.0.1",
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "event-tools = scripts.event_tools:main",
        ],
    },
)
