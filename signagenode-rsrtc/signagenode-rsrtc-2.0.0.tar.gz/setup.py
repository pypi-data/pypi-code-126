import setuptools

_requires = [
    'signagenode>=2.7.2',
    'setuptools-scm',
    'ebs-linuxnode-tables',
    'ebs-linuxnode-i18n',
]

setuptools.setup(
    name='signagenode-rsrtc',
    url='',
    use_scm_version=True,

    author='Chintalagiri Shashank',
    author_email='shashank.chintalagiri@gmail.com',

    description='',
    long_description='',

    packages=setuptools.find_packages(),
    package_data={'rsrtc': ['default/config.ini',
                            'default/background.png',
                            'resources/logo.png',
                            'resources/rsrtc-bg-blue.png',
                            'resources/rsrtc-bg-white.png',
                            'locale/*',
                            'locale/*/LC_MESSAGES/*']},

    install_requires=_requires,

    setup_requires=['setuptools_scm'],

    entry_points={
          'console_scripts': [
              'rsrtc = rsrtc.runnode:run_node'
          ]
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
    ],
    include_package_data=True,
    zip_safe=False,
)
