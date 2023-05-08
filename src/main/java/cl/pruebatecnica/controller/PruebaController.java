package cl.pruebatecnica.controller;


import cl.pruebatecnica.dto.*;
import cl.pruebatecnica.entity.Phone;
import cl.pruebatecnica.entity.User;
import cl.pruebatecnica.repository.PhoneRepository;
import cl.pruebatecnica.repository.UserRepository;
import cl.pruebatecnica.service.RegisterService;
import cl.pruebatecnica.service.UpdateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/prueba")
public class PruebaController {

    @Autowired
    private RegisterService registerService;

    @Autowired
    UserRepository userRepository;

    @Autowired
    PhoneRepository phoneRepository;

    @Autowired
    UpdateService updateService;

    @GetMapping
    public List<RegisterResponse> getUser() {
        List<User> users = this.userRepository.findAll();
        List<RegisterResponse> responses = new ArrayList<>();
        for (User user : users) {
            List<Phone> phones = user.getPhones();
            List<String> phoneNumbers = new ArrayList<>();
            for (Phone phone : phones) {
                phoneNumbers.add(phone.getNumber());
            }
            RegisterResponse response = new RegisterResponse(user.getId(), user.getCreated(), user.getModified(), user.getToken(), user.getName(), user.getEmail(), phoneNumbers);
            responses.add(response);
        }
        return responses;
    }

    @GetMapping("/phones")
    public List<Phone> getAllPhones() {
        return phoneRepository.findAll();
    }


    @PostMapping
    public ResponseEntity<?> createUser(@RequestBody UserRequest user) {
        Optional<User> optionalUser = Optional.ofNullable(registerService.createUser(user));
        if (optionalUser.isPresent()) {
            User created = optionalUser.get();
            RegisterResponse registerResponse = new RegisterResponse();
            registerResponse.setId(created.getId());
            registerResponse.setCreated(created.getCreated());
            registerResponse.setModified(created.getModified());
            registerResponse.setToken(created.getToken());
            return ResponseEntity.status(HttpStatus.CREATED).body(registerResponse);
        } else {
            ErrorResponse error = new ErrorResponse();
            error.setCode(409);
            error.setMessage("El usuario ya existe en el sistema.");
            return ResponseEntity.status(HttpStatus.CONFLICT).body(error);
        }
    }

    /*@GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return userRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("User", "id", id));
    }*/

    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user){
        updateService.
        User existingUser = userRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("User", "id", id));
        existingUser.setName(user.getName());
        existingUser.setEmail(user.getEmail());
        // actualizar otros atributos
        return userRepository.save(existingUser);
    }

    /*@DeleteMapping("/{id}")
    public ResponseEntity<?> deleteUser(@PathVariable Long id) {
        User existingUser = userRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("User", "id", id));
        userRepository.delete(existingUser);
        return ResponseEntity.ok().build();
    }*/




