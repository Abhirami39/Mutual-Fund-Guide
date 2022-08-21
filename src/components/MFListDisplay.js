import React, {useState} from 'react';

function MFListDisplay(){
  const [data, setData] = useState([]);

  const apiGet = () => {
    fetch("http://127.0.0.1:8000/get-all-mf/")
    .then((response) => {
      //console.log(response);
      return response.json()
    })
    .then((json) => {
      console.log(json.names);
      setData(json.names);
    });
  }

  const [mfDetails, setMfDetails] = useState([]);
  
  const get_details = (mf_name) =>{
    //console.log(event);
    //var mf_name = event.target.innerText
    console.log(mf_name);
    const url = `http://127.0.0.1:8000/get-mf-deets/${mf_name}`
    //const url = "http://127.0.0.1:8000/get-mf-deets/ICICI%20Prudential%20Value%20Discovery%20Fund%20%20-%20Growth"
    
    fetch(url)
    .then((response) => {
      //console.log(response);
      return response.json()
    })
    .then((json_mf_detail) => {
      console.log(json_mf_detail.mf_details_dict);
      setMfDetails(json_mf_detail.mf_details_dict);
    });
  }

  //console.log(Object.keys(mfDetails));

  const result = Object.entries(mfDetails).map(([key, value]) => {
    // console.log(key);
    // console.log(value);
  
    return {[key]: value};
  });
  
  console.log(result);

  return(
    <div>
      MY API <br />
      <button onClick={apiGet}>get list of MFs</button>
      <br />

      if(data == null){
        <ul>
          {data.map((mf_each) => 
            <li><a onClick={() => get_details(mf_each)} style={{cursor: 'pointer'}}>{mf_each}</a></li>
          )}
        </ul>
      }

      if(mfDetails){
        // <ul>
        //   {mfDetails.map(([each_detail_name, each_detail]) => 
        //     <li>{each_detail_name} : {each_detail}</li>
        //   )}
        // </ul>
        <ul>
        {
          Object.entries(mfDetails)
          .map( ([key, value]) => <li>{key} : {value}</li> )
        }
        </ul>
      }
      
    </div>
  );
}

export default MFListDisplay;