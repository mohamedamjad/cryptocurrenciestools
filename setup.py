from distutils.core import setup
import setuptools

def readme():
    with open("README.md") as f:
        return f.read()

setup(
  name='cryptocurrenciestools',
  packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']), # this must be the same as the name above
  version='0.2dev',
  description='Download and analyse cryptocurrencies data',
  long_description=readme(),
  author='Mohamed Amjad LASRI',
  author_email='amjad.sig@gmail.com',
  url='https://github.com/mohamedamjad/CMC_data_sniffer', # use the URL to the github repo
  download_url='https://github.com/mohamedamjad/CMC_data_sniffer/archive/0.2dev.tar.gz', # I'll explain this in a second
  keywords=['cryptocurrency', 'analysis', 'tools', 'bitcoin', 'data'], # arbitrary keywords
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2.7',
  ],
  install_requires=['requests','pandas'],
  python_requires='>=2.6',
)
