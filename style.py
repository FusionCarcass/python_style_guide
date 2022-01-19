#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""This module's docstring summary line.
This is a multi-line docstring. Paragraphs are separated with blank lines.
Lines conform to 79-column limit.
Module and packages names should be short, lower_case_with_underscores.
Notice that this in not PEP8-cheatsheet.py
Seriously, use flake8. Atom.io with https://atom.io/packages/linter-flake8
is awesome!
See http://www.python.org/dev/peps/pep-0008/ for more PEP-8 details
"""


from __future__ import barry_as_FLUFL  # python mandates futures must appear
                                       # first in the module before any other
                                       # than the docstring.

__version__ = "1.0.0"  # Other dunders appear after futures but before other code

import os  # STD lib imports first
import sys  # alphabetical

import some_third_party_lib  # 3rd party stuff next
import some_third_party_other_lib  # alphabetical

import local_stuff  # local stuff last
import more_local_stuff
import dont_import_two, modules_in_one_line  # IMPORTANT!
from pyflakes_cannot_handle import *  # and there are other reasons it should be avoided # noqa
# Using # noqa in the line above avoids flake8 warnings about line length!

_a_global_var = 2  # so it won't get imported by 'from foo import *'
_b_global_var = 3

A_CONSTANT = 'ugh.'  # Use all caps for constants


# 2 empty lines between top-level funcs + classes
def naming_convention():
    """Write docstrings for ALL public classes, funcs and methods.
    Functions use snake_case.
    """
    if x == 4:  # x is blue <== USEFUL 1-liner comment (2 spaces before #)
        x, y = y, x  # inverse x and y <== USELESS COMMENT (1 space after #)
    c = (a + b) * (a - b)  # operator spacing should improve readability.
    dict['key'] = dict[0] = {'x': 2, 'cat': 'not a dog'}


class NamingConvention(object):  # Use the CapWords naming convention
    """First line of a docstring is short and next to the quotes.
    Class and exception names are CapWords.
    Closing quotes are on their own line.
    """

    a = 2
    b = 4
    _internal_variable = 3  # I prefer to use leading underscore to indicate
                            # that this variable is a class member.
                            
    class_ = 'foo'  # trailing underscore to avoid conflict with builtin

    # this will trigger name mangling to further discourage use from outside
    # this is also very useful if you intend your class to be subclassed, and
    # the children might also use the same var name for something else; e.g.
    # for simple variables like 'a' above. Name mangling will ensure that
    # *your* a and the children's a will not collide.
    __internal_var = 4

    # some examples of how to wrap code to conform to 79-columns limit:
    def __init__(self,
                 width,
                 height,
                 color='black',
                 emphasis=None,
                 highlight=0):
        
        if width == 0 and height == 0 and \
           color == 'red' and emphasis == 'strong' or \
           highlight > 100:
            raise ValueError('sorry, you lose')
        if width == 0 and height == 0 and (color == 'red' or
                                           emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" %
                             (width, height))
        Blob.__init__(self, width, height,
                      color, emphasis, highlight)

    # empty lines within method to enhance readability; no set rule
    short_foo_dict = {'loooooooooooooooooooong_element_name': 'cat',
                      'other_element': 'dog'}

    long_foo_dict_with_many_elements = {
        'foo': 'cat',
        'bar': 'dog'
    }

    # 1 empty line between in-class definitions
    def foo_method(self, x, y):  # Methods use lower_case_with_underscores
        """Performs the calculation a * x + b * y
        This is the second line of the docstring.
        
        x -- float representing the pressure of cylinder 1
        y -- float representing the temperature of monitor 2
        """
        return self.a * x + self.b * y  # I recommend always using self to
                                        # refer to class members so that it is
                                        # very obvious to the readers what the
                                        # scope of the variable is.

    @classmethod
    def bar(cls, value=2):  # Don't add space to default parameter values
        """Sets the default value of self.a
        Always use cls for class methods.
        
        value -- integer the value to set for all self.a default = 2.
        """
        cls.a = value
        
    @staticmethod
    def add(num1, num2):
        """Static methods should be used when the data is not tied to the
        class itself, but needs to be accessible publically. No access to the
        instance members a and b.
        """
        return num1 + num2

# a 79-char ruler:
# 34567891123456789212345678931234567894123456789512345678961234567897123456789

"""
Common naming convention names:
snake_case
MACRO_CASE
camelCase
CapWords

Avoid the letters 'l' (lowercase letter el), 'O' (uppercase letter oh),
or 'I' (uppercase letter eye) as single character variable names.
"""

#Use whitespace sparingly in expressions and statetments
example = {'eggs': 2, 'ham': 1}
x = 4
y = 2
if x == 4: print(x, y)
x, y = y, x  # swaps two variables

# Newline at end of file