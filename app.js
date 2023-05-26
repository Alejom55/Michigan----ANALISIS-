const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const app = express();
const ejs = require('ejs');
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(session({
  secret: 'mi_secreto',
  resave: false,
  saveUninitialized: false
}));
app.engine('html', ejs.renderFile);
app.set('view engine', 'ejs');
app.set('views', './views');


/* GET METHODS */

app.get('/', (req, res) => {
  if (!req.session.login) { res.redirect('/login'); return; }
  res.redirect('/home');
});


app.get('/home', (req, res) => {
  //console.log('SESSION USERNAME HOME ', req.session.username)

  res.render('home');
});

app.post('/home', (req, res) => {
  console.log('BODY HOME ', req.body)

  res.render('home');
});


app.listen(7777, () => {
  console.log('El servidor está funcionando en el puerto 7777');
});
