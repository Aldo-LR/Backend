const express = require("express")

const app = express()
const port = 5000

app.get('/',(req,res)=>{
    res.send('<center><h1>Bievenido a mi servidor: aldo 123</h1></center>')

})

app.get('/json',function(req,res){
    res.json({
        nombre: 'Aldo',
        dni: '72854498',
        email: 'aldog@gmail.com'
})
})

app.get('/saludar/:nombre',function(req,res){
    res.send('Hola '+req.params.nombre)
})

app.get('/formulario',function(req,res){
    html = "<form action='http://localhost:5000/saludopost' method='post'>"
    html += "<input type='text' name='nombre'>"
    html += "<input type='submit' value='Enviar'>"
    html += "</form>"
    res.send(html)
})

const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/saludopost',function(req,res){
    html = "<h1>Hola como estas "+ req.body.nombre +"</h1>"	
    res.send(html)

})

app.use(express.json());

app.post('/saludopostjson',function(req,res){
    const nombre = req.body.nombre;
    res.json({
        'saludo':'hola'+nombre
    })
})



app.listen(port,function(){
    console.log('servidor corriendo en el puerto http://localhost:'+port)
})