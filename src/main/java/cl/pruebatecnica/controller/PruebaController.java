package cl.pruebatecnica.controller;


import cl.pruebatecnica.dto.*;
import cl.pruebatecnica.entity.Phone;
import cl.pruebatecnica.entity.User;
import cl.pruebatecnica.repository.PhoneRepository;
import cl.pruebatecnica.repository.UserRepository;
import cl.pruebatecnica.service.RegisterService;
import cl.pruebatecnica.utils.Utils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/prueba")
@Slf4j
public class PruebaController {

    @Autowired
    private RegisterService registerService;

    @Autowired
    UserRepository userRepository;

    @Autowired
    PhoneRepository phoneRepository;


    @GetMapping("/user/{id}")
    public ResponseEntity<UserResponse> getUserById(@PathVariable Long id) {
        UserResponse userResponse = registerService.getUserById(id);
        if (userResponse == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(userResponse);
    }

    @GetMapping("/users")
    public List<UserResponse> getAllUsers() {
        return registerService.getAllUser();
    }

    @PostMapping("/create")
    public ResponseEntity<?> createUser(@RequestBody UserRequest user) {
        if(!Utils.validarCorreo(user.getEmail())){
            MessageResponse error = new MessageResponse();
            error.setCode(409);
            error.setMessage("correo invalido.");
            return ResponseEntity.status(HttpStatus.CONFLICT).body(error);

        }
        if(!Utils.validarPassword(user.getPassword())){
            MessageResponse error = new MessageResponse();
            error.setCode(409);
            error.setMessage("Contraseña invalida.");
            return ResponseEntity.status(HttpStatus.CONFLICT).body(error);
        }
        Optional<UserResponse> optionalUser = Optional.ofNullable(registerService.createUser(user));
        if (optionalUser.isPresent()) {
            UserResponse created = optionalUser.get();
            RegisterResponse registerResponse = new RegisterResponse();
            registerResponse.setId(created.getId());
            registerResponse.setCreated(created.getCreated());
            registerResponse.setModified(created.getModified());
            registerResponse.setToken(created.getToken());
            log.info(registerResponse + "Se a creado usuario");
            return ResponseEntity.status(HttpStatus.CREATED).body(registerResponse);


        } else {
            MessageResponse error = new MessageResponse();
            error.setCode(409);
            error.setMessage("El usuario ya existe en el sistema.");
            log.info(error.getMessage());
            return ResponseEntity.status(HttpStatus.CONFLICT).body(error);
        }
    }



    @PutMapping("/update/{id}")
    public ResponseEntity<?> updateUser(@PathVariable("id") Long id, @RequestBody UserRequest userRequest) {

        if(!Utils.validarCorreo(userRequest.getEmail())){
            MessageResponse error = new MessageResponse();
            error.setCode(409);
            error.setMessage("correo invalido.");
            log.info(error.getMessage());
            return ResponseEntity.status(HttpStatus.CONFLICT).body(error);

        }
        if(!Utils.validarPassword(userRequest.getPassword())){
            MessageResponse error = new MessageResponse();
            error.setCode(409);
            error.setMessage("Contraseña invalida.");
            log.info(error.getMessage());
            return ResponseEntity.status(HttpStatus.CONFLICT).body(error);
        }
        UserResponse updatedUser = registerService.updateUser(userRequest);
        if (updatedUser != null) {
            RegisterResponse registerResponse = new RegisterResponse();
            registerResponse.setId(updatedUser.getId());
            registerResponse.setCreated(updatedUser.getCreated());
            registerResponse.setModified(updatedUser.getModified());
            registerResponse.setToken(updatedUser.getToken());
            return ResponseEntity.ok().body(registerResponse);
        } else {
            MessageResponse error = new MessageResponse();
            error.setCode(404);
            error.setMessage("El usuario no existe");
            log.info(error.getMessage());
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
        }
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<?> deleteUser(@PathVariable("id") Long id) {
        Optional<User> existingUser = userRepository.findById(id);
        if (existingUser.isPresent()) {
            registerService.deleteUser(existingUser.get().getId());
            MessageResponse message = new MessageResponse();
            message.setCode(HttpStatus.OK.value());
            message.setMessage("usuario eliminado correctamente.");
            log.info(message.getMessage());
            return ResponseEntity.status(HttpStatus.OK).body(message);
        } else {
            MessageResponse error = new MessageResponse();
            error.setCode(HttpStatus.NOT_FOUND.value());
            error.setMessage("Usuario no encontrado.");
            log.info(error.getMessage());
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
        }
    }
}




