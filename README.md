MultiRubyEval
=============

A Sublime Text plugin to execute ruby code on multiple selections.


Installation
------------

Assumes [ruby](https://www.ruby-lang.org) is installed, and that ruby is available in path.

Install using [Package Control](https://sublime.wbond.net/) (Recommended), or by cloning this repository into the `Packages` directory.


Usage
-----

Default key bindings:

- OSX: <kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>e</kbd>
- Linux: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>e</kbd>
- Windows: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>e</kbd>

Through Command Palette, find `MultiRubyEval: evaluate selections`

Enter a ruby expression, where the variable `x` will contain the selection as a string. To also evaluate the selection itself as a ruby expression, use `eval(x)`.


Examples
--------


