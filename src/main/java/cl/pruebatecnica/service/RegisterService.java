package cl.pruebatecnica.service;

import cl.pruebatecnica.dto.PhoneRequest;
import cl.pruebatecnica.dto.RegisterResponse;
import cl.pruebatecnica.dto.UserRequest;
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

import java.security.SecureRandom;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.*;

@Service
public class RegisterService {

    @Autowired
    UserRepository userRepository;

    @Autowired
    PhoneRepository phoneRepository;

    @Autowired
    ModelMapper modelMapper;

    public User createUser(UserRequest userRequest) {

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
        List<PhoneRequest> phoneRequests = userRequest.getPhones();
        List<Phone> phones = new ArrayList<>();
        for (PhoneRequest phoneRequest : phoneRequests) {
            Phone phone = new Phone();
            phone.setNumber(phoneRequest.getNumber());
            phone.setUser(user);
            phones.add(phone);
        }
        user.setPhones(phones);
        User repository = userRepository.save(user);
        
        return user;
    }
    public RegisterResponse getUser(){
        return null;
    }










}
