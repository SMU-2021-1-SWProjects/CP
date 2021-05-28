import React, { Component } from 'react'
import { View, Text, TextInput, Button, StyleSheet} from 'react-native';
// import DatePicker from 'react-datepicker/dist/react-datepicker';
// import './App.css';

import t from 'tcomb-form-native'; // 0.6.9

const Form = t.form.Form;

const User = t.struct({
    eid: t.String,
    epw: t.String,
    nid: t.String,
    npw: t.String,
    url: t.String,
  });

const options = {
  fields: {
    eid: {
      label: 'e-강의동 ID를 입력해 주세요',
      autoCapitalize: 'none'
    },
    epw: {
      label: 'e-강의동 비밀번호를 입력해 주세요',
      password: true,
      secureTextEntry: true,
      autoCapitalize: 'none'
    },
    nid: {
      label: '네이버 ID를 입력해 주세요',
      autoCapitalize: 'none'
    },
    npw: {
      label: '네이버 비밀번호를 입력해 주세요',
      password: true,
      secureTextEntry: true,
      autoCapitalize: 'none'
    },
    url: {
      label: 'Slack URL을 입력해 주세요',
      autoCapitalize: 'none'
    },
  },
};

export default class App extends Component {

  handleChange =(e)=>{
    this.setState({
      [e.target.name] : e.target.value
    });
  }

  handleSubmit = ()=>{
    const value = this._form.getValue(); // use that ref to get the form value
    console.log('value: ', value);

    const post ={
      eid : value.eid,
      epw : value.epw,
      nid : value.nid,
      npw : value.npw,
      url : value.url,
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
      <View style={styles.container}>
        <Form
          ref={c => this._form = c}
          type={User}
          options={options}
        />
        <View style={styles.buttonContainer}>
          <Button
              style={styles.buttonLabel}
              title="Register"
              color="#fff"
              onPress={() => this.handleSubmit()}
          />
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    justifyContent: 'center',
    marginTop: 50,
    padding: 20,
    backgroundColor: '#fff',
  },
  buttonContainer: {
    backgroundColor: '#467FD3',
    borderRadius: 4,
    alignSelf: 'flex-start',
    marginBottom: 24,
  },
  buttonLabel: {
    fontSize: 16,
    lineHeight: 32,
    paddingVertical: 8,
    paddingHorizontal: 32,
    color: '#fff',
  },
});
