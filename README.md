# Bioxydyn Tech Test

## Introduction

Welcome to Bioxydyn's Technical Test! The purpose of the test is to assess your ability to write clean code that implements an equation as specified. The test can be completed using either the Javascript or python programming languages.

## Instructions

Clone this repository to your computer, and modify the file Javascript/equation.js _or_ Python/equation.py (depending on your language preference) to implement the brief below. When you are finished, zip the tech-test folder and email to matthew.heaton@bioxydyn.com. Alternatively, you may work in a private github repository and share your repository with @mj-heaton & @schofield-r.

This techncal test should take approximately 1 hour and if possible should be completed in one sitting with regular commits to show your progress. 

If you require any further information or encounter any issues in completing this test, please contact matthew.heaton@bioxydyn.com.

Please *do not* make the source code of your completed test public.

## The Brief

Complete the function `washInEquation` in `equation.js` or `equation.py` so that it implements following equation with the following parameter values:

![equation](equation.png)

where:
    t_start = 10

    A = 1

    B = 5

    τ = 12

## Testing your code

Run the provided tests to check your code.

### JavaScript

    node Javascript/test

*note: with node assertions you will only get a message if the tests have failed*

### Python 

Install pytest

    $ pip3 install pytest

Then run 

    $ pytest Python/test.py
