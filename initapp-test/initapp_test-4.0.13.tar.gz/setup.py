from setuptools import setup, find_packages

setup(
    name='initapp_test',
    version='4.0.13',
    include_package_data=True,
    packages=['initcost_conf', 'util','match_cost','.'],
    install_requires=[
        'numpy',
        'ffmpeg_python==0.2.0',
        'opencv_python',
        'openpyxl',
        'pandas',
        'xlrd',
        'pytesseract==0.3.8',
        'ffmpeg==1.4',
        'PyYAML',
    ],
    #packages= find_packages(),
    url='',
    license='',
    author='wangkejun',
    author_email='446093036@qq.com',
    description='initapp_test'
)
# scp -i pbox_id_rsa_kuaishou -P 41022 hs@117.54.227.102:/home/hs/pboxData/2022-07-05/RedmiNote8Pro/pro/pro1.mp4 /Users/wangkejun
# ssh -i pbox_id_rsa_kuaishou  hs@kuaishou-id-jkt-0.headspin.io -p 41022