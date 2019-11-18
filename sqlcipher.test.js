const Database = require('./lib');

const dbPath = './temp/sqlcipher.db'
const db = new Database(dbPath);
db.pragma('key = "123"');
db.prepare('CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT)').run();
db.prepare('INSERT INTO people (name) VALUES (@name)').run({ name: 'jack' });
console.log(db.prepare(`SELECT * FROM people;`).all());
db.close();

const db2 = new Database(dbPath);
db2.pragma('key = "1234"')
try {
  db2.prepare(`SELECT * FROM people;`).all();
} catch (e) {
  console.log('sqlcipher build passed!')
}
