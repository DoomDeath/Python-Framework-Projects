import React, { useContext } from 'react'
import { ModalContext } from '../../contexts/modalContext';


const ToolbarCliente = () => {
  const { setModalTitle, setShowModal } = useContext(ModalContext);

    const abrirModalCrear = () => {
      setModalTitle('Registrar Nuevo Cliente');
      setShowModal(true);
    }


    return ( 
        <div className="container">
            <button className="button is-small is-primary"
            onClick={ () => abrirModalCrear()}>
              <span className="icon is-small">
                <i className="fas fa-plus"></i>
              </span>
              <span>Registrar Nuevo</span>
            </button>
          </div>
    );
}
 
export default ToolbarCliente;