import React, { Component, useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function MFSubStr(){
  const {mf_sub_str} = useParams()
  const [data, setData] = useState([]);

  const apiGet = () => {
    fetch(`http://127.0.0.1:8000/get-mfname/${mf_sub_str}`)
    .then((response) => response.json())
    .then((json) => {
      console.log(json);
      setData(json);
    });
  }

  return(
    <div>
     {this.props.match.params} <br />
      <button onClick={apiGet}>search for mf</button>
      <br />

      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default MFSubStr;