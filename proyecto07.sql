-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-09-2025 a las 18:12:38
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto07`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idusuario` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `contrasena` varchar(128) NOT NULL,
  `foto` varchar(25) NOT NULL,
  `inactivo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idusuario`, `nombre`, `contrasena`, `foto`, `inactivo`) VALUES
('31311616', 'Vicentico 1', 'bb3f2505c0acec46c6a16ec89bdae3f760fbffa290177d17948541b57d4a629f20f4c3962b9f2890790342d316fcbc9481a6030f84f5b7f09e258df03053047c', '31311616.jpg', 0),
('acortez', 'Adriana Cortez', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 'acortez.jpg', 0),
('afvelasco', 'Andres Velasco', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 'afvelasco.bmp', 0),
('antonio ', 'antoñito crack gameryt', '3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2', 'antonio .jfif', 0),
('bvhrhc', 'samu', '617efa321777984509180436af66e89d96cf476a2e0c24ecb13857ed89f133924693e27ccc0161eac882dcad62771a138ad88fb1d62050298c90ba302fdc38d0', 'bvhrhc.PNG', 0),
('dfgdfgdf', 'dsfsdfs', 'f38a3b5aa7c40c4ecf03bc895fc7fac9d51bbf3cc0aabc27d53b9c56896bcf8d294ebdc2d7f9a34516e55c06663d6a4b3c380ee326be1d1a2ea1eb4e0602b94b', 'dfgdfgdf.png', 0),
('Ftte', 'Felipe', '0dd3e512642c97ca3f747f9a76e374fbda73f9292823c0313be9d78add7cdd8f72235af0c553dd26797e78e1854edee0ae002f8aba074b066dfce1af114e32f8', 'Ftte.jpeg', 0),
('hello_world', 'hola_mundo', 'ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413', 'hello_world.jpg', 0),
('hola', 'Arrozconleche', 'abed9a8611d6b64ecc50766ac87a766816b738d4097d1b897c5f73b99640fffd9687b00650be54056b65940fed60674c1a377b53d4d28e1b450e2837ea0b6f42', 'hola.jpeg', 0),
('juane', 'Juan', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 'juane.jpg', 0),
('Mdv', 'Monica', 'ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413', 'Mdv.jfif', 0),
('migdonio', 'migodnio Goat pro777', '3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2', 'migdonio.png', 0),
('ñiñin', 'ñiñin', 'ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413', 'ñiñin.jpg', 0),
('saml', 'santiago alexander mejia leiton', '3b90acfa12692d6730dab578f8224480f9096355612a232ac84dd0b941cd69316a828208e802c19ee037bdbe61b62f880db9bc7dd2d51976f79accf555e1f713', 'saml.jpg', 0),
('vivasandres', 'Andres Felipe Vivas', 'ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413', 'vivasandres.png', 0),
('wesoto', 'wilson', 'ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413', 'wesoto.jpg', 0),
('yaperdio', 'Yamileth Perdomo Diosa', 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db', 'yaperdio.bmp', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idusuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
