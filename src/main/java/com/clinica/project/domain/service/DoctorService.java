package com.clinica.project.domain.service;

import com.clinica.project.infrastructure.model.Doctor;
import com.clinica.project.infrastructure.repository.DoctorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class DoctorService {
    @Autowired
    private DoctorRepository doctorRepository;

    public List<Doctor> findAll() {
        return doctorRepository.findAll();
    }
}