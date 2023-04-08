#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
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
