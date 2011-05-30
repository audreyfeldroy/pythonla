############################
Code Documentation Standards
############################

All Python code must be documented using docstrings & comments written in
correct RST. These docstrings are later compiled into documentation available
from the main docs page.

Docstrings in Python
====================

Docstrings begin and end with a triple-double-quote, **"""**, and are inserted
*inside* the object they are documenting.

Sphinx defines a set of keywords that are specially formatted when placed in
docstrings.

Common sphinx keywords are:

    * param, parameter, arg, argument, key, keyword: Description of a parameter.
    * type: Type of a parameter.
    * raises, raise, except, exception: That (and when) a specific exception is raised.
    * var, ivar, cvar: Description of a variable.
    * returns, return: Description of the return value.
    * rtype: Return type.

Example usage::

    :param filename: A file name.
    :type filename: String

    :returns: type -- Description of return

The scope of a keyword extends one RST paragraph or until another keyword is
specified. For a longer description, simply start another line without
indentation::

    :returns: int -- The number of people it
              took to write these docs.

For a complete list, see
http://sphinx.pocoo.org/markup/desc.html#info-field-lists

Docstrings in Comment Style
===========================

Documentation can also be specified using hash comments using a :, like so::

    #: Description of the field
    myfield = 4

These are still parsed by sphinx and rst is still valid. This is especially
useful for describing properties, as the comments come *before* the item to be
described.

The Standard
============

Imports
-------

Docstrings for imports are not parsed by Sphinx's doc generation system, so
any links included here will not work. Instead, add a comment here if it is
not obvious why you import a module, class, or function.

Modules
-------

The docstring at the beginning of the file should contain a long description
of the module's purpose as well as a complete bolded dotted name of the
module::

    # -*- coding: utf-8 -*-
    """
        **package.module**

        A brief description goes here.

    """


Classes
-------

Should include:

    * A short description
    * A long description offering insight into class functionality
    * A link to narrative documentation in RST format

An example docstring::

    """[short description - <= 80 characters]

        [Long description - 2+ lines of text]

        See :ref:`Model Car Narrative Docs`
    """

.. note::

   Documentation for the __init__ method of a class should be placed in the
   docstring of the class itself. Sphinx ignores documentation of the __init__
   method.

Class Properties
----------------

A hash comment in the following form should be used before each field. This
is parsed by sphinx and can be in RST format.

::

    #: Description of the field
    myfield = 4

Functions & Methods
-------------------

Should include:

    * A short description
    * A long description (when the short is not enough)
    * A list of parameters with descriptions and an example, using the sphinx
      *\:param:* and *\:type:* keywords
    * A list of exceptions raised using the sphinx *\:raises:* keyword
    * The return value with the type and a short description, using the sphinx
      *\:raises:* keyword.

An example docstring::

    """[short description - <= 80 characters]

        :param filename: A file name.
        :type filename: String

        :returns: type -- Description of return

        :raises: ExceptionType, AnotherException Type
    """


.. _docstandards-example-code:

Example Code
============

Code example with all of the above

.. code-block:: python

    # -*- coding: utf-8 -*-
    """
        **pharaoh.path.to.Module**

        This module is an example module for showing documentation.

        It defines one global:

        **global_one** : Description of global_one

    """

    # Included for creating GUIDS
    import uuid


    global_one = 3


    class Model_Class:
        """[short description - <= 80 characters]

        [Long description - 2+ lines of text]

        See :ref:`Model Car Narrative Docs`
        """

        #: Description of wings parameter
        wings = None

        #: Description of headlights parameter
        headlights = 2

        def big_long_function_name(pants, trousers):
            """[short description - <= 80 characters]

            :param pants: Description of pants.
            :type pants: Type of pants.
            :param trousers: Description of trousers.
            :type trousers: Type of trousers.

            :returns: type -- Description of return

            :raises: ExceptionType, AnotherException Type
            """
            pass
