import React from "react";
import Layout from "../components/commons/Layout";
import TablaCliente from "../components/clientes/TableClientes";
import ToolbarCliente from "../components/clientes/ToolbarCliente";
import Modal from "../components/commons/Modal";
import FormCliente from "../components/clientes/FormCliente";
import { ClienteContextProvider } from "../contexts/clienteContext";

const Clientes = () => {
  return (
    <Layout>
      <ClienteContextProvider >
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
      </ClienteContextProvider>
    </Layout>
  );
};

export default Clientes;
