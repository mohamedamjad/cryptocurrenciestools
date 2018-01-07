from distutils.core import setup


def readme():
    with open("README.md") as f:
        return f.read()

setup(
  name='cryptocurrenciestools',
  packages=['cryptocurrenciestools'], # this must be the same as the name above
  version='0.1',
  description='Download and analyse cryptocurrencies data',
  long_description=readme(),
  author='Mohamed Amjad LASRI',
  author_email='amjad.sig@gmail.com',
  url='https://github.com/mohamedamjad/CMC_data_sniffer', # use the URL to the github repo
  download_url='https://github.com/mohamedamjad/CMC_data_sniffer/archive/0.1.tar.gz', # I'll explain this in a second
  keywords=['cryptocurrency', 'analysis', 'tools', 'bitcoin', 'data'], # arbitrary keywords
  install_requires=['pandas','requests'],
  classifiers=[],
)