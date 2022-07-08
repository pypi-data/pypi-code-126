from setuptools import setup
import os

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()
		
setup(
  name = 'norm-evolution',         
  packages = ['norm_evolution'],   
  version = '0.4',      
  license='MIT',        
  description = 'Simulates which strategy evolves when agents immitate their neighbors',   
  long_description=read_file('README.md'),
  long_description_content_type='text/markdown',
  author = 'ankurtutlani',                   
  author_email = 'ankur.tutlani@gmail.com',      
  url = 'https://github.com/ankur-tutlani/norm-evolution',   
  download_url = 'https://github.com/ankur-tutlani/norm-evolution/archive/refs/tags/v_04.tar.gz',    
  keywords = ['game theory', 'evolutionary game', 'social norms','multi-agents','evolution','circular network'],   
  install_requires=[            
          'numpy',
		  'pandas',
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