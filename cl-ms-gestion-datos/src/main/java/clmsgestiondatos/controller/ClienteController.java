package clmsgestiondatos.controller;

import com.ventas.ventas.model.Cliente;
import com.ventas.ventas.service.ClienteService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

/**
 * @author freddyar
 */
@RestController
@RequestMapping("/api/clientes")
public class ClienteController {

    @Autowired
    private ClienteService clienteService;

    @Operation(summary = "Obtiene todos los clientes")
    @GetMapping
    public ResponseEntity<List<Cliente>> findAll() {
        return ResponseEntity.ok(clienteService.findAll());
    }

    @Operation(summary = "Obtiene un cliente por su ID")
    @GetMapping("/{id}")
    public ResponseEntity<Cliente> findById(
            @Parameter(description = "Identificador del cliente que desea obtener")
            @PathVariable("id") Integer idCliente) {
        return clienteService.findById(idCliente)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @Operation(summary = "Realiza la creación de un cliente")
    @PostMapping
    public ResponseEntity<Cliente> create(@Valid @RequestBody Cliente cliente) {
        return new ResponseEntity<>(clienteService.create(cliente), HttpStatus.CREATED);
    }

    @Operation(summary = "Modifica un cliente")
    @PutMapping
    public ResponseEntity<Cliente> update(@Valid @RequestBody Cliente cliente) {
        return clienteService.findById(cliente.getIdCliente())
                .map(c -> ResponseEntity.ok(clienteService.update(cliente)))
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @Operation(summary = "Elimina un cliente")
    @DeleteMapping("/{id}")
    public ResponseEntity<Cliente> delete(
            @Parameter(description = "Identificador del cliente que desea eliminar")
            @PathVariable("id") Integer idCliente) {
        return clienteService.findById(idCliente)
                .map(c -> {
                    clienteService.delete(idCliente);
                    return ResponseEntity.ok(c);
                })
                .orElseGet(() -> ResponseEntity.notFound().build());
    }
}
