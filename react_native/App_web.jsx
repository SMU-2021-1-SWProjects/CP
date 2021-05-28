import React, { Component } from 'react'
import styles from './login.css';
export default class App extends Component {
  state = {
    eid : "",
    epw : "",
    nid : "",
    npw : "",
    url : "",
  }

  handleChange =(e)=>{
    this.setState({
      [e.target.name] : e.target.value,
    });
  }

  submitId = ()=>{
    const post ={
      eid : this.state.eid,
      epw : this.state.epw,
      nid : this.state.nid,
      npw : this.state.npw,
      url : this.state.url,
    };

    fetch("http://localhost:3001/idplz", {
      method : "post", // 통신방법
      headers : {
        "content-type" : "application/json",
      },
      body : JSON.stringify(post),
    })
    .then((res)=>res.json())
    .then((json)=>{
      this.setState({
        eid : json.text,
        epw : json.text,
        nid : json.text,
        npw : json.text,
        url : json.text,
      });
    });
  };

  render() {
    return (
        <html>
            <head>
                <link rel="stylesheet" type="text/css" href="./login.css" />
            </head>
            <body width="100%" height="100%">
                <form action="index.html" method="post" class="loginForm">
                    <h2>아이디 비밀번호 입력</h2>
                    <div class="idForm">
                        <input onChange={this.handleChange} name = "eid" type="text" class="id" placeholder="E강의동 ID" />
                    </div>

                    <div class="passForm">
                        <input onChange={this.handleChange} name = "epw" type="password" class="pw" placeholder="E강의동 PW" />
                    </div>

                    <div class="idForm">
                        <input onChange={this.handleChange} name = "nid"  type="text" class="id" placeholder="네이버 ID" />
                    </div>

                    <div class="passForm">
                        <input onChange={this.handleChange} name = "npw"  type="password" class="pw" placeholder="네이버 PW" />
                    </div>

                    <div class="idForm">
                        <input onChange={this.handleChange} name = "url"  type="text" class="id" placeholder="Slack URL" />
                    </div>

                    <button type="button" class="btn" onClick = {this.submitId}>
                      저장
                    </button>
                </form>
            </body>
        </html>
    )
  }
}
