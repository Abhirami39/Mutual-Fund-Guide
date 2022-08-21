import React, { Component, useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function MFDetails(){
  const {mf_name} = useParams()
  const [data, setData] = useState([]);

  const apiGet = () => {
    fetch(`http://127.0.0.1:8000/get-mf-deets/${mf_name}`)
    .then((response) => response.json())
    .then((json) => {
      console.log(json);
      setData(json);
    });
  }

  return(
    <div>
      MY API <br />
      <button onClick={apiGet}>get mf details</button>
      <br />

      <pre>{JSON.stringify(data, null, 2)}</pre>
      {/* <a href='http://127.0.0.1:8000/get-mf-deets/ICICI%20Prudential%20Value%20Discovery%20Fund%20%20-%20Growth'>ICICI Prudential Value Discovery Fund  - Growth</a> */}
    </div>
  );
}

export default MFDetails;