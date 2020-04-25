# Winter

Command line password generator.

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

To generate a password write a string like below:

`a b c d`

This would generate a password of four random words starting with the letter a, b, c, and d.
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
