/*
SQLyog Enterprise - MySQL GUI v7.02 
MySQL - 5.0.67-community-nt : Database - test1
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`test1` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `test1`;

/*Table structure for table `login1` */

DROP TABLE IF EXISTS `login1`;

CREATE TABLE `login1` (
  `Name` varchar(100) default NULL,
  `email` varchar(100) default NULL,
  `mob` varchar(100) default NULL,
  `username` varchar(100) default NULL,
  `password` varchar(20) default NULL,
  `fathername` varchar(20) default NULL,
  `pincode` varchar(6) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC;

/*Data for the table `login1` */

insert  into `login1`(`Name`,`email`,`mob`,`username`,`password`,`fathername`,`pincode`) values ('bhgbj','bhjnkl','nkjjjnl','nklhjiohg','dd',NULL,NULL),('vcvg','bkjnmk','knlkjm','lkmllkl',';',NULL,NULL),('abhi','abhi','9800','abhishek','1234',NULL,NULL),('vhj','bjbk','bkjbkjb','kjbkjbkjbk','jkbbj','jb','jbb'),('vhg','jbhb ','hjbjh','bjhjhb','bh','bh','hjvhj'),('abhlk','abhis.garg@gmail.com','uyggyu','gybnj','plp','bhjlkjhnbjh','87uy'),('ftyugh','bhj@vgh.cfv','ftyguhi','vyybun','yu','vhbjn','vtygbh'),('xdfghbj','tcyvu@dcfvgb.cfvg','56789','cgvhbjn','kk','ctyvbuhn',''),('ftyfyguhi','ytvbhnj@bnm.hbh','bhnj','tgyh','hh','vbhnj','tvbh'),('ftvgybun','cfav@gcvhbjn.bo','1234578900','edrfgh','kk','ftgyuj','888888'),('dfgh','dxrcfvg@xcfvg.gH','5555555555','dfghb','ff','rty7u8i','777777'),('6dfghj','AGVHBJ@VGBH.VBN','0000000000','GVBH','kk','CFGVHB','888888'),('SGDHJN','SNXDJ@BNJD.CIK','9898989898','CVGBHN','JJ','VBHNJSKX','000000'),('ghjns233','abh@jns.co','0909090909','sbdnjkc','JJ','njlm78','888888'),('YUYUHIN','GFHBJ@YVU.HG','9999999999','DCFVGBHJ','lol','CVGBH','777777'),('hb','CF@FGB.njm','0000000000','ybui','jnj','HB','888888');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
