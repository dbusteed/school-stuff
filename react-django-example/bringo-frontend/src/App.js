import React, { Component } from 'react'
import './App.css'
import Board from './components/board'
import NavBar from './components/navbar'
import Login from './components/login'
import Main from './components/main'
import SignUp from './components/signup'
import CreateBoard from './components/createBoard'
import ManageBoards from './components/manageBoards'
import EditBoard from './components/editBoard'
import { 
  BrowserRouter as Router,
  Route
} from 'react-router-dom'
import { connect } from 'react-redux'
import * as actions from './store/actions/auth'

class App extends Component {

  componentDidMount() {
    this.props.onTryAutoSignup()
  }

  render() {
    return (
      <Router>
        <NavBar />
        <div className="main">
          <div className="main-gutter"></div>
          <div className="main-container">
            <Route exact path="/" component={Main} />
            <Route path="/board/:id" component={Board} />
            <Route path="/login" component={Login} />
            <Route path="/signup" component={SignUp} />
            <Route path="/create" component={CreateBoard} />
            <Route path="/manage" component={ManageBoards} />
            <Route path="/edit/:id" component={EditBoard} />
          </div>
          <div className="main-gutter"></div>
        </div>
      </Router>
    )
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onTryAutoSignup: () => dispatch(actions.authCheckState())
  }
}

export default connect(null, mapDispatchToProps)(App);
