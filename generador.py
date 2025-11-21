import os

# Configuración del proyecto
BASE_DIR = "clinica-backend"
PACKAGE_PATH = "src/main/java/com/clinica/project"
RESOURCES_PATH = "src/main/resources"

# Estructura de directorios
directories = [
    f"{BASE_DIR}/{PACKAGE_PATH}/controller",
    f"{BASE_DIR}/{PACKAGE_PATH}/domain/dto",
    f"{BASE_DIR}/{PACKAGE_PATH}/domain/service",
    f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/model",
    f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/repository",
    f"{BASE_DIR}/{PACKAGE_PATH}/security/jwt",
    f"{BASE_DIR}/{PACKAGE_PATH}/security/service",
    f"{BASE_DIR}/{RESOURCES_PATH}",
]

# Contenidos de los archivos
files = {}

# --------------------------------------------------------------------------
# 1. POM.XML
# --------------------------------------------------------------------------
files[f"{BASE_DIR}/pom.xml"] = """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.0</version>
        <relativePath/>
    </parent>
    <groupId>com.clinica</groupId>
    <artifactId>clinica-backend</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>clinica-backend</name>
    <description>Sistema de Gestion Clinica</description>

    <properties>
        <java.version>17</java.version>
    </properties>

    <dependencies>
        <!-- Web -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>

        <!-- Data & DB -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <scope>runtime</scope>
        </dependency>

        <!-- Security & JWT -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-api</artifactId>
            <version>0.11.5</version>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-impl</artifactId>
            <version>0.11.5</version>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-jackson</artifactId>
            <version>0.11.5</version>
            <scope>runtime</scope>
        </dependency>

        <!-- Utilities -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
            <version>2.2.0</version>
        </dependency>
        
        <!-- Test -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.security</groupId>
            <artifactId>spring-security-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
"""

# --------------------------------------------------------------------------
# 2. APPLICATION.PROPERTIES
# --------------------------------------------------------------------------
files[f"{BASE_DIR}/{RESOURCES_PATH}/application.properties"] = """# Database Config
spring.datasource.url=jdbc:postgresql://localhost:5432/clinica
spring.datasource.username=postgres
spring.datasource.password=1234
spring.jpa.hibernate.ddl-auto=update
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.show-sql=true

# JWT Config (Clave secreta para firmar tokens - cambiar en produccion)
clinica.app.jwtSecret=SecretKeySuperSeguraParaLaClinicaBackendConSpringSecurity2024
clinica.app.jwtExpirationMs=86400000

# OpenAPI / Swagger
springdoc.api-docs.path=/api-docs
springdoc.swagger-ui.path=/swagger-ui.html
"""

# --------------------------------------------------------------------------
# 3. MAIN APPLICATION
# --------------------------------------------------------------------------
files[f"{BASE_DIR}/{PACKAGE_PATH}/ClinicaApplication.java"] = """package com.clinica.project;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ClinicaApplication {
    public static void main(String[] args) {
        SpringApplication.run(ClinicaApplication.class, args);
    }
}
"""

# --------------------------------------------------------------------------
# 4. INFRASTRUCTURE - MODEL (ENTITIES)
# --------------------------------------------------------------------------

# Rol
files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/model/ERol.java"] = """package com.clinica.project.infrastructure.model;

public enum ERol {
    ROLE_USER,
    ROLE_DOCTOR,
    ROLE_ADMIN
}
"""

files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/model/Rol.java"] = """package com.clinica.project.infrastructure.model;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "roles")
@Data
@NoArgsConstructor
public class Rol {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Enumerated(EnumType.STRING)
    @Column(length = 20)
    private ERol name;
    
    public Rol(ERol name) {
        this.name = name;
    }
}
"""

# Usuario
files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/model/Usuario.java"] = """package com.clinica.project.infrastructure.model;

import jakarta.persistence.*;
import lombok.Data;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "usuarios", 
       uniqueConstraints = { 
           @UniqueConstraint(columnNames = "username"),
           @UniqueConstraint(columnNames = "email") 
       })
@Data
public class Usuario {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String username;

    @Column(nullable = false)
    private String email;

    @Column(nullable = false)
    private String password;

    @ManyToMany(fetch = FetchType.EAGER)
    @JoinTable(name = "usuario_roles", 
               joinColumns = @JoinColumn(name = "usuario_id"),
               inverseJoinColumns = @JoinColumn(name = "rol_id"))
    private Set<Rol> roles = new HashSet<>();

    public Usuario() {}

