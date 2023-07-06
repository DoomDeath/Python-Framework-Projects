import React from "react";
import Layout from "../components/commons/Layout";
import TablaCliente from "../components/clientes/TableClientes";

const Clientes = () => {
  return (
    <Layout>
      <div className="panel">
        <div className="panel-heading">Clientes</div>
        <div className="box">
          <div className="container">
            <button className="button is-small is-primary">
              <span className="icon is-small">
                <i className="fas fa-plus"></i>
              </span>
              <span>Registrar Nuevo</span>
            </button>
          </div>
          <TablaCliente/>
        </div>
      </div>
    </Layout>
  );
};

export default Clientes;
