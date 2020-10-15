 
from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: POSIX :: Linux',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='fliptrack',
  version='1.0.0',
  description='A Library for getting Flipkart Products info',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/saikatsahana77/fliptrack.git',
  author='Saikat Sahana',
  author_email='saikatsahana91@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='flipkart_python fliptrack flipkart_module_python', 
  packages=find_packages(),
  install_requires=['requests','bs4'] 
)