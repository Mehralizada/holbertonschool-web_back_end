const http = require('http');
const fs = require('fs');
const path = require('path');

const countStudents = (database) => {
  return new Promise((resolve, reject) => {
    fs.readFile(database, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const students = lines.slice(1).filter(line => line.trim() !== '').map(line => line.split(','));
      const totalStudents = students.length;

      const csStudents = students.filter(student => student[3] === 'CS').map(student => student[0]);
      const sweStudents = students.filter(student => student[3] === 'SWE').map(student => student[0]);

      let output = `Number of students: ${totalStudents}\n`;
      output += `Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}\n`;
      output += `Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`;

      resolve(output);
    });
  });
};

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');

    const database = process.argv[2];
    if (!database) {
      res.end('Database is not provided');
    } else {
      try {
        const studentData = await countStudents(database);
        res.end(studentData);
      } catch (err) {
        res.end(err.message);
      }
    }
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
