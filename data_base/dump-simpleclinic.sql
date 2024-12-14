-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: simpleclinic
-- ------------------------------------------------------
-- Server version	11.6.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `consulta`
--

DROP TABLE IF EXISTS `consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consulta` (
  `ID` int(11) NOT NULL,
  `pacientesID` int(11) NOT NULL,
  `medicaID` int(11) NOT NULL,
  `data` date NOT NULL,
  `Preco` float DEFAULT NULL,
  PRIMARY KEY (`ID`,`pacientesID`,`medicaID`),
  KEY `pacientesID` (`pacientesID`),
  KEY `medicaID` (`medicaID`),
  CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`pacientesID`) REFERENCES `pacientes` (`ID`),
  CONSTRAINT `consulta_ibfk_2` FOREIGN KEY (`medicaID`) REFERENCES `medica` (`EmpregadosID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consulta`
--

LOCK TABLES `consulta` WRITE;
/*!40000 ALTER TABLE `consulta` DISABLE KEYS */;
INSERT INTO `consulta` VALUES (2,2,3,'2024-11-25',NULL),(3,3,3,'2024-11-25',NULL),(4,4,3,'2024-11-25',NULL);
/*!40000 ALTER TABLE `consulta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consultorio`
--

DROP TABLE IF EXISTS `consultorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consultorio` (
  `ID` int(11) NOT NULL,
  `cnpj` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `cnpj` (`cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consultorio`
--

LOCK TABLES `consultorio` WRITE;
/*!40000 ALTER TABLE `consultorio` DISABLE KEYS */;
INSERT INTO `consultorio` VALUES (1,'057.421.548/0001-22');
/*!40000 ALTER TABLE `consultorio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empregados`
--

DROP TABLE IF EXISTS `empregados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empregados` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `Cpf` varchar(100) DEFAULT NULL,
  `Tipo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Cpf` (`Cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empregados`
--

LOCK TABLES `empregados` WRITE;
/*!40000 ALTER TABLE `empregados` DISABLE KEYS */;
INSERT INTO `empregados` VALUES (1,'lucinda rodrigues','11111111111','enfermeira'),(2,'diamantina cruz','22222222222','enfermeira'),(3,'lagaia correia','33333333333','medica');
/*!40000 ALTER TABLE `empregados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enfermeira`
--

DROP TABLE IF EXISTS `enfermeira`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enfermeira` (
  `EmpregadosID` int(11) NOT NULL,
  `coren` varchar(100) NOT NULL,
  PRIMARY KEY (`EmpregadosID`),
  CONSTRAINT `enfermeira_ibfk_1` FOREIGN KEY (`EmpregadosID`) REFERENCES `empregados` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enfermeira`
--

LOCK TABLES `enfermeira` WRITE;
/*!40000 ALTER TABLE `enfermeira` DISABLE KEYS */;
INSERT INTO `enfermeira` VALUES (1,'234567 RS'),(2,'654321 SP');
/*!40000 ALTER TABLE `enfermeira` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lotacao`
--

DROP TABLE IF EXISTS `lotacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lotacao` (
  `enfermeiraID` int(11) NOT NULL,
  `quartosID` int(11) NOT NULL,
  PRIMARY KEY (`enfermeiraID`,`quartosID`),
  KEY `quartosID` (`quartosID`),
  CONSTRAINT `lotacao_ibfk_1` FOREIGN KEY (`enfermeiraID`) REFERENCES `enfermeira` (`EmpregadosID`),
  CONSTRAINT `lotacao_ibfk_2` FOREIGN KEY (`quartosID`) REFERENCES `quartos` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lotacao`
--

LOCK TABLES `lotacao` WRITE;
/*!40000 ALTER TABLE `lotacao` DISABLE KEYS */;
INSERT INTO `lotacao` VALUES (1,1),(1,2),(1,3),(2,4);
/*!40000 ALTER TABLE `lotacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medica`
--

DROP TABLE IF EXISTS `medica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medica` (
  `EmpregadosID` int(11) NOT NULL,
  `crm` varchar(100) NOT NULL,
  `especialidade` varchar(100) NOT NULL,
  PRIMARY KEY (`EmpregadosID`),
  CONSTRAINT `medica_ibfk_1` FOREIGN KEY (`EmpregadosID`) REFERENCES `empregados` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medica`
--

LOCK TABLES `medica` WRITE;
/*!40000 ALTER TABLE `medica` DISABLE KEYS */;
INSERT INTO `medica` VALUES (3,'CRM/RS 876543','Cardiologista');
/*!40000 ALTER TABLE `medica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pacientes`
--

DROP TABLE IF EXISTS `pacientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pacientes` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `Cpf` varchar(100) DEFAULT NULL,
  `Restricoes` varchar(100) DEFAULT NULL,
  `quartosID` int(11) DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Cpf` (`Cpf`),
  KEY `quartosID` (`quartosID`),
  CONSTRAINT `pacientes_ibfk_1` FOREIGN KEY (`quartosID`) REFERENCES `quartos` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pacientes`
--

LOCK TABLES `pacientes` WRITE;
/*!40000 ALTER TABLE `pacientes` DISABLE KEYS */;
INSERT INTO `pacientes` VALUES (1,'arthur carvalho balejo','86868686886','silencio',1,'2000-05-23'),(2,'gabriel cruz','32132132132','alergia ozempic',2,'1997-06-10'),(3,'isabela costa','21321321321',NULL,3,'2002-07-12'),(4,'eduardo zitske','23123123123','alergia coach',4,'2001-08-26');
/*!40000 ALTER TABLE `pacientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quartos`
--

DROP TABLE IF EXISTS `quartos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quartos` (
  `ID` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `consultorioID` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `consultorioID` (`consultorioID`),
  CONSTRAINT `quartos_ibfk_1` FOREIGN KEY (`consultorioID`) REFERENCES `consultorio` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quartos`
--

LOCK TABLES `quartos` WRITE;
/*!40000 ALTER TABLE `quartos` DISABLE KEYS */;
INSERT INTO `quartos` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1),(7,7,1),(8,8,1),(9,9,1),(10,10,1),(11,11,1),(12,22,1),(13,13,1),(14,14,1),(15,15,1),(16,16,1),(17,17,1),(18,18,1),(19,19,1),(20,21,1),(21,22,1),(22,23,1),(23,24,1),(24,24,1),(25,25,1),(26,26,1);
/*!40000 ALTER TABLE `quartos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receita`
--

DROP TABLE IF EXISTS `receita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receita` (
  `consultaID` int(11) NOT NULL,
  `pacientesID` int(11) NOT NULL,
  `medicaID` int(11) NOT NULL,
  `medicamento` varchar(100) DEFAULT NULL,
  `Preco` float DEFAULT NULL,
  PRIMARY KEY (`consultaID`,`pacientesID`,`medicaID`),
  CONSTRAINT `receita_ibfk_1` FOREIGN KEY (`consultaID`, `pacientesID`, `medicaID`) REFERENCES `consulta` (`ID`, `pacientesID`, `medicaID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receita`
--

LOCK TABLES `receita` WRITE;
/*!40000 ALTER TABLE `receita` DISABLE KEYS */;
INSERT INTO `receita` VALUES (2,2,3,'tirzepatida',3500),(4,4,3,'ibuprofeno',40);
/*!40000 ALTER TABLE `receita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'simpleclinic'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-14 19:08:48
