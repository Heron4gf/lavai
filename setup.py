from setuptools import setup, find_packages

# Read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="lavai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'click>=8.0.0',
        'openai>=0.27.0'
    ],
    entry_points={
        'console_scripts': [
            'lavai=lavai.cli:main',
        ],
    },
    python_requires='>=3.7',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Heron4gf',
    author_email='heron@giambuzzi.it',
    description='A Python library for securely storing API keys for various AI providers locally and providing a unified client interface to interact with them.',
    license='MIT',
    keywords='ai openai api key management',
    url='https://github.com/lavai/lavai',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
