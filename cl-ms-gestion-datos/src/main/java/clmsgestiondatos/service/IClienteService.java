package clmsgestiondatos.service;

import com.ventas.ventas.model.Cliente;

import java.util.List;
import java.util.Optional;

/**
 * @author freddyar
 */
public interface IClienteService {

    List<Cliente> findAll();

    Optional<Cliente> findById(Integer id);

    Cliente create(Cliente cliente);

    Cliente update(Cliente cliente);

    void delete(Integer id);
}
