from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name= 'TheProactivestradinglibrary' ,
    version= '0.0.1',
    description='A demo trading library',
    Long_description=open('README-txt').read() + '\n\n' + open( 'CHANGELOG.txt'). read(),
    url='',
    author='The Proactives', 
    author_email='wenhong92290@gmail.com',
    Licenses ='MIT',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=['']
)