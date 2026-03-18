from setuptools import setup, find_packages

setup(
    name="personal_assistant",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],  # Тут можна вказати залежності, якщо вони з'являться
    entry_points={
        'console_scripts': [
            'assistant=main:main',  # Команда 'assistant' буде запускати функцію main у main.py
        ],
    },
)