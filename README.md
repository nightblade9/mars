# Mars

[![Build Status](https://travis-ci.org/nightblade9/mars.svg?branch=master)](https://travis-ci.org/nightblade9/mars)

Mars is a command-line tools for generating and running HaxeFlixel games in Python, via Dragon. Mars is currently useful for **intermediate users of Haxe, who are used to looking up APIs and troubleshooting Haxe compilation errors.**

# Sample Usage

- `mars template`: creates a new HaxeFlixel starter project, in Python
- `mars build <platform>`: transpiles the Python code to HaxeFlixel and builds it against the specified Haxe target platform (wraps calls to `lime build <platform>`).
