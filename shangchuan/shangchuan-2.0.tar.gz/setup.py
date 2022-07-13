from distutils.core import  setup

setup(name='shangchuan',
      version='2.0',
      description='mHapTk is a tool kit for analysis of DNA methylation haplotypes. It has 5 sub-commands: tanghulu, stat, genomeWide, R2 and MHBDiscovery',
      author='ckw',
      author_email='1353595807@qq.com',

      packages=['shangchuan','mhaptkckw'],
      entry_points={
            'console_scripts': [
                  'shangchuan = mhaptkckw.mhap_console:main'
            ]
      }

      )

