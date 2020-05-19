from distutils.core import setup

setup(
    name='Corruption research',
    packages=['Corruption research'],
    version='0.1',
    description='Program for researching corruption in developing countries',
    author='Oleksandr Dubas',
    author_email='dubas@ucu.edu.ua',
    requires=[
        'matplotlib',
        'json',
        'urllib',
        'requests',
        'lxml',
        'numpy',
        'pandas',
        'geopandas',
        'shapely'
        'fiona',
        'GDAL',
        'pyproj',
        'six',
        'mapclassify'
    ],
    url='https://github.com/saniochky/research',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: Stable",
        "Topic :: Economics"
    ]
)
