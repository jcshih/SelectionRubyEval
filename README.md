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

- OSX: <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>r</kbd>
- Linux: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>r</kbd>
- Windows: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>r</kbd>

Through Command Palette, find `MultiRubyEval: evaluate selections`

Enter a ruby expression, where the variable `x` will contain the selection as a string. To also evaluate the selection itself as a ruby expression, use `eval(x)`. Outputs are treated as string also, so if the result of an expression is a ruby structure, you can use `#to_s` to get its string representation.

Note: Currently, MultiRubyEval does not handle newlines, so each selection's input and output must reside on one line.


Examples
--------


