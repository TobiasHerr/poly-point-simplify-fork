from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='poly-point-simplify',
      version='0.0.1',
      description=u"Make small polygons into points",
      long_description=long_description,
      classifiers=[],
      keywords='geojson',
      author=u"Matthew Perry",
      author_email='perrygeo@gmail.com',
      url='https://github.com/perrygeo/poly-point-simplify',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click', 'cligj'
      ],
      entry_points="""
      [console_scripts]
      poly-point-simplify=poly_point_simplify.scripts.cli:main
      """
      )
