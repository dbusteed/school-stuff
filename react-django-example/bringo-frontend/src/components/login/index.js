import React, { Component } from 'react'
import { Form, Icon, Input, Button, Spin } from 'antd'
import { connect } from 'react-redux'
import * as actions from '../../store/actions/auth'
import { Link } from 'react-router-dom'

const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />

class Login extends Component {
  handleSubmit = e => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {
      if (!err) {
        this.props.onAuth(values.username, values.password)
      }
    })
    setTimeout(() => {
      if (this.props.token !== null) {
        this.props.history.push("/")
      }
    }, 1000)
  }

  render() {  

    let errorMessage = null;
    if (this.props.error) {
      console.log( this.props.error.response.data['non_field_errors'].map(x => `<p>${x}</p>`) )
      errorMessage = (
        <p>{this.props.error.response.data['non_field_errors'][0]}</p>
      )
    }

    const { getFieldDecorator } = this.props.form;
    
    return (

      <div>
        {
          this.props.loading ?

          <Spin indicator={antIcon} />

          :

          <Form onSubmit={this.handleSubmit} className="login-form">
            <h1>login</h1>
            {errorMessage}
            <Form.Item>
              {getFieldDecorator('username', {
                rules: [{ required: true, message: 'Please input your username!' }],
              })(
                <Input
                prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />}
                placeholder="Email"
                />,
                )}
            </Form.Item>
            <Form.Item>
              {getFieldDecorator('password', {
                rules: [{ required: true, message: 'Please input your Password!' }],
              })(
                <Input
                prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />}
                type="password"
                placeholder="Password"
                />,
                )}
            </Form.Item>
            <Form.Item>
              <Button type="primary" htmlType="submit" className="login-form-button">
                log in
              </Button>
              <span style={{marginLeft: '10px'}}>
                or
              </span>
              <Link to="/signup" style={{marginLeft: '10px'}}>
                signup here
              </Link>
            </Form.Item>
          </Form>
        }
      </div>
    );
  }
}

const WrappedLogin = Form.create({ name: 'login' })(Login);

const mapStateToProps = (state) => {
  return {
    loading: state.loading,
    error: state.error,
    token: state.token
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onAuth: (username, password) => dispatch(actions.authLogin(username, password))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(WrappedLogin)