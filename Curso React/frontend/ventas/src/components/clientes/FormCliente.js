import React, { useContext, useState } from "react";
import { ModalContext } from "../../contexts/modal/modalContext";

const FormCliente = () => {
  const clienteDefault = {
    nombres: "",
    apellidos: "",
    direccion: "",
    telefono: "",
    email: "",
  };

  const { setShowModal } = useContext(ModalContext);

  const [cliente, setCliente] = useState(clienteDefault);
  const [mensaje, setMensaje] = useState(null);

  const handleOnSubmit = (e) => {
    e.preventDefault();
    if( cliente.nombres === '' && cliente.apellidos === '' && cliente.email === ''){
        setMensaje("el nombre, apellido y el email son requeridos");
        return;

    }
    limpiarForm();
    cerrarModal();
    console.log(obtenerClienteAEnviar());
  };

  const limpiarForm = () => {
    setMensaje(null);
    setCliente(clienteDefault);
  }
  const handleChange = (e) => {
    setCliente({
      ...cliente,
      [e.target.name]: e.target.value,
    });
  };

  const cerrarModal = () => {
    limpiarForm();
    setShowModal(false);
    
  }
  const obtenerClienteAEnviar = () => {
    let clienteTemp =  {...cliente};
    if(clienteTemp.direccion === "") delete clienteTemp.direccion;
    if(clienteTemp.telefono === "") delete clienteTemp.telefono;
    return clienteTemp
  }

  return (
    <form onSubmit={handleOnSubmit}>
        { mensaje ? <div className="notification is-danger">{mensaje}</div> : null}
      <div className="field is-horizontal">
        <div className="field-label is-normal">
          <label className="label">Nombre Completo</label>
        </div>
        <div className="field-body">
          <div className="field">
            <p className="control has-icons-left has-icons-right">
              <input className="input" type="text" placeholder="Nombres"
              name="nombres"
              value={cliente.nombres}
              onChange={handleChange} />
              <span className="icon is-small is-left">
                <i className="fas fa-user"></i>
              </span>
            </p>
          </div>
          <div className="field">
            <input className="input" type="text" placeholder="Apellidos"
            name="apellidos"
            value={cliente.apellidos}
            onChange={handleChange} />
          </div>
        </div>
      </div>
      <div className="field is-horizontal">
        <div className="field-label is-normal">
          <label className="label">Dirección</label>
        </div>
        <div className="field-body">
          <div className="field">
            <div className="control has-icons-left has-icons-right">
              <input
                className="input"
                type="text"
                placeholder="Ingrese su dirección"
                name="direccion"
                value={cliente.direccion}
                onChange={handleChange}
              />
              <span className="icon is-small is-left">
                <i className="fa-solid fa-map-location-dot"></i>
              </span>
            </div>
          </div>
        </div>
      </div>
      <div className="field is-horizontal">
        <div className="field-label is-normal">
          <label className="label">Telefono</label>
        </div>
        <div className="field-body">
          <div className="field is-expanded">
            <div className="field has-addons">
              <p className="control">
                <a className="button is-static">+56 9</a>
              </p>
              <p className="control is-expanded">
                <input
                  className="input"
                  type="tel"
                  placeholder="Your phone number"
                  name="telefono"
                  value={cliente.telefono}
                  onChange={handleChange}
                />
              </p>
            </div>
          </div>
        </div>
      </div>
      <div className="field is-horizontal">
        <div className="field-label is-normal">
          <label className="label">Email</label>
        </div>
        <div className="field-body">
          <div className="field">
            <div className="control has-icons-left has-icons-right">
              <input className="input" type="email" placeholder="Email"
              name="email"
              value={cliente.email}
              onChange={handleChange} />
              <span className="icon is-small is-left">
                <i className="fa-solid fa-envelope"></i>
              </span>
            </div>
          </div>
        </div>
      </div>

      <div className="field is-horizontal">
        <div className="field-label is-normal">
          <label className="label"></label>
        </div>
        <div className="field-body">
          <div className="field is-grouped">
            <p className="control">
              <button className="button is-primary mr-1" type="submit">
                Guardar
              </button>
            </p>
            <p className="control">
              <button className="button is-light"
               type="button"
               onClick={ () => cerrarModal() }>
                Cancelar
              </button>
            </p>
          </div>
        </div>
      </div>
    </form>
  );
};

export default FormCliente;
