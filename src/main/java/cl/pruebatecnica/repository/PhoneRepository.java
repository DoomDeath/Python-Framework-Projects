package cl.pruebatecnica.repository;

import cl.pruebatecnica.entity.Phone;
import cl.pruebatecnica.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@EnableJpaRepositories
public interface PhoneRepository extends JpaRepository<Phone, Long> {
    List<Phone> findByUser(User user);
}