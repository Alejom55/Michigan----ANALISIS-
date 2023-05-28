const express = require('express');#1
const session = require('express-session');#1
const bodyParser = require('body-parser');#1
const app = express();#1
const ejs = require('ejs');#1
app.set('view engine', 'ejs');#1

app.use(bodyParser.urlencoded({ extended: false }));#1
app.use(bodyParser.json());#1
app.use(session({#1
  secret: 'mi_secreto', #1
  resave: false, #1
  saveUninitialized: false #1
}));
app.engine('html', ejs.renderFile); #1
app.set('view engine', 'ejs'); #1
app.set('views', './views'); #1


/* GET METHODS */

app.get('/', (req, res) => { #1
  if (!req.session.login) { res.redirect('/login'); return; } #1
  res.redirect('/home'); #1
});


app.get('/home', (req, res) => { #1
  //console.log('SESSION USERNAME HOME ', req.session.username)
 
  res.render('home'); #1
});

app.post('/home', (req, res) => { #1
  console.log('BODY HOME ', req.body) #1

  res.render('home'); #1
});


app.listen(7777, () => { #1
  console.log('El servidor está funcionando en el puerto 7777'); #1
});

#En general, el código proporcionado tiene una complejidad constante para la mayoría de las operaciones, lo que significa que el tiempo de ejecución y el uso de recursos no aumentan a medida que los datos de entrada crecen.
