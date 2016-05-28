from setuptools import setup, find_packages

deps = []
try:
    import pkg_resources
except ImportError:
    pass
else:
    f = open('requirements.txt', 'r')
    try:
        deps = [str(req) for req in pkg_resources.parse_requirements(f)]
    finally:
        f.close()

setup(
    name='kudago_mapper',
    version='1.0.0',
    url='https://github.com/maxvyaznikov/kudago-test',
    download_url='https://github.com/maxvyaznikov/kudago-test',
    author='Max Vyaznikov',
    author_email='maxvyaznikov@gmail.com',
    license='Use only with permission of the author',
    description='Testing task from KudaGo.com',
    long_description=open('README.md').read(),
    platforms='Any',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
    packages=find_packages(),
    install_requires=deps,
)
