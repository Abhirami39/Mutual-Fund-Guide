// import logo from './logo.svg';
// import './App.css';
import React from "react";
import ReactDOM from 'react-dom';
import MFListDisplay from "./components/MFListDisplay";
import { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  BrowserRouter,
  Routes
} from "react-router-dom"
import MFDetails from "./components/MFDetails";
import MFSubStr from "./components/MFSubStr";

function App() {
  // root.render(<MFDetails/>);
  //root.render(<MFListDisplay></MFListDisplay>)
  //root.render(<MFSubStr/>)

  return(
    <BrowserRouter>
      <Routes>
        <Route path = "/" element = {<MFListDisplay/>} />
        <Route path = "/get-mf-deets/:mf_name" element = {<MFDetails/>} />
        <Route path = "/get-mfname/:sub_str_mfname" element = {<MFSubStr/>} />
      </Routes>
    </BrowserRouter>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

export default App;
