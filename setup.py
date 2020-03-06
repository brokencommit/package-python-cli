from setuptools import setup

setup(name='package-python-cli',
      version='0.01',
      description='test making cli python script',
      author='Broken Commit',
      github='brokencommit',
      packages=['important'],
      entry_points={
          'console_scripts': ['fudo=important.test:main'], # "fudo" calls important/test.py => main()
      },
      include_package_data=True,
)