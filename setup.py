from setuptools import setup

setup(
    name='df-compress',
    version='0.1.0',    
    description="A python package to compress pandas DataFrames akin to Stata's `compress` command",
    url='https://github.com/phchavesmaia/df-compress',
    author='Pedro H. Chaves Maia',
    author_email='pedro.maia@imdsbrasil.org',
    license='MIT',
<<<<<<< HEAD
    packages=['df_compress'],
=======
    packages=['df-compress'],
>>>>>>> cf9aba9bb7b86f77ce3b68f9b9d11ccbfa4bba7d
    install_requires=['pandas',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.13',
    ],
)
