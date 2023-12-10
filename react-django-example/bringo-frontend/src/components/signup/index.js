import React, { Component } from 'react'
import { Form, Input, Button } from 'antd'
import { connect } from 'react-redux'
import * as actions from '../../store/actions/auth'

class SignUp extends Component {
  state = {
    confirmDirty: false,
    autoCompleteResult: []
  };

  handleSubmit = e => {
    e.preventDefault();
    this.props.form.validateFieldsAndScroll((err, values) => {
      if (!err) {
        this.props.onSignUp(values.email, values.password, values.confirm)
      }
    })
    setTimeout(() => {
      if (this.props.token !== null) {
        this.props.history.push("/")
      }
    }, 1000)
  };

  handleConfirmBlur = e => {
    const { value } = e.target;
    this.setState({ confirmDirty: this.state.confirmDirty || !!value });
  };

  compareToFirstPassword = (rule, value, callback) => {
    const { form } = this.props;
    if (value && value !== form.getFieldValue('password')) {
      callback('Two passwords that you enter is inconsistent!');
    } else {
      callback();
    }
  };

  validateToNextPassword = (rule, value, callback) => {
    const { form } = this.props;
    if (value && this.state.confirmDirty) {
      form.validateFields(['confirm'], { force: true });
    }
    callback();
  };

  render() {
    const { getFieldDecorator } = this.props.form;

    const formItemLayout = {
      labelCol: {
        xs: { span: 24 },
        sm: { span: 8 },
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 16 },
      },
    };
    const tailFormItemLayout = {
      wrapperCol: {
        xs: {
          span: 24,
          offset: 0,
        },
        sm: {
          span: 16,
          offset: 8,
        },
      },
    };

    let errorMessage = null;
    if (this.props.error) {
      // console.log( this.props.error.response.data['non_field_errors'].map(x => `<p>${x}</p>`) )
      errorMessage = (
        <div>
          <p>{this.props.error.response.data['email']}</p>
          <p>{this.props.error.response.data['password1']}</p>
        </div>
      )
    }

    return (
      <Form {...formItemLayout} onSubmit={this.handleSubmit}>
        <h1>sign up</h1>
        {errorMessage}
        <Form.Item label="email">
          {getFieldDecorator('email', {
            rules: [
              {
                type: 'email',
                message: 'The input is not valid E-mail!',
              },
              {
                required: true,
                message: 'Please input your E-mail!',
              },
            ],
          })(<Input />)}
        </Form.Item>
        <Form.Item label="password" hasFeedback>
          {getFieldDecorator('password', {
            rules: [
              {
                required: true,
                message: 'Please input your password!',
              },
              {
                validator: this.validateToNextPassword,
              },
            ],
          })(<Input.Password />)}
        </Form.Item>
        <Form.Item label="confirm password" hasFeedback>
          {getFieldDecorator('confirm', {
            rules: [
              {
                required: true,
                message: 'Please confirm your password!',
              },
              {
                validator: this.compareToFirstPassword,
              },
            ],
          })(<Input.Password onBlur={this.handleConfirmBlur} />)}
        </Form.Item>
        <Form.Item {...tailFormItemLayout}>
          <Button type="primary" htmlType="submit">
            sign up
          </Button>
        </Form.Item>
      </Form>
    );
  }
}

const WrappedSignUpForm = Form.create({ name: 'register' })(SignUp);

const mapStateToProps = (state) => {
  return {
    loading: state.loading,
    error: state.error
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onSignUp: (email, password, confirm) => {
      dispatch(actions.authSignup(email, email, password, confirm))
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(WrappedSignUpForm)