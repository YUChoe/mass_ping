from setuptools import setup

with open('README.md', 'r') as fp:
    long_desc = fp.read()

setup(
    name='mass-ping',
    version='1',
    author='Tom YU Choe',
    author_email='yonguk.choe@gmail.com',
    description='A threaded ICMP ping using /bin/ping, ping.exe.',
    long_description=long_desc,
    url='https://github.com/YUChoe/mass_ping',
    long_description_content_type="text/markdown",
    py_modules=['mass_ping'],
    package_dir={'': 'src'},
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
