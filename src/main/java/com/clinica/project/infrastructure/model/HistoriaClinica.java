package com.clinica.project.infrastructure.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDate;

@Entity
@Table(name = "historias_clinicas")
@Data
public class HistoriaClinica {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDate fechaCreacion;
    private String diagnostico;
    private String observaciones;

    @ManyToOne
    @JoinColumn(name = "paciente_id")
    private Paciente paciente;
}
