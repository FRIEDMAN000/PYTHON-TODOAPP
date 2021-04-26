-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 26, 2021 at 03:30 PM
-- Server version: 8.0.23-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `TODO_LIST`
--

-- --------------------------------------------------------

--
-- Table structure for table `Todo`
--

CREATE TABLE `Todo` (
  `todo_name` varchar(255) NOT NULL,
  `todo_list_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Todo`
--



-- --------------------------------------------------------

--
-- Table structure for table `Todo_List`
--

CREATE TABLE `Todo_List` (
  `todo_list_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `statut` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'pending...',
  `user_name` varchar(20) NOT NULL,
  `reminder_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Todo_List`
--



-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `user_name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `User`
--



--
-- Indexes for dumped tables
--

--
-- Indexes for table `Todo`
--
ALTER TABLE `Todo`
  ADD PRIMARY KEY (`todo_name`,`todo_list_name`),
  ADD KEY `todo_list_name` (`todo_list_name`);

--
-- Indexes for table `Todo_List`
--
ALTER TABLE `Todo_List`
  ADD PRIMARY KEY (`todo_list_name`),
  ADD KEY `user_name` (`user_name`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`user_name`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Todo`
--
ALTER TABLE `Todo`
  ADD CONSTRAINT `Todo_ibfk_1` FOREIGN KEY (`todo_list_name`) REFERENCES `Todo_List` (`todo_list_name`);

--
-- Constraints for table `Todo_List`
--
ALTER TABLE `Todo_List`
  ADD CONSTRAINT `Todo_List_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `User` (`user_name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