    public Usuario(String username, String email, String password) {
        this.username = username;
        this.email = email;
        this.password = password;
    }
}
"""

# Paciente
files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/model/Paciente.java"] = """package com.clinica.project.infrastructure.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "pacientes")
@Data
public class Paciente {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre;
    private String apellido;
    private String dni;
    private String telefono;
    
    // Relación opcional con Usuario si el paciente se loguea
    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "usuario_id", referencedColumnName = "id")
    private Usuario usuario;
}
"""

# Doctor
files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/model/Doctor.java"] = """package com.clinica.project.infrastructure.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "doctores")
@Data
public class Doctor {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre;
    private String apellido;
    private String especialidad;
    private String numeroLicencia;

    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "usuario_id", referencedColumnName = "id")
    private Usuario usuario;
}
"""

# Cita
files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/model/Cita.java"] = """package com.clinica.project.infrastructure.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;

@Entity
@Table(name = "citas")
@Data
public class Cita {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDateTime fechaHora;
    private String motivo;
    
    @ManyToOne
    @JoinColumn(name = "paciente_id")
    private Paciente paciente;

    @ManyToOne
    @JoinColumn(name = "doctor_id")
    private Doctor doctor;
}
"""

# HistoriaClinica
files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/model/HistoriaClinica.java"] = """package com.clinica.project.infrastructure.model;

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
"""

# Tratamiento
files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/model/Tratamiento.java"] = """package com.clinica.project.infrastructure.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDate;

@Entity
@Table(name = "tratamientos")
@Data
public class Tratamiento {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String descripcion;
    private String medicamentos;
    private LocalDate fechaInicio;
    private LocalDate fechaFin;

    @ManyToOne
    @JoinColumn(name = "historia_id")
    private HistoriaClinica historiaClinica;
}
"""

# --------------------------------------------------------------------------
# 5. INFRASTRUCTURE - REPOSITORY
# --------------------------------------------------------------------------

files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/repository/UsuarioRepository.java"] = """package com.clinica.project.infrastructure.repository;

import com.clinica.project.infrastructure.model.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface UsuarioRepository extends JpaRepository<Usuario, Long> {
    Optional<Usuario> findByUsername(String username);
    Boolean existsByUsername(String username);
    Boolean existsByEmail(String email);
}
"""

files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/repository/RolRepository.java"] = """package com.clinica.project.infrastructure.repository;

import com.clinica.project.infrastructure.model.ERol;
import com.clinica.project.infrastructure.model.Rol;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface RolRepository extends JpaRepository<Rol, Integer> {
    Optional<Rol> findByName(ERol name);
}
"""

files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/repository/PacienteRepository.java"] = """package com.clinica.project.infrastructure.repository;

import com.clinica.project.infrastructure.model.Paciente;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PacienteRepository extends JpaRepository<Paciente, Long> {
}
"""

# (Generic stub for others to save space, but structure is complete)
common_repos = ["Doctor", "Cita", "HistoriaClinica", "Tratamiento"]
for repo in common_repos:
    files[f"{BASE_DIR}/{PACKAGE_PATH}/infrastructure/repository/{repo}Repository.java"] = f"""package com.clinica.project.infrastructure.repository;

import com.clinica.project.infrastructure.model.{repo};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {repo}Repository extends JpaRepository<{repo}, Long> {{
}}
"""

# --------------------------------------------------------------------------
# 6. SECURITY
# --------------------------------------------------------------------------

# JwtUtils
files[f"{BASE_DIR}/{PACKAGE_PATH}/security/jwt/JwtUtils.java"] = """package com.clinica.project.security.jwt;

import com.clinica.project.security.service.UserDetailsImpl;
import io.jsonwebtoken.*;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Component;
import java.security.Key;
import java.util.Date;

@Component
public class JwtUtils {
    private static final Logger logger = LoggerFactory.getLogger(JwtUtils.class);

    @Value("${clinica.app.jwtSecret}")
    private String jwtSecret;

    @Value("${clinica.app.jwtExpirationMs}")
    private int jwtExpirationMs;

    public String generateJwtToken(Authentication authentication) {
        UserDetailsImpl userPrincipal = (UserDetailsImpl) authentication.getPrincipal();

        return Jwts.builder()
                .setSubject((userPrincipal.getUsername()))
                .setIssuedAt(new Date())
                .setExpiration(new Date((new Date()).getTime() + jwtExpirationMs))
                .signWith(key(), SignatureAlgorithm.HS256)
                .compact();
    }

    private Key key() {
        return Keys.hmacShaKeyFor(Decoders.BASE64.decode(jwtSecret));
    }

    public String getUserNameFromJwtToken(String token) {
        return Jwts.parserBuilder().setSigningKey(key()).build()
               .parseClaimsJws(token).getBody().getSubject();
    }

