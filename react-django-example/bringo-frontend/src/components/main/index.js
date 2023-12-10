import React, { Component } from 'react'
import axios from 'axios'
import Thumbnail from '../thumbnail'
import config from '../../config'
import { Link } from 'react-router-dom'
import './style.css'
import { Icon, Spin } from 'antd'

const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />

class Main extends Component {
  state = {
    loading: true,
    tileData: []
  }

  componentDidMount() {
    axios.get(config.BACKEND_URL+'/api/boards')
      .then(res => {
        this.setState({
          tileData: res.data.map( (obj) => [obj.id, obj.name] ),
          loading: false
        })
      })
      .catch(e => {
        console.log(e)
        this.setState({loading: false})
      })
  }

  render() {

    let content

    let header = (
      <h1>all bringo boards</h1>
      // add search sometime?
    )

    if (this.state.loading) {
      content = (
        <div>
          <Spin indicator={antIcon} />
        </div>
      )
    } else if (this.state.tileData.length === 0) {
      content = (
        <div>
          {header}
          <p>no boards were found, please try again later</p>
        </div>
      )
    } else {
      content = (
        <div>
          {header}
          <ul className="board-list">
            {this.state.tileData.map( (tile, index) => (
              <li>            
                <Link key={index} to={`/board/${tile[0]}`}>
                  <Thumbnail name={tile[1]} />
                </Link>
              </li>
            ))}
            </ul>
        </div>
      )
    }

    return (
      <div>
        {content}
      </div>
    )
  }
}

export default Main