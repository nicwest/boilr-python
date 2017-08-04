{{ PackageName }}
{{repeat "=" (len PackageName)}}

{{ Description }}

**source code**: `{{SourcePrefix}}/{{PackageName}}`_

**issues**: `{{SourcePrefix}}/{{PackageName}}/issues`_

**change log**: `{{SourcePrefix}}/{{PackageName}}/blob/master/CHANGELOG.md`_


Installation
============

.. code-block:: bash

    pip install {{PackageName}}

Usage
=====

.. code-block:: python
    import {{PackageName}}

Contributing
============

1. `create an issue on github <{{SourcePrefix}}/{{PackageName}}/issues>`_
2. fork `the repository <{{SourcePrefix}}/{{PackageName}}>`_ and make your
   changes
3. write a test to show the bug was fixed and to make sure the bug is not
   reintroduced in the future
4. update the CHANGELOG.md file with your changes in the Unrelased section
5. create a pull request. 
