#!/usr/bin/env python

from setuptools import setup

setup(
    name='{{PackageName}}',
    version='{{Version}}',
    description='{{Description}}',
    author='{{AuthorName}}',
    author_email='{{AuthorEmail}}',
    url='{{SourcePrefix}}/{{PackageName}}',
    packages=['{{PackageName}}'],
    install_requires=[],
    classifiers=[
{{- if eq DevelopmentStatus "Planning" }}
        'Development Status :: 1 - Planning',
{{- else if eq DevelopmentStatus "Pre-Alpha" }}
        'Development Status :: 2 - Pre-Alpha',
{{- else if eq DevelopmentStatus "Alpha" }}
        'Development Status :: 3 - Alpha',
{{- else if eq DevelopmentStatus "Beta" }}
        'Development Status :: 4 - Beta',
{{- else if eq DevelopmentStatus "Production/Stable" }}
        'Development Status :: 5 - Production/Stable',
{{- else if eq DevelopmentStatus "Mature" }}
        'Development Status :: 6 - Mature',
{{- else if eq DevelopmentStatus "Inactive" }}
        'Development Status :: 7 - Inactive',
{{- end }}
{{- if eq PythonVersion "3" }}
        'Programming Language :: Python :: 3 :: Only',
{{- else if eq PythonVersion "2" }}
        'Programming Language :: Python :: 2 :: Only',
{{- else if eq PythonVersion "both" }}
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
{{- end }}
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
)
