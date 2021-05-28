const express = require("express");
const app = express();
const port = 3001; // react의 기본값은 3000이니까 3000이 아닌 아무 수
const cors = require("cors");
const bodyParser = require("body-parser");
const mysql = require("mysql"); // mysql 모듈 사용

var connection = mysql.createConnection({
    host : "localhost",
    user : "root", //mysql의 id
    password : "mysql_76", //mysql의 password
    database : "react_native", //사용할 데이터베이스
});

connection.connect();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

app.get('/', (req, res) =>{
    res.send('혁이는 코딩 중!')
})

app.post("/idplz", (req,res)=>{
    const eid = req.body.eid;
    const epw = req.body.epw;
    const nid = req.body.nid;
    const npw = req.body.npw;
    const url = req.body.url;

    console.log(req.body);
    connection.query("INSERT INTO react_native.id_pw (eid, epw, nid, npw, url) values (?, ?, ?, ?, ?)",[eid, epw, nid, npw, url],
    function(err,rows,fields){
        if(err){
            console.log("실패");
            // console.log(err);
        }else{
            console.log("성공");
            // console.log(rows);
        };
    });
});

app.listen(port, ()=>{
    console.log(`Connect at http://localhost:${port}`);
})