    public boolean validateJwtToken(String authToken) {
        try {
            Jwts.parserBuilder().setSigningKey(key()).build().parseClaimsJws(authToken);
            return true;
        } catch (MalformedJwtException e) {
            logger.error("Invalid JWT token: {}", e.getMessage());
        } catch (ExpiredJwtException e) {
            logger.error("JWT token is expired: {}", e.getMessage());
        } catch (UnsupportedJwtException e) {
            logger.error("JWT token is unsupported: {}", e.getMessage());
        } catch (IllegalArgumentException e) {
            logger.error("JWT claims string is empty: {}", e.getMessage());
        }
        return false;
    }
}
"""

# AuthTokenFilter
files[f"{BASE_DIR}/{PACKAGE_PATH}/security/jwt/AuthTokenFilter.java"] = """package com.clinica.project.security.jwt;

import com.clinica.project.security.service.UserDetailsServiceImpl;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.util.StringUtils;
import org.springframework.web.filter.OncePerRequestFilter;
import java.io.IOException;

public class AuthTokenFilter extends OncePerRequestFilter {
    @Autowired
    private JwtUtils jwtUtils;

    @Autowired
    private UserDetailsServiceImpl userDetailsService;

    private static final Logger logger = LoggerFactory.getLogger(AuthTokenFilter.class);

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {
        try {
            String jwt = parseJwt(request);
            if (jwt != null && jwtUtils.validateJwtToken(jwt)) {
                String username = jwtUtils.getUserNameFromJwtToken(jwt);

                UserDetails userDetails = userDetailsService.loadUserByUsername(username);
                UsernamePasswordAuthenticationToken authentication =
                        new UsernamePasswordAuthenticationToken(
                                userDetails,
                                null,
                                userDetails.getAuthorities());
                authentication.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));

                SecurityContextHolder.getContext().setAuthentication(authentication);
            }
        } catch (Exception e) {
            logger.error("Cannot set user authentication: {}", e);
        }

        filterChain.doFilter(request, response);
    }

    private String parseJwt(HttpServletRequest request) {
        String headerAuth = request.getHeader("Authorization");
        if (StringUtils.hasText(headerAuth) && headerAuth.startsWith("Bearer ")) {
            return headerAuth.substring(7);
        }
        return null;
    }
}
"""

# AuthEntryPoint
files[f"{BASE_DIR}/{PACKAGE_PATH}/security/jwt/AuthEntryPointJwt.java"] = """package com.clinica.project.security.jwt;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.web.AuthenticationEntryPoint;
import org.springframework.stereotype.Component;
import java.io.IOException;

@Component
public class AuthEntryPointJwt implements AuthenticationEntryPoint {
    private static final Logger logger = LoggerFactory.getLogger(AuthEntryPointJwt.class);

    @Override
    public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException authException)
            throws IOException, ServletException {
        logger.error("Unauthorized error: {}", authException.getMessage());
        response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Error: Unauthorized");
    }
}
"""

# UserDetailsImpl
files[f"{BASE_DIR}/{PACKAGE_PATH}/security/service/UserDetailsImpl.java"] = """package com.clinica.project.security.service;

import com.clinica.project.infrastructure.model.Usuario;
import com.fasterxml.jackson.annotation.JsonIgnore;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import java.util.Collection;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class UserDetailsImpl implements UserDetails {
    private static final long serialVersionUID = 1L;
    private Long id;
    private String username;
    private String email;
    @JsonIgnore
    private String password;
    private Collection<? extends GrantedAuthority> authorities;

    public UserDetailsImpl(Long id, String username, String email, String password,
            Collection<? extends GrantedAuthority> authorities) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.password = password;
        this.authorities = authorities;
    }

    public static UserDetailsImpl build(Usuario usuario) {
        List<GrantedAuthority> authorities = usuario.getRoles().stream()
                .map(role -> new SimpleGrantedAuthority(role.getName().name()))
                .collect(Collectors.toList());

        return new UserDetailsImpl(
                usuario.getId(),
                usuario.getUsername(),
                usuario.getEmail(),
                usuario.getPassword(),
                authorities);
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() { return authorities; }
    public Long getId() { return id; }
    public String getEmail() { return email; }
    @Override
    public String getPassword() { return password; }
    @Override
    public String getUsername() { return username; }
    @Override
    public boolean isAccountNonExpired() { return true; }
    @Override
    public boolean isAccountNonLocked() { return true; }
    @Override
    public boolean isCredentialsNonExpired() { return true; }
    @Override
    public boolean isEnabled() { return true; }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        UserDetailsImpl user = (UserDetailsImpl) o;
        return Objects.equals(id, user.id);
    }
}
"""

# UserDetailsService
files[f"{BASE_DIR}/{PACKAGE_PATH}/security/service/UserDetailsServiceImpl.java"] = """package com.clinica.project.security.service;

