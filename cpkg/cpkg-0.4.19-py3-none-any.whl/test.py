import createPkg as c
c.create(
    path='./',
    dirName='xrew/',
    pkgName='xrew',
    description='.',
    url='https://github.com/seoul2k/xrew',
    project_urls={
        "Bug Tracker": "https://github.com/seoul2k/xrew/issues",
    },
    install_requires=[""],
    ismod=True,
    modPath='./index.cpgmod'
)

# c.CreateModule(
#     path='./index',
#     author='xiongts',
#     author_email='Mr_Xiongts@163.com',
#     classifiers=[
#         'Development Status :: 4 - Beta',
#         'Operating System :: OS Independent',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: BSD License',
#         'Programming Language :: Python :: 2.7',
#         'Programming Language :: Python :: Implementation',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.4',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.6',
#         'Programming Language :: Python :: 3.8',
#         'Topic :: Software Development :: Libraries'
#     ],
#     python_requires='>=2'
# )
