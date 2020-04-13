#!/usr/bin/env python

from setuptools import setup, find_packages

from pathlib import Path

current_path = Path(__file__).resolve()
project_dir = current_path.parent
version_path = project_dir / "hyperion" / "version.py"

with open(version_path) as f:
    exec(f.read())


setup(name = 'HyperionAPI',
      version = __version__,
      description = 'Public API for Hyperion Instruments from Micron Optics, Inc.',
      author = 'Dustin W. Carr',
      author_email = 'dcarr@micronoptics.com',
      include_package_data = True,
      packages = find_packages(exclude=("*.test","test","test_*","tests",)),
      py_modules=['hyperion']
      )
