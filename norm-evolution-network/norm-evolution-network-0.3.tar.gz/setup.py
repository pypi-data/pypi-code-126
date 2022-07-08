from setuptools import setup
import os

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

setup(
  name = 'norm-evolution-network',         
  packages = ['norm_evolution_network'],   
  version = '0.3',      
  license='MIT',        
  description = 'Simulates which strategy evolves when agents are connected with each others via social network',  
  long_description=read_file('README.md'),
  long_description_content_type='text/markdown',  
  author = 'ankurtutlani',                   
  author_email = 'ankur.tutlani@gmail.com',      
  url = 'https://github.com/ankur-tutlani/norm-evolution-network',   
  download_url = 'https://github.com/ankur-tutlani/norm-evolution-network/archive/refs/tags/v_03.tar.gz',    
  keywords = ['game theory', 'evolutionary game', 'social norms','multi-agents','evolution','social network','small world network','connected network','grid network'],   
  install_requires=[            
          'numpy',
		  'pandas',
		  'networkx',
		  'matplotlib',
		  'setuptools'
		  
		  
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
												
	'Programming Language :: Python :: 3.7',
  ],
)