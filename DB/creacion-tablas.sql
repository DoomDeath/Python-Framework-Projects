-- Crear tabla de Usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(60) NOT NULL,
    fecha_registro TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Crear tabla de Perfiles de Seguridad
CREATE TABLE perfiles_seguridad (
    id SERIAL PRIMARY KEY,
    nombre_perfil VARCHAR(50) NOT NULL,
    descripcion TEXT
);

-- Insertar un usuario
INSERT INTO usuarios (nombre_usuario, correo_electronico, contrasena) VALUES ('Usuario1', 'usuario1@example.com', 'contrasena1');

-- Insertar un perfil de usuario
INSERT INTO perfiles_seguridad (nombre_perfil, descripcion) VALUES ('Usuario', 'Rol de usuario estándar');

-- Insertar un perfil de moderador
INSERT INTO perfiles_seguridad (nombre_perfil, descripcion) VALUES ('Moderador', 'Rol de moderador con permisos adicionales');

-- Crear tabla de Asignación de Perfiles a Usuarios
CREATE TABLE asignacion_perfiles (
    usuario_id INT NOT NULL,
    perfil_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (perfil_id) REFERENCES perfiles_seguridad(id)
);

-- Asignar el perfil de "Usuario" al usuario 1
INSERT INTO asignacion_perfiles (usuario_id, perfil_id) VALUES (1, 1);

-- Asignar el perfil de "Moderador" al usuario 2
INSERT INTO asignacion_perfiles (usuario_id, perfil_id) VALUES (2, 2);