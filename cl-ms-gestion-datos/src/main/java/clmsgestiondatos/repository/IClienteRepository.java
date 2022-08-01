package clmsgestiondatos.repository;

import com.ventas.ventas.model.Cliente;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * @author freddyar
 */
public interface IClienteRepository extends JpaRepository<Cliente, Integer> {
}
