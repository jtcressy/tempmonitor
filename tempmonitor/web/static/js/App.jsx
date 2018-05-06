// App.jsx
import React from "react";
import ReactDOM from "react-dom";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import RaisedButton from "material-ui/RaisedButton";

export default class App extends React.Component {
  render () {
      return (
      <MuiThemeProvider>
          <p> Hello React!</p>
          <RaisedButton label="default"/>
      </MuiThemeProvider>
  );
  }
}

