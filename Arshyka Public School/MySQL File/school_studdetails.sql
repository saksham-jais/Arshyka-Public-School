-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: school
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `studdetails`
--

DROP TABLE IF EXISTS `studdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studdetails` (
  `admission_no` int NOT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `Father_name` varchar(100) DEFAULT NULL,
  `Mother_name` varchar(100) DEFAULT NULL,
  `sclass` varchar(10) DEFAULT NULL,
  `section` varchar(10) DEFAULT NULL,
  `phone_no` varchar(10) DEFAULT NULL,
  `DOA` varchar(20) DEFAULT NULL,
  `Address` varchar(1000) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `sdob` varchar(20) DEFAULT NULL,
  `stream` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`admission_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studdetails`
--

LOCK TABLES `studdetails` WRITE;
/*!40000 ALTER TABLE `studdetails` DISABLE KEYS */;
INSERT INTO `studdetails` VALUES (100,'rashika','pradeep','renu','12','d','9794083484','12/2/12','IMARTI ROAD','rashika@gmail.com','female','30/10/2006','Science with Maths'),(101,'rashi','pradeep','renu','4','d','9794083484','12/2/12','IMARTI ROAD','rashika@gmail.com','female','30/10/2006','None'),(102,'som','pradeep','renu','7','d','9794083484','12/2/12','IMARTI ROAD','rashika@gmail.com','male','30/10/2006','None'),(103,'pritosh','pradeep','renu','10','d','9794083484','12/2/12','IMARTI ROAD','rashika@gmail.com','male','30/10/2006','None'),(104,'aman','pradeep','renu','11','d','9794083484','12/2/12','IMARTI ROAD','rashika@gmail.com','male','30/10/2006','Science with Bio'),(105,'shivansh','pradeep','renu','11','d','9794083484','12/2/12','IMARTI ROAD','rashika@gmail.com','male','30/10/2006','Commerce'),(106,'ruby','pradeep','renu','11','d','9794083484','12/2/12','IMARTI ROAD','rashika@gmail.com','male','30/10/2006','Humanity');
/*!40000 ALTER TABLE `studdetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-06 14:58:55
