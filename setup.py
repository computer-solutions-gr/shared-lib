from setuptools import setup

setup(name='cssa_shared-lib',
      version='0.1',
      description='CSSA common libraries',
      url='https://github.com/computer-solutions-gr/shared-lib',
      author='Stavros Pitoglou',
      author_email='s.pitoglou@csl.gr',
      license='GNU',
      packages=['cssalib', 'projects'],
    #   test_suite='nose.collector',
    #   tests_require=['nose'],
      install_requires=[
          'requests',
          'loguru',
          'scikit-learn',
          'numpy',
          'matplotlib'
      ],
      zip_safe=False)