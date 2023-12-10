import * as actionTypes from './actionTypes'
import axios from 'axios'
import config from '../../config'

export const authStart = () => {
  return {
    type: actionTypes.AUTH_START
  }
}

export const authSuccess = (token) => {
  return {
    type: actionTypes.AUTH_SUCCESS,
    token: token
  }
}

export const authFail = (error) => {
  return {
    type: actionTypes.AUTH_FAIL,
    error: error
  }
}

export const authLogin = (username, password) => {
  return dispatch => {
    dispatch(authStart())

    axios.post(config.BACKEND_URL+'/rest-auth/login/', {
      username: username,
      password: password
    })
    .then((res) => {
      const token = res.data.key
      const expirationDate = new Date(new Date().getTime() + 3600 * 1000) // one hour
      localStorage.setItem('token', token)
      localStorage.setItem('expirationDate', expirationDate)
      dispatch(authSuccess(token))
      dispatch(checkAuthTimeout(3600))
    })
    .catch((err) => {
      dispatch(authFail(err))
    })
  }
}

export const authLogout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('expirationDate')
  return {
    type: actionTypes.AUTH_LOGOUT
  }
}

const checkAuthTimeout = (expirationTime) => {
  return dispatch => {
    setTimeout(() => {
      dispatch(authLogout())
    }, expirationTime * 1000)
  }
}

export const authSignup = (username, email, password1, password2) => {
  return dispatch => {
    dispatch(authStart())
    axios.post(config.BACKEND_URL+'/rest-auth/registration/', {
      username: username,
      email: email,
      password1: password1,
      password2: password2
    })
    .then((res) => {
      const token = res.data.key
      const expirationDate = new Date(new Date().getTime() + 3600 * 1000) // one hour
      localStorage.setItem('token', token)
      localStorage.setItem('email', email)
      localStorage.setItem('expirationDate', expirationDate)
      dispatch(authSuccess(token))
      dispatch(checkAuthTimeout(3600))
    })
    .catch((err) => {
      console.log(err.response.data)
      console.log(err)
      dispatch(authFail(err))
    })
  }
}

export const authCheckState = () => {
  return dispatch => {
    const token = localStorage.getItem('token')
    if (token === undefined) {
      dispatch(authLogout())
    } else {
      const expirationDate = new Date(localStorage.getItem('expirationDate'))
      if (expirationDate <= new Date()) {
        dispatch(authLogout())
      } else {
        dispatch(authSuccess(token)) // need to fix this probably
        dispatch(checkAuthTimeout((expirationDate.getTime() - new Date().getTime()) / 1000))
      }
    }
  }
}