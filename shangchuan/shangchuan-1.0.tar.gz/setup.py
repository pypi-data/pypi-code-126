from setuptools import setup,find_packages
version = '1.0'
setup(name='shangchuan',
      version='1.0',
      description='mHapTk is a tool kit for analysis of DNA methylation haplotypes. It has 5 sub-commands: tanghulu, stat, genomeWide, R2 and MHBDiscovery',
      author='ckw',
      author_email='1353595807@qq.com',

      packages=find_packages(),
      scripts=['bin/mhap_console']

      )

