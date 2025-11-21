package com.clinica.project.domain.service;

import com.clinica.project.infrastructure.model.Cita;
import com.clinica.project.infrastructure.repository.CitaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class CitaService {
    @Autowired
    private CitaRepository citaRepository;

    public List<Cita> findAll() {
        return citaRepository.findAll();
    }
}