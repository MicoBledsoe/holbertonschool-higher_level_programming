#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num) || num < 1) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < num) {
    console.log('X'.repeat(num));
    i++;
  }
}
