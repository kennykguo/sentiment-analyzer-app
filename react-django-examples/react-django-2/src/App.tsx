// import './App.css'

// function App() {
//     const apples = [
//         {name: 'Bramley', color: 'red and green', photoUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Bramley%27s_Seedling_Apples.jpg/320px-Bramley%27s_Seedling_Apples.jpg'},
//         {name: 'Cox Orange Renette', color: 'yellow', photoUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Cox_orange_renette2.JPG/320px-Cox_orange_renette2.JPG'},
//         {name: 'Granny Smith', color: 'green', photoUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Granny_smith_closeup.jpg/320px-Granny_smith_closeup.jpg'},
//         {name: 'SugarBee', color: 'red and yellow', photoUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/The_SugarBee_Apple_now_grown_in_Washington_State.jpg/320px-The_SugarBee_Apple_now_grown_in_Washington_State.jpg'},
//     ]

//     return (
//         <>
//             <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">

//                 {apples.map((apple, index) => (
                    
//                     <div className="bg-white rounded-lg shadow-md overflow-hidden" key={index}>

//                         <img
//                             src={apple.photoUrl}
//                             alt={`A beautiful round apple, with a shiny skin, perfect for eating or baking. The ${apple.name} apple has a ${apple.color} color.`}
//                             className="w-full h-48 object-cover"
//                             width="400"
//                             height="300"
//                         />

//                         <div className="p-4">
//                             <h3 className="text-lg font-semibold text-gray-800 mb-2">{apple.name}</h3>
//                             <p className="text-gray-600">Color: {apple.color}</p>
//                         </div>

//                     </div>

//                 ))}

//             </div>
//         </>
//     )
// }

// export default App


import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
    const [apples, setApples] = useState<Apple[]>([])

    interface Apple {
        name: string;
        color: string;
        photo_url: string;
    }

    useEffect(() => {
        const applesListUrl = 'http://localhost:8000/apples/'
        axios.get<Apple[]>(applesListUrl)
            .then(response => setApples(response.data))
    }, [])

    return (
        <>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {apples.map((apple, index) => (
                    <div className="bg-white rounded-lg shadow-md overflow-hidden" key={index}>
                        <img
                            src={apple.photo_url}
                            alt={`${apple.name} apple`}
                            className="w-full h-48 object-cover"
                        />
                        <div className="p-4">
                            <h3 className="text-lg font-semibold text-gray-800 mb-2">{apple.name}</h3>
                            <p className="text-gray-600">Color: {apple.color}</p>
                        </div>
                    </div>
                ))}
            </div>
        </>
    )
}

export default App
