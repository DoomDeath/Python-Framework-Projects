import { OBTENER_CLIENTES, REGISTRAR_CLIENTE } from "../const/actionTypes";

// eslint-disable-next-line import/no-anonymous-default-export
export default (state, action) => {
  switch (action.type) {
    case OBTENER_CLIENTES:

        return {
            ...state,
            clientesList: action.payload
        };
        case REGISTRAR_CLIENTE:
            return{
              ...state,
              clientesList: [...state.clientesList, action.payload]   
            };
    default:
      return state;
  }
};
