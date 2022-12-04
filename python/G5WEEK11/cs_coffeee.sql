-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Dec 06, 2021 at 09:58 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs_coffee`
--

-- --------------------------------------------------------

--
-- Table structure for table `coffee_tb`
--

CREATE TABLE `coffee_tb` (
  `coffee_id` int(11) NOT NULL,
  `coffee_name` varchar(20) NOT NULL,
  `coffee_price` float NOT NULL,
  `mat_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `coffee_tb`
--

INSERT INTO `coffee_tb` (`coffee_id`, `coffee_name`, `coffee_price`, `mat_id`) VALUES
(1, 'Americano', 2.5, 1),
(2, 'Latte', 2.8, 2),
(3, 'Cappuccino', 2.9, 3);

-- --------------------------------------------------------

--
-- Table structure for table `customer_tb`
--

CREATE TABLE `customer_tb` (
  `customer_id` int(11) NOT NULL,
  `customer_first` varchar(12) DEFAULT NULL,
  `customer_last` varchar(12) DEFAULT NULL,
  `customer_phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_tb`
--

INSERT INTO `customer_tb` (`customer_id`, `customer_first`, `customer_last`, `customer_phone`) VALUES
(1, 'xie', 'weiya', '012606103'),
(2, 'lan', 'zhan ', '111'),
(3, 'Wei ', 'Wuxian', '222'),
(4, 'xie', 'lian', '333'),
(5, 'xiao', 'zhan', '555');

-- --------------------------------------------------------

--
-- Table structure for table `material_tb`
--

CREATE TABLE `material_tb` (
  `mat_id` int(11) NOT NULL,
  `mat_water` float NOT NULL,
  `mat_coffee_bean` float NOT NULL,
  `mat_sugar` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `material_tb`
--

INSERT INTO `material_tb` (`mat_id`, `mat_water`, `mat_coffee_bean`, `mat_sugar`) VALUES
(1, 10, 20, 30),
(2, 30, 20, 10),
(3, 20, 30, 10);

-- --------------------------------------------------------

--
-- Table structure for table `resource_tb`
--

CREATE TABLE `resource_tb` (
  `resource_id` int(10) UNSIGNED NOT NULL,
  `water` float NOT NULL,
  `coffee_bean` float NOT NULL,
  `sugar` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resource_tb`
--

INSERT INTO `resource_tb` (`resource_id`, `water`, `coffee_bean`, `sugar`) VALUES
(1, 1011, 1031, 1051);

-- --------------------------------------------------------

--
-- Table structure for table `sell_tb`
--

CREATE TABLE `sell_tb` (
  `sell_id` int(11) NOT NULL,
  `customer_id` int(10) UNSIGNED NOT NULL,
  `coffee_id` int(10) UNSIGNED NOT NULL,
  `sell_total` float NOT NULL DEFAULT 0,
  `sell_date` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sell_tb`
--

INSERT INTO `sell_tb` (`sell_id`, `customer_id`, `coffee_id`, `sell_total`, `sell_date`) VALUES
(1, 1, 1, 2.25, '2021-12-06'),
(2, 2, 2, 2.52, '2021-12-06'),
(3, 2, 3, 2.61, '2021-12-06'),
(4, 4, 3, 2.61, '2021-12-06'),
(5, 5, 1, 2.25, '2021-12-06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `coffee_tb`
--
ALTER TABLE `coffee_tb`
  ADD PRIMARY KEY (`coffee_id`);

--
-- Indexes for table `customer_tb`
--
ALTER TABLE `customer_tb`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `material_tb`
--
ALTER TABLE `material_tb`
  ADD PRIMARY KEY (`mat_id`);

--
-- Indexes for table `resource_tb`
--
ALTER TABLE `resource_tb`
  ADD PRIMARY KEY (`resource_id`);

--
-- Indexes for table `sell_tb`
--
ALTER TABLE `sell_tb`
  ADD PRIMARY KEY (`sell_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `coffee_tb`
--
ALTER TABLE `coffee_tb`
  MODIFY `coffee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `customer_tb`
--
ALTER TABLE `customer_tb`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `material_tb`
--
ALTER TABLE `material_tb`
  MODIFY `mat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `resource_tb`
--
ALTER TABLE `resource_tb`
  MODIFY `resource_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `sell_tb`
--
ALTER TABLE `sell_tb`
  MODIFY `sell_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
