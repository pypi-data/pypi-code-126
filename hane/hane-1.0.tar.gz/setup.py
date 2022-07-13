from distutils.core import  setup
version = '1.1'
setup(name='hane',
      version='1.0',
      description='mHapTk is a tool kit for analysis of DNA methylation haplotypes. It has 5 sub-commands: tanghulu, stat, genomeWide, R2 and MHBDiscovery',
      author='ckw',
      author_email='1353595807@qq.com',

      packages=['mhaptk','console'],
      # entry_points={
      #       'console_scripts': [
      #             'shangchuan = console.mhap_console:main'
      #       ]
      # }

      )

