// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <div>
//         {/* Grab data from backend */}
//         <h1>BB Tech Company</h1>
//       </div>
//     </div>
//   );
// }

// export default App;


import axois from 'axios';
import React from 'react';

class App extends React.Component{
    state = {details: [], }

    componentDidMount(){
        let data;
        axois.get('http://localhost:8000')
        .then(res => {
            data = res.data;
            this.setState({
                details: data
            });
        })
        .catch(err => {})
    }

    render (){
        return (
            <div> 
                <header> Data generated from Django </header>
                <hr></hr>
                {this.state.details.map((output, id) => (
                    <div key = {id}>
                        <div>
                            <h2>{output.employee}</h2>
                            <h3>{output.department}</h3>
                        </div>
                    </div>
                ))}
            </div>
        )
    }
}

export default App;