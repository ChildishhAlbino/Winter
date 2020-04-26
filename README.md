# Winter

(Proof of Concept) Command line password generator.

## Concept

You type a generation key string following the below rules and Winter will generate a password for you based on the rules.

## Basic Char rules

- Alphabetical character e.g `'j'`:

  - Produces a word of any length starting with that letter. If the letter is capitalized, so is that letter in the word.

- A question mark `'?'`:

  - A wildcard character. Produces a word of the same length as the number of `'?'s` found in that position.  
    i.e `????` would return any four letter word.

- A hash symbol `'#'`:

  - A numerical wildcard. Returns a number of however many digits as the number of `'#'s` found in that position.  
    i.e `#####` would return any five digit number.

## Usage

* Install `pyperclip` via `pip install pyperclip`.
* Type out a string following the rules e.g `### ???? l p`
* Copy it to the clipboard.
* Run `python winter.py`.
* Paste your result. e.g. `425 pond luka pineapple`

## Examples

For the below string:

`a b c d`

Winter would generate a password of four random words starting with the letter a, b, c, and then finally d.
i.e:

`apple Barbara courtney dixon`

However a string like this:

`a b C`

might generate:

`anderson billy Clock`

and a string like

`???? b C d`

would generate something like:

`pear battle Coupon disco`
