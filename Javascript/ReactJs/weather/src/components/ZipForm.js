import React from 'react';

//classname must be same as filename
class ZipForm extends React.Component{
    render(){
        return <div className='zip-form'>
        <form>
            <label  htmlFor="zipcode">Zip Code</label>
            <input 
                className="form-control"
                type="input"
                name = "zipcode" />
            <button type="submit" className="btn btn-success">Get the forcast </button>
        </form>
        </div>
    }
}

export default ZipForm;