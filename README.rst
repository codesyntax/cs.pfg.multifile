Introduction
============

This product provides a new form field for PloneFormGen_ forms that allows
adding more than one files using the `jquery.filer`_

The standard file field for PloneFormGen_ allows only adding one file. Adding
just a new file field with the option *multiple* can solve the problem, but
we think that the usability of that option is not good. Is not obvious for
a lot of people to push Ctrl or Shift to add more than one files. So to
address this usability feature, we have added the `jquery.filer`_ file
selection widget, that shows in a very nice interface the added files with an
option to delete them or adding new ones without much effort.

.. _PloneFormGen: https://pypi.python.org/pypi/Products.PloneFormGen
.. _`jquery.filer`: https://github.com/CreativeDream/jQuery.filer

Installation
============

Add this product to your buildout file and rerun the buildout.

Go to Site Setup -> Add ons and install it

A new field will show in your PloneFormGen_ forms called MultiFileField.
