from distutils.core import setup

requirements = ['pyserial']

setup(name='lineproto',
      version='0.1.1',
      description='Python implementation of the LINE protocol',
      author='Marcsello',
      author_email='marcsello@sch.bme.hu',
      packages=['lineproto'],
      python_requires='>=3.10',
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Topic :: Communications',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.10'
      ],
      install_requires=requirements,
      setup_requires=requirements,
      tests_require=requirements,
      )
