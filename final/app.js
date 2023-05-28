// O(1)
const express = require('express');

// O(1)
const session = require('express-session');

// O(1)
const bodyParser = require('body-parser');

// O(1)
const app = express();

// O(1)
const ejs = require('ejs');

// O(1)
app.set('view engine', 'ejs');

// O(1)
app.use(bodyParser.urlencoded({ extended: false }));

// O(1)
app.use(bodyParser.json());

// O(1)
app.use(session({
  secret: 'mi_secreto',
  resave: false,
  saveUninitialized: false
}));

// O(1)
app.engine('html', ejs.renderFile);

// O(1)
app.set('view engine', 'ejs');

// O(1)
app.set('views', './views');

/* GET METHODS */

// O(1)
app.get('/', (req, res) => {
  if (!req.session.login) { res.redirect('/login'); return; }
  res.redirect('/home');
});

// O(1)
app.get('/home', (req, res) => {
  //console.log('SESSION USERNAME HOME ', req.session.username)
  res.render('home');
});

// O(1)
app.post('/home', (req, res) => {
  console.log('BODY HOME ', req.body)
  res.render('home');
});

// O(1)
app.listen(7777, () => {
  console.log('El servidor está funcionando en el puerto 7777');
});
//La mayoría de las operaciones en el código tienen una complejidad constante O(1), lo que significa que su tiempo de ejecución no depende del tamaño de la entrada.
