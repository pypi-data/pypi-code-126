from setuptools import setup, find_packages
#MAO2116
setup(
    name='akxurl',
    packages=find_packages(),
    include_package_data=True,
    version="2.0.0",
    description='URL SHORTENER WITH PYTHON - 9 SERVER',
    author='AKXVAU',
    author_email='dev.akxvau@gmail.com',
    long_description=(open("README.md","r")).read(),
    long_description_content_type="text/markdown",
   install_requires=['lolcat','requests'],
 
    keywords=['hacker', 'spam', 'tool', 'sms', 'bomber', 'call', 'prank', 'termux', 'hack','sms bomber','sms bomber', 'AKXVAU', 'URL', 'URL SHORTNER', 'AKXURL'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    
    license='MIT',
    entry_points={
            'console_scripts': [
                'akxurl = akxurl.akxurl:menu',
                
            ],
    },
    python_requires='>=3.9'
)
