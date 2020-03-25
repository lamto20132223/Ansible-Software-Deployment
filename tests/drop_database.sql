SET FOREIGN_KEY_CHECKS=0;

USE `auto_lamtv10` ;
DELETE FROM changes;
DELETE FROM  deployments;
DELETE FROM  disk_resources;
DELETE FROM  file_configs;
DELETE FROM  interface_resources;
DELETE FROM  node_infos;
DELETE FROM  node_roles;
DELETE FROM  nodes;
DELETE FROM  openstack_configs;
DELETE FROM  passwords;
DELETE FROM  service_info_file_config;
DELETE FROM  service_infos;
DELETE FROM  service_setups;
DELETE FROM  tasks;
DELETE FROM  update_change;
DELETE FROM  updates;
SET FOREIGN_KEY_CHECKS=1;

