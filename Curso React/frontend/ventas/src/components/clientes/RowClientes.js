import React, { useContext } from 'react'
import { ModalContext } from '../../contexts/modalContext';

const RowClientes = ({cliente}) => {

  const { setShowModal, setModalTitle } = useContext(ModalContext);

    const AbrirModalModificarCliente = () => {
        setModalTitle('Modificar Cliente')
        setShowModal(true);
    }
    const eliminarCliente = () => {
      setModalTitle('Eliminar Cliente')
      setShowModal(true);
    }
    return (  
        <tr>
            <td>
              <button className="button is-small is-info mr-1" 
              title="Editar"
              onClick={ () => AbrirModalModificarCliente()}>
                <span className="icon is-small">
                  <i className="fas fa-edit"></i>
                </span>
              </button>
              <button className="button is-small is-danger" title="Eliminar"
              onClick={ () => eliminarCliente()}>
                <span className="icon is-small">
                  <i className="fas fa-trash-alt"></i>
                </span>
              </button>
            </td>
            <td>{cliente.nombres}</td>
            <td>{cliente.apellidos}</td>
            <td>{cliente.direccion}</td>
            <td>{cliente.telefono}</td>
            <td>{cliente.email}</td>
          </tr>
    );
}
 
export default RowClientes;