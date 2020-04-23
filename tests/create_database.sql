SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


DROP SCHEMA IF EXISTS `auto_lamtv10`;

CREATE SCHEMA IF NOT EXISTS `auto_lamtv10` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `auto_lamtv10` ;

-- -----------------------------------------------------
-- Table `auto_lamtv10`.`node_infos`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`node_infos` (
  `node_info_id` VARCHAR(255) NOT NULL ,
  `memory_mb` INT(11) NULL ,
  `memory_mb_free` INT(11) NULL ,
  `numa_topology` TEXT NULL ,
  `metrics` TEXT NULL ,
  `processor_core` INT NULL ,
  `processor_count` INT NULL ,
  `processor_threads_per_core` INT NULL ,
  `processor_vcpu` INT NULL ,
  `node_name` VARCHAR(255) NULL ,
  `os_family` VARCHAR(255) NULL ,
  `pkg_mgr` VARCHAR(255) NULL ,
  `os_version` VARCHAR(255) NULL ,
  `default_ipv4` VARCHAR(255) NULL ,
  `default_broadcast` VARCHAR(255) NULL ,
  `default_gateway` VARCHAR(255) NULL ,
  `default_interface_id` VARCHAR(255) NULL ,
  PRIMARY KEY (`node_info_id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`deployments`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`deployments` (
  `deployment_id` INT(11) NOT NULL AUTO_INCREMENT ,
  `created_at` DATETIME NULL ,
  `updated_at` DATETIME NULL ,
  `finished_at` DATETIME NULL ,
  `status` VARCHAR(255) NULL ,
  `name` VARCHAR(255) NULL ,
  `jsondata` TEXT NULL ,
  `log` TEXT NULL ,
  `result` VARCHAR(255) NULL ,
  `progress` VARCHAR(255) NULL ,
  PRIMARY KEY (`deployment_id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`nodes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`nodes` (
  `node_id` INT(11) NOT NULL AUTO_INCREMENT ,
  `created_at` DATETIME NULL ,
  `updated_at` DATETIME NULL ,
  `deleted_at` DATETIME NULL ,
  `management_ip` VARCHAR(255) NULL ,
  `ssh_user` VARCHAR(255) NULL ,
  `ssh_password` VARCHAR(255) NULL ,
  `status` TEXT NULL ,
  `node_display_name` VARCHAR(255) NULL ,
  `node_info_id` VARCHAR(255) NULL ,
  `deployment_id` INT(11) NULL ,
  `node_type` VARCHAR(255) NULL ,
  PRIMARY KEY (`node_id`) ,
  CONSTRAINT `fk_nodes_hardware_infos1`
    FOREIGN KEY (`node_info_id` )
    REFERENCES `auto_lamtv10`.`node_infos` (`node_info_id` )
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_nodes_deployments1`
    FOREIGN KEY (`deployment_id` )
    REFERENCES `auto_lamtv10`.`deployments` (`deployment_id` )
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_nodes_hardware_infos1_idx` ON `auto_lamtv10`.`nodes` (`node_info_id` ASC) ;

CREATE INDEX `fk_nodes_deployments1_idx` ON `auto_lamtv10`.`nodes` (`deployment_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`interface_resources`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`interface_resources` (
  `interface_id` VARCHAR(255) NOT NULL ,
  `device_name` VARCHAR(255) NULL ,
  `speed` INT(11) NULL ,
  `port_info` TEXT NULL ,
  `active` VARCHAR(255) NULL ,
  `features` TEXT NULL ,
  `macaddress` VARCHAR(255) NULL ,
  `module` VARCHAR(255) NULL ,
  `mtu` INT NULL ,
  `pciid` VARCHAR(255) NULL ,
  `phc_index` INT NULL ,
  `type_interface` VARCHAR(255) NULL ,
  `is_default_ip` VARCHAR(255) NULL ,
  `node_info_id` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`interface_id`) ,
  CONSTRAINT `fk_interface_resources_node_infos1`
    FOREIGN KEY (`node_info_id` )
    REFERENCES `auto_lamtv10`.`node_infos` (`node_info_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_interface_resources_node_infos1_idx` ON `auto_lamtv10`.`interface_resources` (`node_info_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`service_setups`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`service_setups` (
  `service_setup_id` INT(11) NOT NULL AUTO_INCREMENT,
  `service_type` VARCHAR(255) NULL ,
  `service_name` VARCHAR(255) NULL ,
  `enable` VARCHAR(255) NULL ,
  `status` VARCHAR(255) NULL ,
  `service_info` TEXT NULL ,
  `service_lib` TEXT NULL ,
  `service_config_folder` TEXT NULL ,
  `setup_index` INT(11) NULL ,
  `is_validated_success` VARCHAR(255) NULL ,
  `validated_status` VARCHAR(45) NULL ,
  `deployment_id` INT(11) NOT NULL ,
  PRIMARY KEY (`service_setup_id`) ,
  CONSTRAINT `fk_service_setups_deployments1`
    FOREIGN KEY (`deployment_id` )
    REFERENCES `auto_lamtv10`.`deployments` (`deployment_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_service_setups_deployments1_idx` ON `auto_lamtv10`.`service_setups` (`deployment_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`tasks`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`tasks` (
  `task_id` INT(11) NOT NULL AUTO_INCREMENT ,
  `created_at` DATETIME NULL ,
  `finished_at` DATETIME NULL ,
  `task_display_name` VARCHAR(255) NULL ,
  `setup_data` VARCHAR(255) NULL ,
  `task_type` VARCHAR(255) NULL ,
  `status` VARCHAR(255) NULL ,
  `result` VARCHAR(255) NULL ,
  `log` TEXT NULL ,
  `task_index` INT(11) NULL ,
  `service_setup_id` INT(11) NOT NULL ,
  PRIMARY KEY (`task_id`) ,
  CONSTRAINT `fk_tasks_service_setups1`
    FOREIGN KEY (`service_setup_id` )
    REFERENCES `auto_lamtv10`.`service_setups` (`service_setup_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_tasks_service_setups1_idx` ON `auto_lamtv10`.`tasks` (`service_setup_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`file_configs`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`file_configs` (
  `file_id` INT(11) NOT NULL AUTO_INCREMENT ,
  `node_id` INT(11) NOT NULL ,
  `file_name` VARCHAR(255) NULL ,
  `file_path` VARCHAR(255) NULL ,
  `service_name` VARCHAR(255) NULL ,
  `created_at` DATETIME NULL ,
  `modified_at` DATETIME NULL ,
  PRIMARY KEY (`file_id`) ,
  CONSTRAINT `fk_file_config_nodes1`
    FOREIGN KEY (`node_id` )
    REFERENCES `auto_lamtv10`.`nodes` (`node_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_file_config_nodes1_idx` ON `auto_lamtv10`.`file_configs` (`node_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`changes`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`changes` (
  `change_id` VARCHAR(255) NOT NULL ,
  `created_at` DATETIME NULL ,
  `finished_at` DATETIME NULL ,
  `status` VARCHAR(255) NULL ,
  `change_type` VARCHAR(255) NULL ,
  `new_service` VARCHAR(255) NULL ,
  `backup_service` VARCHAR(255) NULL ,
  `new_file` TEXT NULL ,
  `backup_file` TEXT NULL ,
  `new_folder` TEXT NULL ,
  `backup_folder` TEXT NULL ,
  `change_log` TEXT NULL ,
  `task_id` INT(11) NULL ,
  `change_index` INT NULL ,
  `file_config_id` VARCHAR(255) NULL ,
  `file_config_file_id` INT(11) ,
  PRIMARY KEY (`change_id`) ,
  CONSTRAINT `fk_changes_tasks1`
    FOREIGN KEY (`task_id` )
    REFERENCES `auto_lamtv10`.`tasks` (`task_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_changes_file_config1`
    FOREIGN KEY (`file_config_file_id` )
    REFERENCES `auto_lamtv10`.`file_configs` (`file_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_changes_tasks1_idx` ON `auto_lamtv10`.`changes` (`task_id` ASC) ;

CREATE INDEX `fk_changes_file_config1_idx` ON `auto_lamtv10`.`changes` (`file_config_file_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`updates`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`updates` (
  `update_id` VARCHAR(255) NOT NULL ,
  `created_at` DATETIME NULL ,
  `deleted_at` DATETIME NULL ,
  `note` TEXT NULL ,
  `log` TEXT NULL ,
  PRIMARY KEY (`update_id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`update_change`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`update_change` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `update_id` VARCHAR(255) NOT NULL ,
  `change_id` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `fk_update_change_update1`
    FOREIGN KEY (`update_id` )
    REFERENCES `auto_lamtv10`.`updates` (`update_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_update_change_changes1`
    FOREIGN KEY (`change_id` )
    REFERENCES `auto_lamtv10`.`changes` (`change_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_update_change_update1_idx` ON `auto_lamtv10`.`update_change` (`update_id` ASC) ;

CREATE INDEX `fk_update_change_changes1_idx` ON `auto_lamtv10`.`update_change` (`change_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`passwords`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`passwords` (
  `password_id` INT(11) NOT NULL AUTO_INCREMENT ,
  `created_at` DATETIME NULL ,
  `updated_at` DATETIME NULL ,
  `user` VARCHAR(255) NULL ,
  `password` VARCHAR(255) NULL ,
  `update_id` VARCHAR(255) NOT NULL ,
  `service_name` VARCHAR(255) NULL ,
  PRIMARY KEY (`password_id`, `update_id`) ,
  CONSTRAINT `fk_password_update1`
    FOREIGN KEY (`update_id` )
    REFERENCES `auto_lamtv10`.`updates` (`update_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_password_update1_idx` ON `auto_lamtv10`.`passwords` (`update_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`openstack_configs`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`openstack_configs` (
  `config_id` VARCHAR(255) NOT NULL ,
  `created_at` DATETIME NULL ,
  `deleted_at` DATETIME NULL ,
  `key` VARCHAR(255) NULL ,
  `value` TEXT NULL ,
  `service` VARCHAR(255) NULL ,
  `update_id` VARCHAR(255) NOT NULL ,
  `password_id` INT(11) NULL ,
  `block` VARCHAR(255) NULL ,
  `file_id` INT(11) NOT NULL ,
  `activate` INT NULL ,
  PRIMARY KEY (`config_id`, `update_id`, `file_id`) ,
  CONSTRAINT `fk_openstack_config_update1`
    FOREIGN KEY (`update_id` )
    REFERENCES `auto_lamtv10`.`updates` (`update_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_openstack_config_password1`
    FOREIGN KEY (`password_id` )
    REFERENCES `auto_lamtv10`.`passwords` (`password_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_openstack_config_file_config1`
    FOREIGN KEY (`file_id` )
    REFERENCES `auto_lamtv10`.`file_configs` (`file_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_openstack_config_update1_idx` ON `auto_lamtv10`.`openstack_configs` (`update_id` ASC) ;

CREATE INDEX `fk_openstack_config_password1_idx` ON `auto_lamtv10`.`openstack_configs` (`password_id` ASC) ;

CREATE INDEX `fk_openstack_config_file_config1_idx` ON `auto_lamtv10`.`openstack_configs` (`file_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`disk_resources`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`disk_resources` (
  `disk_id` VARCHAR(255) NOT NULL ,
  `device_name` VARCHAR(255) NULL ,
  `size` INT NULL ,
  `model` VARCHAR(255) NULL ,
  `removable` INT NULL ,
  `sectors` MEDIUMTEXT NULL ,
  `sectorsize` INT NULL ,
  `serial` VARCHAR(255) NULL ,
  `vendor` VARCHAR(255) NULL ,
  `support_discard` VARCHAR(255) NULL ,
  `virtual` INT NULL ,
  `node_info_id` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`disk_id`) ,
  CONSTRAINT `fk_disk_resources_node_infos1`
    FOREIGN KEY (`node_info_id` )
    REFERENCES `auto_lamtv10`.`node_infos` (`node_info_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_disk_resources_node_infos1_idx` ON `auto_lamtv10`.`disk_resources` (`node_info_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`service_infos`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`service_infos` (
  `service_id` INT(11) NOT NULL AUTO_INCREMENT ,
  `service_type` VARCHAR(255) NULL ,
  `service_status` VARCHAR(255) NULL ,
  `tag` VARCHAR(255) NULL ,
  `node_id` INT(11) NOT NULL ,
  PRIMARY KEY (`service_id`) ,
  CONSTRAINT `fk_service_infos_nodes1`
    FOREIGN KEY (`node_id` )
    REFERENCES `auto_lamtv10`.`nodes` (`node_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_service_infos_nodes1_idx` ON `auto_lamtv10`.`service_infos` (`node_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`service_info_file_config`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`service_info_file_config` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `service_id` INT(11) NOT NULL ,
  `file_config_id` INT(11) NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `fk_service_info_file_config_service_infos1`
    FOREIGN KEY (`service_id` )
    REFERENCES `auto_lamtv10`.`service_infos` (`service_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_service_info_file_config_file_config1`
    FOREIGN KEY (`file_config_id` )
    REFERENCES `auto_lamtv10`.`file_configs` (`file_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_service_info_file_config_service_infos1_idx` ON `auto_lamtv10`.`service_info_file_config` (`service_id` ASC) ;

CREATE INDEX `fk_service_info_file_config_file_config1_idx` ON `auto_lamtv10`.`service_info_file_config` (`file_config_id` ASC) ;


-- -----------------------------------------------------
-- Table `auto_lamtv10`.`node_roles`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auto_lamtv10`.`node_roles` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `role_name` VARCHAR(255) NULL ,
  `node_id` INT(11) NOT NULL ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `fk_node_roles_nodes1`
    FOREIGN KEY (`node_id` )
    REFERENCES `auto_lamtv10`.`nodes` (`node_id` )
    ON DELETE CASCADE 
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_node_roles_nodes1_idx` ON `auto_lamtv10`.`node_roles` (`node_id` ASC) ;

USE `auto_lamtv10` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
