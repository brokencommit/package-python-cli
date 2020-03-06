from setuptools import setup

setup(name='package-python-cli',
      version='practice',
      description='test making cli python script',
      author='Broken Commit',
      github='brokencommit',
      packages=['important'],
      entry_points={
          'console_scripts': ['fudo=important.test:main'], # fudo is our cli key word
      },
      include_package_data=True,
)