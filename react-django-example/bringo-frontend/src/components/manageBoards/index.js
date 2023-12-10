import React, { Component } from 'react'
import config from '../../config'
import axios from 'axios'
import { connect } from 'react-redux'
import { Link } from 'react-router-dom'
import './style.css'

class ManageBoards extends Component {
  
  state = {
    boards: []
  }

  componentDidMount() {
    this.fetchBoards()
  }

  fetchBoards() {
    axios.get(config.BACKEND_URL+`/api/boards?owner=${this.props.token}`)
      .then(res =>{
        this.setState({
          boards: res.data
        })
      })
      .catch(err => {
        console.log(err)
      })
  }

  deleteBoard(id) {
    axios.delete(config.BACKEND_URL+`/api/boards/${id}/`, {data: {
      board_id: id,
      token: this.props.token
    }})
      .then(res => {
        console.log('yup')
        this.fetchBoards()
      })
      .catch(err => {
        console.log(err)
      })
  }
  
  render() {
    return (
      <div>
        <h1>manage my boards</h1>
        {
          this.state.boards.length === 0 ?

          <div>
            <p>no boards found...</p>
            <p className="p-link" onClick={() => this.fetchBoards()}>click to refresh</p>
          </div>

          :

          <table className="manage-table"> 
            <tbody>
              {
                this.state.boards.map((board, index) => (
                  <tr key={index}>
                    <td>{board['name']}</td>
                    <td>           
                      <Link to={`/board/${board['id']}`}>
                        view
                      </Link>
                    </td>
                    <td>
                      <Link to={`/edit/${board['id']}`}>
                        edit
                      </Link>
                    </td>
                    <td>
                      <span className="p-link" onClick={() => this.deleteBoard(board['id'])}>delete</span>
                    </td>
                  </tr>
                ))
              }
            </tbody>
          </table>
        }
      </div>
    )
  }
}

const mapStateToProps = state => {
  return {
    token: state.token
  }
}

export default connect(mapStateToProps, null)(ManageBoards)