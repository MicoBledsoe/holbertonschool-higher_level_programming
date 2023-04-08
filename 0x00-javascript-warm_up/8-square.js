#!/usr/bin/node

const args = process.argv;
const size = parseInt(args[2]);

if (isNaN(size) || size < 1) {
  console.log('Missing Size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let b = 0; b < size; b++) {
      line += 'X';
    }
    console.log(line);
  }
}
