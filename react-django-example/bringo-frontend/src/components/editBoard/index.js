import React, { Component } from 'react'
import { Form, Input, Button } from 'antd'
import { connect } from 'react-redux'
import { Link } from 'react-router-dom'
import axios from 'axios'
import config from '../../config'

const { TextArea } = Input;

class EditBoard extends Component {
  state = {
    message: null,
    error: false,
    boardName: null,
    boardTiles: null
  }

  componentDidMount() {
    axios.get(config.BACKEND_URL+`/api/boards/${this.props.match.params.id}/`)
      .then(res => {
        this.setState({
          boardName: res.data['name'],
          boardTiles: res.data['tiles'].split('|').join('\n')
        })
      })
      .catch(err => {
        console.log(err)
      })
  }

  handleSubmit = e => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {
      if (!err) {
        axios.put(config.BACKEND_URL+`/api/boards/${this.props.match.params.id}/`, {
          board_id: this.props.match.params.id,
          name: values.name,
          tiles: [...new Set(values.tiles.replace('|', '/').split('\n'))].join('|'),
          owner: this.props.token
        })
        .then(res => {
          if (res.data.error !== undefined) {
            this.setState({message: "incorrect user, this isn't your board!"})
          } else {
            this.setState({message: "board successfully updated!"})
          }
        })
        .catch(err => {
          this.setState({message: "something went wrong...please try again later", error: true})
          console.log(err)
        })
      }
    });
  };

  render() {
    const { getFieldDecorator } = this.props.form;
    let content;
    
    if (this.props.token == null) {
      
      // same as checking if it is the correct user?

      content = (
        <p>
          you gotta<Link to="/login"> login </Link>before editing a board
        </p>  
      )

    } else if (this.state.message !== null) {
      content = (
        <p>{this.state.message}</p>
      )

    } else {
      content = (
        <Form onSubmit={this.handleSubmit} className="login-form">
          <h1 onClick={() => console.log(this.state) }>edit board</h1>
          <br />
          <Form.Item label="board name">
            {getFieldDecorator('name', {
              rules: [{ required: true, message: 'please give your board a name!' }],
              initialValue: this.state.boardName
            })(
              <Input />,
            )}
          </Form.Item>
          <Form.Item label="board tiles (seperate with a new line)">
            {getFieldDecorator('tiles', {
              rules: [{ required: true, message: 'please give you board some tiles!' }],
              initialValue: this.state.boardTiles            
            })(
              <TextArea rows={10} />,
            )}
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit" className="login-form-button">
              update board
            </Button>
          </Form.Item>
        </Form>
      )
    }
    
    return (
      <div>
        {content}
      </div>
    );
  }
}

const WrappedEditBoard = Form.create({ name: 'edit_board' })(EditBoard);

const mapStateToProps = state => {

  return {
    token: state.token
  } 
}

export default connect(mapStateToProps, null)(WrappedEditBoard)