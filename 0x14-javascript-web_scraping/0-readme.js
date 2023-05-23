#!/usr/bin/node

const fs = require('fs');

// Check if the filename is provided as a command line argument
if (process.argv.length < 3) {
  console.log('Usage: node <script-name> <filename>');
  process.exit(1);
}

const filename = process.argv[2];

fs.readFile(filename, 'utf-8', function (err, data) {
  if (!err) {
    console.log(data);
  } else {
    console.log('{ Error: ' + err.code + ': ' + err.path + '\n    at Error (native) }');
  }
});
