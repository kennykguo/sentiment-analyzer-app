// frontend/src/Hooks/useModal.js
import { useState } from "react";

export default function useModal() {
    const [modal, setModal] = useState(null); // State for modal visibility

    const handlerOpen = () => {
        setModal(true); // Open modal
    };
    
    const handlerClose = () => {
        setModal(null); // Close modal
    };

    return [
        modal, handlerOpen, handlerClose // Return modal state and handlers
    ];
}
