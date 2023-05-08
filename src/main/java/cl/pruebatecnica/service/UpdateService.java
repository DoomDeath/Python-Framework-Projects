package cl.pruebatecnica.service;

import cl.pruebatecnica.dto.UserRequest;
import cl.pruebatecnica.entity.User;
import cl.pruebatecnica.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;

public class UpdateService {

    @Autowired
    UserRepository userRepository;

    @Autowired
    UserRequest userRequest;

    public User updateUser(Long id, UserRequest userRequest) {
        User existingUser = userRepository.findById(id).orElse(null);
        if (existingUser != null) {
            existingUser.setName(userRequest.getName());
            existingUser.setEmail(userRequest.getEmail());
            existingUser.setPassword(userRequest.getPassword());
            existingUser.setPhones(userRequest.getPhones()); // Actualiza los números de teléfono
            return userRepository.save(existingUser);
        } else {
            return null;
        }
    }
}

