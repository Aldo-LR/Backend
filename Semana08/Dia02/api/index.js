const express = require('express');
const app = express();

// settings
app.set('port',process.env.PORT || 5000);

//middlewares
app.use(express.json());

//routes
app.get('/',function(req,res){
    res.send({
        'status':true,
        content:'Bienvenido a mi API'
    });
})
//
const mysqlConnection = require('./database');
app.get('/employees',function(req,res){
    mysqlConnection.query('SELECT * FROM employee',(err,rows,fields)=>{
        if(!err){
            res.json(rows);
        }else{
            console.log(err);
        }
    })
});

app.post('/employee',function(req,res){
    const {name,salary} = req.body;
    const query = `insert into employee(name,salary) values(?,?)`;

    mysqlConnection.query(query,[name,salary],(err,rows,fields)=>{
        if(!err){
            res.json({
                status:true,
                message:'Employes inserted'
            });
        }else{
            console.log(err);
        }
    })
});

app.put('/employee/:id',function(req,res){
    const {name,salary} = req.body;
    const {id} = req.params;
    const query = `update employee set name = ?, salary = ? where id = ?`;

    mysqlConnection.query(query,[name,salary,id],(err,rows,fields)=>{
        if(!err){
            res.json({
                status:true,
                message:'Employes updated'
            });
        }else{
            console.log(err);
        }
    })
} ); 

app.delete('/employee/:id',function(req,res){
    const {id} = req.params;
    const query = `delete from employee 
                    where id=?`

    mysqlConnection.query(query,[id],
        (err,rows,fields)=>{
        if(!err){
            res.json({
                'status':true,
                'content':'Employee Deleted'
            })
        }else{
            console.log(err);
        }
    })
}) 



app.listen(app.get('port'),()=>{
    console.log(`Server running at http://localhost:${app.get('port')}`);
})

