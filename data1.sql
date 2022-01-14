/*

SQLyog Ultimate v12.09 (64 bit)

MySQL - 8.0.27 : Database - base1

*********************************************************************

*/





/*!40101 SET NAMES utf8 */;



/*!40101 SET SQL_MODE=''*/;



/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`project` /*!40100 DEFAULT CHARACTER SET gbk */ /*!80016 DEFAULT ENCRYPTION='N' */;



USE `project`;



/*Table structure for table `obj_envinterface` */



DROP TABLE IF EXISTS `model_obj_envinterface`;



CREATE TABLE `model_obj_envinterface` (

  `interfaceid` bigint NOT NULL AUTO_INCREMENT COMMENT '������ID',

  `carLicenseno` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '��ID',

  `readtime` datetime DEFAULT NULL COMMENT '�豸ʱ��',

  `baidulongitude` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '�ٶȾ���',

  `baidulatitude` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '�ٶ�γ��',

  `gpslongitude` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'gps����',

  `gpslatitude` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'gpsγ��',

  `recordspeed` int DEFAULT NULL COMMENT '����',

  `cardirection` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '����',

  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '��λ��ַ',

  `loadweight` int DEFAULT NULL COMMENT '����',

  `garabtype` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,

  PRIMARY KEY (`interfaceid`) USING BTREE

) ENGINE=InnoDB AUTO_INCREMENT=47317265 DEFAULT CHARSET=utf8mb3 ROW_FORMAT=COMPACT COMMENT='�Ϻ�����Ժʪ�����ӿ�';



/*Data for the table `obj_envinterface` */



