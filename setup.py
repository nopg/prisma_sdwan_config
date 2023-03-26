from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='cloudgenix_config',
      version='1.9.0b2',
      description='Configuration exporting and Continuous Integration (CI) capable configuration importing for the '
                  'CloudGenix Cloud Controller.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/CloudGenix/cloudgenix_config',
      author='CloudGenix Developer Support',
      author_email='developers@cloudgenix.com',
      license='MIT',
      include_package_data=True,
      install_requires=[
            'cloudgenix >= 6.1.1b1, < 6.1.3b1',
            'PyYAML >= 5.3',
            'jinja2==3.1.2',
            'typer==0.7.0',
            'prisma_sase @ git+https://github.com/PaloAltoNetworks/prisma-sase-sdk-python.git'
      ],
      packages=['cloudgenix_config', 'yaml_config'],
      entry_points={
            'console_scripts': [
                  'do_site = cloudgenix_config.do:go',
                  'pull_site = cloudgenix_config.pull:go',
                  'build_site = yaml_config.build:go'
                  ]
      },
      classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8"
      ]
      )
