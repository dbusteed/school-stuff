import React,{Component} from 'react'
import './style.css'

class Tile extends Component {

  constructor() {
    super()

    this.state = {
      marked: false
    }
  }

  toggleMarked = () => {
    this.setState({marked: !this.state.marked})
  }

  render() {
    return (
      <td className="tile-td" style={{"backgroundColor": (this.state.marked ? '#e5e5e5' : '#ffffff')}} onClick={this.toggleMarked}>
        <p className="tile-text">{this.props.text}</p>
      </td>
    )
  }
}

export default Tile