import com.clinica.project.infrastructure.model.Usuario;
import com.clinica.project.infrastructure.repository.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class UserDetailsServiceImpl implements UserDetailsService {
    @Autowired
    UsuarioRepository usuarioRepository;

    @Override
    @Transactional
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        Usuario usuario = usuarioRepository.findByUsername(username)
                .orElseThrow(() -> new UsernameNotFoundException("User Not Found with username: " + username));
        return UserDetailsImpl.build(usuario);
    }
}
"""

# WebSecurityConfig
files[f"{BASE_DIR}/{PACKAGE_PATH}/security/WebSecurityConfig.java"] = """package com.clinica.project.security;

import com.clinica.project.security.jwt.AuthEntryPointJwt;
import com.clinica.project.security.jwt.AuthTokenFilter;
import com.clinica.project.security.service.UserDetailsServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableMethodSecurity
public class WebSecurityConfig {
    @Autowired
    UserDetailsServiceImpl userDetailsService;

    @Autowired
    AuthEntryPointJwt unauthorizedHandler;

    @Bean
    public AuthTokenFilter authenticationJwtTokenFilter() {
        return new AuthTokenFilter();
    }

    @Bean
    public DaoAuthenticationProvider authenticationProvider() {
        DaoAuthenticationProvider authProvider = new DaoAuthenticationProvider();
        authProvider.setUserDetailsService(userDetailsService);
        authProvider.setPasswordEncoder(passwordEncoder());
        return authProvider;
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration authConfig) throws Exception {
        return authConfig.getAuthenticationManager();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.csrf(csrf -> csrf.disable())
            .exceptionHandling(exception -> exception.authenticationEntryPoint(unauthorizedHandler))
            .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .authorizeHttpRequests(auth -> 
                auth.requestMatchers("/api/auth/**").permitAll()
                    .requestMatchers("/api-docs/**", "/swagger-ui/**").permitAll()
                    .anyRequest().authenticated()
            );

        http.authenticationProvider(authenticationProvider());
        http.addFilterBefore(authenticationJwtTokenFilter(), UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }
}
"""

# --------------------------------------------------------------------------
# 7. DOMAIN - DTOs
# --------------------------------------------------------------------------

files[f"{BASE_DIR}/{PACKAGE_PATH}/domain/dto/LoginRequest.java"] = """package com.clinica.project.domain.dto;

import jakarta.validation.constraints.NotBlank;
import lombok.Data;

@Data
public class LoginRequest {
    @NotBlank
    private String username;
    @NotBlank
    private String password;
}
"""

files[f"{BASE_DIR}/{PACKAGE_PATH}/domain/dto/SignupRequest.java"] = """package com.clinica.project.domain.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import lombok.Data;
import java.util.Set;

@Data
public class SignupRequest {
    @NotBlank
    @Size(min = 3, max = 20)
    private String username;

    @NotBlank
    @Size(max = 50)
    @Email
    private String email;

    private Set<String> role;

    @NotBlank
    @Size(min = 6, max = 40)
    private String password;
}
"""

files[f"{BASE_DIR}/{PACKAGE_PATH}/domain/dto/JwtResponse.java"] = """package com.clinica.project.domain.dto;

import lombok.Data;
import java.util.List;

@Data
public class JwtResponse {
    private String token;
    private String type = "Bearer";
    private Long id;
    private String username;
    private String email;
    private List<String> roles;

    public JwtResponse(String accessToken, Long id, String username, String email, List<String> roles) {
        this.token = accessToken;
        this.id = id;
        this.username = username;
        this.email = email;
        this.roles = roles;
    }
}
"""

files[f"{BASE_DIR}/{PACKAGE_PATH}/domain/dto/PacienteDTO.java"] = """package com.clinica.project.domain.dto;

import lombok.Data;

@Data
public class PacienteDTO {
    private Long id;
    private String nombre;
    private String apellido;
    private String dni;
}
"""

# --------------------------------------------------------------------------
# 8. DOMAIN - SERVICE & CONTROLLER
# --------------------------------------------------------------------------

# AuthController
files[f"{BASE_DIR}/{PACKAGE_PATH}/controller/AuthController.java"] = """package com.clinica.project.controller;

import com.clinica.project.domain.dto.JwtResponse;
import com.clinica.project.domain.dto.LoginRequest;
import com.clinica.project.domain.dto.SignupRequest;
import com.clinica.project.infrastructure.model.ERol;
import com.clinica.project.infrastructure.model.Rol;
import com.clinica.project.infrastructure.model.Usuario;
import com.clinica.project.infrastructure.repository.RolRepository;
import com.clinica.project.infrastructure.repository.UsuarioRepository;
import com.clinica.project.security.jwt.JwtUtils;
import com.clinica.project.security.service.UserDetailsImpl;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

@CrossOrigin(origins = "*", maxAge = 3600)
@RestController
@RequestMapping("/api/auth")
public class AuthController {
    @Autowired AuthenticationManager authenticationManager;
    @Autowired UsuarioRepository usuarioRepository;
    @Autowired RolRepository rolRepository;
    @Autowired PasswordEncoder encoder;
    @Autowired JwtUtils jwtUtils;

