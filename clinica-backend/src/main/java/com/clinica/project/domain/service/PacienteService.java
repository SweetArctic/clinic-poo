package com.clinica.project.domain.service;

import com.clinica.project.infrastructure.model.Paciente;
import com.clinica.project.infrastructure.repository.PacienteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class PacienteService {
    @Autowired
    private PacienteRepository pacienteRepository;

    public List<Paciente> findAll() {
        return pacienteRepository.findAll();
    }

    public Paciente save(Paciente paciente) {
        return pacienteRepository.save(paciente);
    }
}
