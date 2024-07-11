import { createContext } from "react"; // Importing createContext to create a context
import useModal from "./Hooks/useModal"; // Importing custom hook for modal state management

export const AppContext = createContext(); // Creating a new context

const Context = ({ children }) => {
    const [modal, handlerOpen, handlerClose] = useModal(); // Destructuring modal state and handlers

    const getLoginData = (e, p) => {
        let userData = {
            email: e,
            password: p
        };
        console.log(userData);
    };

    const value = { modal, handlerOpen, handlerClose, getLoginData }; // Creating context value

    return (
        <AppContext.Provider value={value}>
            {children}
        </AppContext.Provider>
    );
};

export default Context;
