import React, { createContext, useReducer } from 'react'
import clienteReducer from '../reducer/clienteReducer';
import { OBTENER_CLIENTES, REGISTRAR_CLIENTE } from '../const/actionTypes';
import { v4 as uuidv4} from 'uuid';


export const ClienteContext = createContext();

export const ClienteContextProvider = props => {

    const initialState = {
        clientesList: []
    }

    
    const [state, dispatch] = useReducer(clienteReducer, initialState);

    const obtenerClientes = () => {
        const clientes = [
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
        ];
        dispatch({
            type: OBTENER_CLIENTES,
            payload: clientes
        })
    }
    const registrarCliente =  cliente => {

        let clienteNuevo = {
            ...cliente,
            idCliente: uuidv4()
        }
        dispatch({
            type: REGISTRAR_CLIENTE,
            payload: clienteNuevo

        })
    }
    const obtenerCliente = cliente => {
        dispatch({
            type: OBTENER_CLIENTES,
            payload: cliente
        })
    }

    return(
        <ClienteContext.Provider
            value={{
               clientesList: state.clientesList ,
               obtenerClientes,
               registrarCliente
            }}>
                {props.children}
        </ClienteContext.Provider>
    )

}

