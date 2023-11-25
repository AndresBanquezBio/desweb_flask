-- Schema db_healthcare
DROP SCHEMA IF EXISTS `db_healthcare`;
CREATE SCHEMA IF NOT EXISTS `db_healthcare`;
USE `db_healthcare`;

-- Table `medics`
CREATE TABLE IF NOT EXISTS `medics` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `specialty` VARCHAR(255) NOT NULL,
  `contact` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- Table `patients`
CREATE TABLE IF NOT EXISTS `patients` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `lastname` VARCHAR(255) NOT NULL,
  `contact` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `gender` ENUM('Male', 'Female', 'Other') NOT NULL,
  `medic_id` INT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`medic_id`) REFERENCES `medics`(`id`) ON DELETE SET NULL
) ENGINE = InnoDB;

-- Sample data
INSERT INTO `medics`(`name`, `specialty`, `contact`) VALUES('Dr. Smith', 'Cardiology', '123-456-7890');
INSERT INTO `medics`(`name`, `specialty`, `contact`) VALUES('Dr. Johnson', 'Orthopedics', '987-654-3210');
INSERT INTO `patients`(`name`, `lastname`, `contact`, `address`, `gender`, `medic_id`) VALUES('John', 'Doe', '555-1234', '123 Main St', 'Male', 1);
INSERT INTO `patients`(`name`, `lastname`, `contact`, `address`, `gender`, `medic_id`) VALUES('Jane', 'Smith', '555-5678', '456 Oak St', 'Female', 2);
