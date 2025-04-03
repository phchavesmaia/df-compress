from setuptools import setup

setup(
    name='pycompress',
    version='0.1.0',    
    description="A python package to compress pandas DataFrames akin to Stata's `compress` command",
    url='https://github.com/phchavesmaia/pycompress',
    author='Pedro H. Chaves Maia',
    author_email='pedro.maia@imdsbrasil.org',
    license='MIT',
    packages=['pycompress'],
    install_requires=['pandas',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.13',
    ],
)
