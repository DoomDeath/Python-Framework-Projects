import React from "react";

const TablaCliente = () => {
  return (
    <div className="table-container">
      <table className="table is-striped is-fullwidth">
        <thead>
          <tr>
            <th>Acciones</th>
            <th>Nombres</th>
            <th>Apellidos</th>
            <th>Direccion</th>
            <th>Telefono</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <button className="button is-small is-info mr-1" title="Editar">
                <span className="icon is-small">
                  <i className="fas fa-edit"></i>
                </span>
              </button>
              <button className="button is-small is-danger" title="Eliminar">
                <span className="icon is-small">
                  <i className="fas fa-trash-alt"></i>
                </span>
              </button>
            </td>
            <td>Gustavo</td>
            <td>Burgos</td>
            <td>El Parron 80</td>
            <td>931833749</td>
            <td>gustavoburgos89@gmail.com</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default TablaCliente;
