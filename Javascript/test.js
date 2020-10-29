const assert = require('assert').strict;
const {washInEquation, areaUnderWashInEquation} = require('./equation.js')


// Tests for  washInEquation
assert.equal( 1.0, washInEquation(5))

const actual = washInEquation(15)

assert(2.73083481749 >= actual &&  2.67675888051 <= actual)

// Tests for areaUnderWashInEquation

assert.equal(0.0, areaUnderWashInEquation(0))

const area_15 = areaUnderWashInEquation(0)
assert(2.73083481749 >= area_15 &&  2.67675888051 <= area_15)

