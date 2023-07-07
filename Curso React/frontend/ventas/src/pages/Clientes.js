import React from "react";
import Layout from "../components/commons/Layout";
import TablaCliente from "../components/clientes/TableClientes";
import ToolbarCliente from "../components/clientes/ToolbarCliente";
import Modal from "../components/commons/Modal";
import FormCliente from "../components/clientes/FormCliente";

const Clientes = () => {
  return (
    <Layout>
      <div className="panel">
        <div className="panel-heading">Clientes</div>
        <div className="box">
          <ToolbarCliente/>
          <TablaCliente/>
        </div>
      </div>
      <Modal>
        <FormCliente/>
      </Modal>
    </Layout>
  );
};

export default Clientes;
