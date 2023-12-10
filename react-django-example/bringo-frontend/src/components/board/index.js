import React, { Component } from 'react'
import Tile from '../tile'
import './style.css'
import axios from 'axios'
import config from '../../config'
import { shuffle } from 'lodash'

class Board extends Component {

  state = {
    name: '',
    tiles: []
  }

  componentDidMount() {
    axios.get(config.BACKEND_URL+`/api/boards?id=${this.props.match.params.id}`)
    .then(res => {
      this.setState({
        name: res.data[0].name,
        tiles: res.data[0].tiles.split('|')
      })
    })
    .catch(e => {
      console.log(e)
    })
    .finally(() => {
      this.shuffleTiles()
    })
  }

  shuffleTiles() {
    let tiles = this.state.tiles.slice()

    if (tiles.length >= 24) {
      tiles = shuffle(tiles)
    } else {
      tiles = shuffle(tiles)
      while (tiles.length < 24) {
        tiles.push(...shuffle(tiles))
      }
    }
    
    this.setState({tiles: tiles})
  }

  render() {

    return (
      <div className="board-container">
        <div className="board-title-container">
          <h1>{this.state.name}</h1>
        </div>
        <table className="board-table">
          <tbody>
            <tr>
              <Tile text={this.state.tiles[0]} />
              <Tile text={this.state.tiles[1]} />
              <Tile text={this.state.tiles[2]} />
              <Tile text={this.state.tiles[3]} />
              <Tile text={this.state.tiles[4]} />
            </tr>
            <tr>
              <Tile text={this.state.tiles[5]} />
              <Tile text={this.state.tiles[6]} />
              <Tile text={this.state.tiles[7]} />
              <Tile text={this.state.tiles[8]} />
              <Tile text={this.state.tiles[9]} />
            </tr>
            <tr>
              <Tile text={this.state.tiles[10]} />
              <Tile text={this.state.tiles[11]} />
              <Tile text="free space" />
              <Tile text={this.state.tiles[12]} />
              <Tile text={this.state.tiles[13]} />
            </tr>
            <tr>
              <Tile text={this.state.tiles[14]} />
              <Tile text={this.state.tiles[15]} />
              <Tile text={this.state.tiles[16]} />
              <Tile text={this.state.tiles[17]} />
              <Tile text={this.state.tiles[18]} />
            </tr>
            <tr>
              <Tile text={this.state.tiles[19]} />
              <Tile text={this.state.tiles[20]} />
              <Tile text={this.state.tiles[21]} />
              <Tile text={this.state.tiles[22]} />
              <Tile text={this.state.tiles[23]} />
            </tr>
          </tbody>
        </table>
      </div>
    )
  }
}

export default Board