import React from 'react';
import ZipForm from './ZipForm'

class App extends React.Component{
    // every componenenet must have a render method , if u want something to print
    render(){
        return <div className="app">
            <p> What seems hard Now, will be warmup one day</p>
            <ZipForm />
        </div> 
    }
 }

 export default App;