package cl.pruebatecnica.service;

import cl.pruebatecnica.dto.*;
import cl.pruebatecnica.entity.Phone;
import cl.pruebatecnica.entity.User;
import cl.pruebatecnica.repository.PhoneRepository;
import cl.pruebatecnica.repository.UserRepository;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.io.Encoders;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.security.SecureRandom;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class RegisterService {

    @Autowired
    UserRepository userRepository;

    @Autowired
    PhoneRepository phoneRepository;

    @Autowired
    ModelMapper modelMapper;


    public UserResponse getUserById(Long id) {
        Optional<User> user = userRepository.findById(id);
        if (user.isPresent()) {
            UserResponse response = new UserResponse();
            User userDetails = user.get();
            response.setId(userDetails.getId());
            response.setName(userDetails.getName());
            response.setEmail(userDetails.getEmail());
            response.setCreated(userDetails.getCreated());
            response.setModified(userDetails.getModified());
            response.setToken("xxxxxxxxxx");

            // Buscar y agregar teléfonos
            List<Phone> phones = phoneRepository.findByEmail(userDetails.getEmail());
            List<String> phoneNumbers = new ArrayList<>();
            for (Phone phone : phones) {
                phoneNumbers.add(phone.getNumber());
            }
            response.setPhones(phoneNumbers);

            return response;
        } else {
            return null;
        }
    }


    public List<UserResponse> getAllUser() {
        List<User> users = userRepository.findAll();
        List<Phone> phones = phoneRepository.findAll();
        Map<String, List<Phone>> phonesByEmail = new HashMap<>();

        // Agrupar los números de teléfono por correo electrónico
        for (Phone phone : phones) {
            String email = phone.getEmail();
            if (!phonesByEmail.containsKey(email)) {
                phonesByEmail.put(email, new ArrayList<>());
            }
            phonesByEmail.get(email).add(phone);
        }

        // Crear una lista de objetos UserResponse
        List<UserResponse> responses = new ArrayList<>();
        for (User user : users) {
            UserResponse response = new UserResponse();
            response.setId(user.getId());
            response.setToken(user.getToken());
            response.setName(user.getName());
            response.setModified(user.getModified());
            response.setCreated(user.getCreated());

            String email = user.getEmail();
            if (phonesByEmail.containsKey(email)) {
                List<String> phoneNumbers = new ArrayList<>();
                for (Phone phone : phonesByEmail.get(email)) {
                    phoneNumbers.add(phone.getNumber());
                }
                response.setPhones(phoneNumbers);
            }
            responses.add(response);
        }

        return responses;
    }
    public UserResponse createUser(UserRequest userRequest) {
        UserResponse response = new UserResponse();
        // Validar si el usuario ya existe
        Optional<User> existingUser = userRepository.findByEmail(userRequest.getEmail());
        if (existingUser.isPresent()) {
           return null;
        }
        User user = modelMapper.map(userRequest, User.class);
        user.setCreated(LocalDateTime.now());
        user.setModified(LocalDateTime.now());

        SecureRandom secureRandom = new SecureRandom();
        byte[] key = new byte[32];
        secureRandom.nextBytes(key);
        String base64Key = Base64.getEncoder().encodeToString(key);

        // Crear token
        String token = Jwts.builder()
                .setSubject(user.getEmail())
                .setIssuedAt(new Date())
                .setExpiration(Date.from(LocalDateTime.now().plusDays(1).atZone(ZoneId.systemDefault()).toInstant()))
                .signWith(SignatureAlgorithm.HS256, base64Key)
                .compact();
        user.setToken(token);
        User repository = userRepository.save(user);
        List<String> phones = new ArrayList<>();
        List<PhoneRequest> phoneRequests = userRequest.getPhones();
        for (PhoneRequest phoneRequest : phoneRequests) {
            Phone phone = new Phone();
            phone.setNumber(phoneRequest.getNumber());
            phone.setEmail(repository.getEmail());
            phoneRepository.save(phone);
            phones.add(phone.getNumber());

        }
        response.setId(user.getId());
        response.setToken(user.getToken());
        response.setName(user.getName());
        response.setModified(user.getModified());
        response.setCreated(user.getCreated());
        response.setPhones(phones);
        
        return response;
    }
    public UserResponse updateUser(UserRequest userRequest) {
        // Buscar el usuario existente por correo electrónico
        Optional<User> existingUserOptional = userRepository.findByEmail(userRequest.getEmail());
        if (existingUserOptional.isPresent()) {
            User existingUser = existingUserOptional.get();
            // Actualizar los campos del usuario con los valores proporcionados en el JSON
            existingUser.setName(userRequest.getName());
            existingUser.setPassword(userRequest.getPassword());
            existingUser.setModified(LocalDateTime.now());

            // Actualizar los números de teléfono
            List<String> updatedPhones = new ArrayList<>();
            if (userRequest.getPhones() != null) {
                List<Phone> existingPhones = phoneRepository.findByEmail(existingUser.getEmail());
                List<PhoneRequest> updatedPhoneRequests = userRequest.getPhones();
                // Actualizar los números de teléfono existentes
                for (Phone existingPhone : existingPhones) {
                    Optional<PhoneRequest> updatedPhoneOptional = updatedPhoneRequests.stream()
                            .filter(phoneRequest -> phoneRequest.getNumber() != null && phoneRequest.getNumber().equals(existingPhone.getId()))
                            .findFirst();
                    if (updatedPhoneOptional.isPresent()) {
                        PhoneRequest updatedPhoneRequest = updatedPhoneOptional.get();
                        existingPhone.setNumber(updatedPhoneRequest.getNumber());
                        phoneRepository.save(existingPhone);
                        updatedPhones.add(existingPhone.getNumber());
                    } else {
                        // Eliminar los números de teléfono que no se proporcionan en el JSON
                        phoneRepository.delete(existingPhone);
                    }
                }
                // Agregar nuevos números de teléfono
                for (PhoneRequest newPhoneRequest : updatedPhoneRequests) {
                    if (newPhoneRequest.getNumber() == null) {
                        Phone newPhone = new Phone();
                        newPhone.setNumber(newPhoneRequest.getNumber());
                        newPhone.setEmail(existingUser.getEmail());
                        phoneRepository.save(newPhone);
                        updatedPhones.add(newPhone.getNumber());
                    }
                }
            }

            // Guardar el usuario actualizado en la base de datos
            userRepository.save(existingUser);

            // Crear la respuesta
            UserResponse response = new UserResponse();
            response.setId(existingUser.getId());
            response.setToken(existingUser.getToken());
            response.setName(existingUser.getName());
            response.setModified(existingUser.getModified());
            response.setCreated(existingUser.getCreated());
            response.setPhones(updatedPhones);

            return response;
        } else {
            // Si no se encuentra el usuario, retornar null
            return null;
        }
    }

    public boolean deleteUser(Long userId) {
        Optional<User> userOptional = userRepository.findById(userId);
        if (userOptional.isPresent()) {
            User user = userOptional.get();
            List<Phone> phones = phoneRepository.findByEmail(user.getEmail());
            phoneRepository.deleteAll(phones);
            userRepository.delete(user);
            return true;
        }
        return false;
    }


















}
