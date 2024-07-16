import { createContext, useState } from "react";
import useModal from "./Hooks/useModal";

export const AppContext = createContext();

const Context = ({ children }) => {
    const [modal, handlerOpen, handlerClose] = useModal();
    const [user, setUser] = useState(null);

    const getLoginData = async (e, p) => {
        try {
            const response = await axios.post('token/', {
                username: e,
                password: p,
            });
            localStorage.setItem('token', response.data.access);
            setUser(response.data.user);
            handlerClose();
        } catch (error) {
            console.error(error);
        }
    };

    const value = { modal, handlerOpen, handlerClose, getLoginData, user };

    return (
        <AppContext.Provider value={value}>
            {children}
        </AppContext.Provider>
    );
};

export default Context;
