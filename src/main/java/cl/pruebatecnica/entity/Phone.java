package cl.pruebatecnica.entity;

import lombok.Data;

import javax.persistence.*;
import java.util.List;

@Entity
@Table(name = "phones")
@Data
public class Phone {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String number ;

    @Column(nullable = false)
    private String email;
}