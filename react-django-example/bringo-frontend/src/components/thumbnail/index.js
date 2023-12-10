import React, { Component } from 'react'
import './style.css'

class Thumbnail extends Component {

  rows = [1,2,3,4,5]

  lilTable = (
    <table className="lil-table">
      <tbody>
        {
          this.rows.map(_ => (
            <tr>
              {
                this.rows.map(_ => (
                  <td style={{backgroundColor: Math.random() < .37 ? "#e5e5e5" : "#ffffff"}}></td>
                ))
              }
            </tr>
          ))
        }
      </tbody>
    </table>
  )

  render() {
    return (
      <div className="board-thumbnail">
        <p className="board-thumbnail-title">{this.props.name}</p>
        {this.lilTable}
      </div>
    )
  }
}

export default Thumbnail