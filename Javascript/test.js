const assert = require('assert').strict;
const washInEquation = require('./equation.js')

assert.equal( 1.0, washInEquation(5))

let actual = washInEquation(15)

assert(2.73083481749 >= actual &&  2.67675888051 <= actual)
