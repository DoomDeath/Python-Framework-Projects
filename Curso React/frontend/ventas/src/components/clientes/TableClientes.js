import React, { useState } from "react";
import RowClientes from "./RowClientes";


const TablaCliente = () => {

  const [clientesList, setClientesList] = useState([
    {
      "idCliente": "1",
      "nombres": "Gustavo",
      "apellidos": "Burgos",
      "direccion": "El Parron 80",
      "telefono": "931833749",
      "email": "gustavoburgos89@gmail.com"
    },
    {
      "idCliente": "2",
      "nombres": "Gustavo",
      "apellidos": "Burgos",
      "direccion": "El Parron 80",
      "telefono": "931833749",
      "email": "gustavoburgos89@gmail.com"
    },
    {
      "idCliente": "3",
      "nombres": "Gustavo",
      "apellidos": "Burgos",
      "direccion": "El Parron 80",
      "telefono": "931833749",
      "email": "gustavoburgos89@gmail.com"
    },
    {
      "idCliente": "4",
      "nombres": "Gustavo",
      "apellidos": "Burgos",
      "direccion": "El Parron 80",
      "telefono": "931833749",
      "email": "gustavoburgos89@gmail.com"
    }
  ])
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
          {
            clientesList.map(cli => (
              <RowClientes cliente={cli} key={cli.idCliente} />
            ))
          }

        </tbody>
      </table>
    </div>
  );
};

export default TablaCliente;
