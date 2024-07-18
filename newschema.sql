-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: newschema
-- ------------------------------------------------------
-- Server version	9.0.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes` (
  `sem_no` int NOT NULL,
  `section` varchar(10) NOT NULL,
  PRIMARY KEY (`sem_no`,`section`),
  CONSTRAINT `classes_ibfk_1` FOREIGN KEY (`sem_no`) REFERENCES `sems` (`sem_no`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES (3,'A'),(3,'B');
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sems`
--

DROP TABLE IF EXISTS `sems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sems` (
  `sem_no` int NOT NULL,
  `no_of_subs` int DEFAULT NULL,
  PRIMARY KEY (`sem_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sems`
--

LOCK TABLES `sems` WRITE;
/*!40000 ALTER TABLE `sems` DISABLE KEYS */;
INSERT INTO `sems` VALUES (3,11),(4,11);
/*!40000 ALTER TABLE `sems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subjs`
--

DROP TABLE IF EXISTS `subjs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subjs` (
  `sub` varchar(50) NOT NULL,
  `credits` int DEFAULT NULL,
  `sem_no` int DEFAULT NULL,
  PRIMARY KEY (`sub`),
  KEY `sem_no` (`sem_no`),
  CONSTRAINT `subjs_ibfk_1` FOREIGN KEY (`sem_no`) REFERENCES `sems` (`sem_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subjs`
--

LOCK TABLES `subjs` WRITE;
/*!40000 ALTER TABLE `subjs` DISABLE KEYS */;
INSERT INTO `subjs` VALUES ('ADVANCED JAVAPROGRAMMING',3,4),('COMPUTER ORGANISATION AND ARCHITECTURE',3,4),('DATA STRUCTURES AND APPLICATIONS',3,3),('DATA STRUCTURES WITH C/C++ LAB',1,3),('DATA VISUALIZATION LAB',2,3),('DATABASE MANAGEMENT SYSTEMS',4,4),('DATABASE MANAGEMENT SYSTEMS LAB',4,4),('DESIGN & ANALYSIS OF ALGORITHM',4,4),('DESIGN & ANALYSIS OF ALGORITHM LAB',2,4),('DIGITAL LOGIC DESIGN',4,3),('JAVA LABORATORY',1,4),('MASTERING OFFICE LAB',1,4),('MATHEMATICS',3,4),('MINIPROJECT',2,4),('OPERATING SYSTEM',4,3),('PYTHON PROGRAMMING',3,3),('REGRESSION WITH DATA SCIENCE',3,3),('SOCIAL CONNECT AND RESPONSIBILITY',1,3),('UNIVERSAL HUMAN VALUES COURSE',0,4),('VECTOR SPACES,SAMPLING THEORY AND OPTIMISATION',3,3),('WEB DEVELOPMENT LAB',1,4);
/*!40000 ALTER TABLE `subjs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `sub` varchar(50) DEFAULT NULL,
  `teacher_name` varchar(100) NOT NULL,
  `teacher_id` int DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `emaill` varchar(100) DEFAULT NULL,
  KEY `sub` (`sub`),
  CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`sub`) REFERENCES `subjs` (`sub`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES ('MINIPROJECT','0',0,NULL,NULL),('JAVA LABORATORY','BHARAT & MADHURA',6,NULL,NULL),('DESIGN & ANALYSIS OF ALGORITHM LAB','BINDU BHARGAVI & VAIDEHI',80,NULL,NULL),('DATA STRUCTURES WITH C/C++ LAB','MADHURA & SHALINLI',134,NULL,NULL),('DATABASE MANAGEMENT SYSTEMS LAB','SURESHKUMAR & VANI K',144,NULL,NULL),('DESIGN & ANALYSIS OF ALGORITHM','BINDU BHARGAVI',212,NULL,NULL),('DATABASE MANAGEMENT SYSTEMS','SURESHKUMAR',240,NULL,NULL),('VECTOR SPACES,SAMPLING THEORY AND OPTIMISATION','SAVITHRI',350,NULL,NULL),('PYTHON PROGRAMMING','MADHURA',390,NULL,NULL),('DATA VISUALIZATION LAB','LATHA & PRATHIMA',398,NULL,NULL),('REGRESSION WITH DATA SCIENCE','DIVYA',467,NULL,NULL),('MASTERING OFFICE LAB','PRAVEEN & BHARAT',532,NULL,NULL),('ADVANCED JAVAPROGRAMMING','BHARAT',565,NULL,NULL),('SOCIAL CONNECT AND RESPONSIBILITY','BHARAT B C',567,NULL,NULL),('DIGITAL LOGIC DESIGN','VARAPRASAD',580,NULL,NULL),('OPERATING SYSTEM','CHANDRAKALA',640,NULL,NULL),('UNIVERSAL HUMAN VALUES COURSE','MARY CHERIAN',700,NULL,NULL),('WEB DEVELOPMENT LAB','RADHIKA & LATHA A P',768,NULL,NULL),('MATHEMATICS','CHITHRA',787,NULL,NULL),('COMPUTER ORGANISATION AND ARCHITECTURE','RADHIKA',900,NULL,NULL),('DATA STRUCTURES AND APPLICATIONS','PRAVEEN',980,NULL,NULL),(NULL,'yuktha',NULL,'yuk','1ds22is191@dsce.edu.in'),(NULL,'varsha',NULL,'var','varsha@gmail.com');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tt`
--

DROP TABLE IF EXISTS `tt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tt` (
  `day` varchar(20) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `sub` varchar(100) DEFAULT NULL,
  `teacher_name` varchar(45) DEFAULT NULL,
  `teacher_id` int DEFAULT NULL,
  `sem_no` int DEFAULT NULL,
  `section` varchar(45) DEFAULT NULL,
  KEY `sub_idx` (`sub`),
  KEY `teacher_id_idx` (`teacher_id`),
  KEY `sem_no_idx` (`sem_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tt`
--

LOCK TABLES `tt` WRITE;
/*!40000 ALTER TABLE `tt` DISABLE KEYS */;
INSERT INTO `tt` VALUES ('monday','9:00','DATA VISUALIZATION LAB','LATHA & PRATHIMA',398,3,'C'),('monday','11:15','DIGITAL LOGIC DESIGN','VARAPRASAD',580,3,'C'),('monday','12:15','OPERATING SYSTEM','CHANDRAKALA',640,3,'C'),('monday','2:00','PYTHON PROGRAMMING','MADHURA',390,3,'C'),('monday','3:00','REGRESSION WITH DATA SCIENCE','DIVYA',467,3,'C'),('saturday','9:00','SOCIAL CONNECT AND RESPONSIBILITY','BHARAT B C',567,3,'C'),('saturday','10:00','REGRESSION WITH DATA SCIENCE','DIVYA',467,3,'C'),('tuesday','9:00','VECTOR SPACES,SAMPLING THEORY AND OPTIMISATION','SAVITHRI',350,3,'C'),('tuesday','10:00','OPERATING SYSTEM','CHANDRAKALA',640,3,'C'),('tuesday','11:15','PYTHON PROGRAMMING','MADHURA',390,3,'C'),('tuesday','12:15','DATA STRUCTURES AND APPLICATIONS','PRAVEEN',980,3,'C'),('tuesday','1:00','REGRESSION WITH DATA SCIENCE','DIVYA',467,3,'C'),('tuesday','1:00','SOCIAL CONNECT AND RESPONSIBILITY','BHARAT B C',567,3,'C'),('wednesday','9:00','DATA VISUALIZATION LAB','LATHA & PRATHIMA',398,3,'C'),('wednesday','11:15','DIGITAL LOGIC DESIGN','VARAPRASAD',580,3,'C'),('wednesday','12:15','VECTOR SPACES,SAMPLING THEORY AND OPTIMISATION','SAVITHRI',350,3,'C'),('wednesday','2:00','DATA STRUCTURES WITH C/C++ LAB','MADHURA & SHALINLI',134,3,'C'),('wednesday','2:00','DIGITAL LOGIC DESIGN','VARAPRASAD',580,3,'C'),('wednesday','2:00','OPERATING SYSTEM','CHANDRAKALA',640,3,'C'),('thursday','9:00','DATA VISUALIZATION LAB','LATHA & PRATHIMA',398,3,'C'),('thursday','11:15','VECTOR SPACES,SAMPLING THEORY AND OPTIMISATION','SAVITHRI',350,3,'C'),('thursday','11:15','DIGITAL LOGIC DESIGN','VARAPRASAD',580,3,'C'),('thursday','2:00','DATA STRUCTURES WITH C/C++ LAB','MADHURA & SHALINLI',134,3,'C'),('thursday','2:00','DIGITAL LOGIC DESIGN','VARAPRASAD',580,3,'C'),('thursday','2:00','OPERATING SYSTEM','CHANDRAKALA',640,3,'C'),('friday','9:00','VECTOR SPACES,SAMPLING THEORY AND OPTIMISATION','SAVITHRI',350,3,'C'),('friday','10:00','OPERATING SYSTEM','CHANDRAKALA',640,3,'C'),('friday','11:15','PYTHON PROGRAMMING','MADHURA',390,3,'C'),('friday','12:15','DATA STRUCTURES AND APPLICATIONS','PRAVEEN',980,3,'C'),('friday','2:00','DATA STRUCTURES WITH C/C++ LAB','MADHURA & SHALINLI',134,3,'C'),('friday','2:00','DIGITAL LOGIC DESIGN','VARAPRASAD',580,3,'C'),('friday','2:00','OPERATING SYSTEM','CHANDRAKALA',640,3,'C'),('monday','03:30','python',NULL,NULL,1,'B'),('monday','04:00','python','yuktha3',45,2,'A'),('monday','10','python','yuktha3',45,2,'A'),('monday','9','python','yuktha3',45,2,'A'),('monday','9:00','python','yuktha3',45,2,'A'),('monday','3:00','python','yuktha3',45,2,'A'),('monday','12:15','python','yuktha3',45,2,'A'),('monday','11:15','python','yuktha3',45,2,'A'),('monday','4:00','python','yuktha3',45,2,'A'),('tuesday','2:00','kannada','pranavi',67,1,'A'),('tuesday','3:00','kannada','pranavi',67,1,'A'),('tuesday','9:00','kannada','pranavi',67,2,'A'),('tuesday','9:00','kannada','pranavi',67,5,'A'),('tuesday','9:00','kannada','pranavi',67,8,'A'),('tuesday','2:00','kannada','pranavi',67,6,'A'),('tuesday','9:00','kannada','pranavi',67,6,'A'),('tuesday','12:15','kannada','pranavi',67,6,'A'),('friday','9:00','python','yuktha',NULL,6,'A'),('friday','9:00','python','yuktha',NULL,7,'A');
/*!40000 ALTER TABLE `tt` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-17 19:32:08
