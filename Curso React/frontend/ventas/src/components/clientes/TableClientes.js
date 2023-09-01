import React, { useContext, useEffect } from "react";
import RowClientes from "./RowClientes";
import { ClienteContext } from "../../contexts/clienteContext";

const TablaCliente = () => {

  const { clientesList, obtenerClientes } = useContext(ClienteContext);



  useEffect(() => {
    obtenerClientes();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (clientesList.length === 0) return <center><p>No Existen Clientes</p></center>
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
