#!/usr/bin/node

const arg = process.argv[2];
if (isNaN(arg) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
