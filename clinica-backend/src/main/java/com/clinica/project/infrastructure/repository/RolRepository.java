package com.clinica.project.infrastructure.repository;

import com.clinica.project.infrastructure.model.ERol;
import com.clinica.project.infrastructure.model.Rol;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface RolRepository extends JpaRepository<Rol, Integer> {
    Optional<Rol> findByName(ERol name);
}
