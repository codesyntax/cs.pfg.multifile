from setuptools import setup, find_packages
import os

version = '1.0.1'

setup(name='cs.pfg.multifile',
      version=version,
      description="PloneFormGen fields to allow uploading multiple files",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='https://github.com/codesyntax/cs.pfg.multifile',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cs', 'cs.pfg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.PloneFormGen'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