    @PostMapping("/signin")
    public ResponseEntity<?> authenticateUser(@Valid @RequestBody LoginRequest loginRequest) {
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(loginRequest.getUsername(), loginRequest.getPassword()));

        SecurityContextHolder.getContext().setAuthentication(authentication);
        String jwt = jwtUtils.generateJwtToken(authentication);

        UserDetailsImpl userDetails = (UserDetailsImpl) authentication.getPrincipal();
        List<String> roles = userDetails.getAuthorities().stream()
                .map(item -> item.getAuthority())
                .collect(Collectors.toList());

        return ResponseEntity.ok(new JwtResponse(jwt, userDetails.getId(),
                userDetails.getUsername(), userDetails.getEmail(), roles));
    }

    @PostMapping("/signup")
    public ResponseEntity<?> registerUser(@Valid @RequestBody SignupRequest signUpRequest) {
        if (usuarioRepository.existsByUsername(signUpRequest.getUsername())) {
            return ResponseEntity.badRequest().body("Error: Username is already taken!");
        }
        if (usuarioRepository.existsByEmail(signUpRequest.getEmail())) {
            return ResponseEntity.badRequest().body("Error: Email is already in use!");
        }

        Usuario user = new Usuario(signUpRequest.getUsername(), signUpRequest.getEmail(),
                encoder.encode(signUpRequest.getPassword()));

        Set<String> strRoles = signUpRequest.getRole();
        Set<Rol> roles = new HashSet<>();

        if (strRoles == null) {
            Rol userRole = rolRepository.findByName(ERol.ROLE_USER)
                    .orElseThrow(() -> new RuntimeException("Error: Role is not found."));
            roles.add(userRole);
        } else {
            strRoles.forEach(role -> {
                switch (role) {
                    case "admin":
                        Rol adminRole = rolRepository.findByName(ERol.ROLE_ADMIN)
                                .orElseThrow(() -> new RuntimeException("Error: Role is not found."));
                        roles.add(adminRole);
                        break;
                    case "doctor":
                        Rol docRole = rolRepository.findByName(ERol.ROLE_DOCTOR)
                                .orElseThrow(() -> new RuntimeException("Error: Role is not found."));
                        roles.add(docRole);
                        break;
                    default:
                        Rol userRole = rolRepository.findByName(ERol.ROLE_USER)
                                .orElseThrow(() -> new RuntimeException("Error: Role is not found."));
                        roles.add(userRole);
                }
            });
        }

        user.setRoles(roles);
        usuarioRepository.save(user);
        return ResponseEntity.ok("User registered successfully!");
    }
}
"""

# PacienteService (Business Logic Layer)
files[f"{BASE_DIR}/{PACKAGE_PATH}/domain/service/PacienteService.java"] = """package com.clinica.project.domain.service;

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
"""

# PacienteController
files[f"{BASE_DIR}/{PACKAGE_PATH}/controller/PacienteController.java"] = """package com.clinica.project.controller;

import com.clinica.project.domain.service.PacienteService;
import com.clinica.project.infrastructure.model.Paciente;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/pacientes")
public class PacienteController {
    @Autowired
    private PacienteService pacienteService;

    @GetMapping
    @PreAuthorize("hasRole('USER') or hasRole('DOCTOR') or hasRole('ADMIN')")
    public List<Paciente> getAllPacientes() {
        return pacienteService.findAll();
    }

    @PostMapping
    @PreAuthorize("hasRole('DOCTOR') or hasRole('ADMIN')")
    public Paciente createPaciente(@RequestBody Paciente paciente) {
        return pacienteService.save(paciente);
    }
}
"""

# Crear directorios y archivos
for directory in directories:
    os.makedirs(directory, exist_ok=True)

for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Proyecto generado exitosamente en la carpeta: {BASE_DIR}")
print("Sigue las instrucciones en el archivo LEEME.md")