function List(props) {
    return (
      <ul>
        {props.animals.map((animal) => {
          return animal.startsWith("L") && <li key={animal}>{animal}</li>;
        })}
      </ul>
    );
  }
  
  function App() {
    const animals = ["Lion", "Cow", "Snake", "Lizard"];
  
    return (
      <div>
        <h1>Animals: </h1>
        <List animals={animals} />
      </div>
    );
  }