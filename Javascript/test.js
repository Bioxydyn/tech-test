const assert = require('assert').strict;
const {washInEquation, areaUnderWashInEquation} = require('./equation.js')

// Tests for  washInEquation
assert.equal(washInEquation(5), 1.0)

const actual = washInEquation(15)

assert(2.73083481749 >= actual &&  2.67675888051 <= actual)

// Tests for areaUnderWashInEquation

assert.equal(areaUnderWashInEquation(0), 0.0)

const area_15 = areaUnderWashInEquation(15)
console.log(area_15)
assert(19.84623001714354 >= area_15 &&  19.154623001714354 <= area_15)

