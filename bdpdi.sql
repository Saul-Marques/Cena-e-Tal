/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.6.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: projetoPDI
-- ------------------------------------------------------
-- Server version	11.6.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add user',7,'add_user'),
(26,'Can change user',7,'change_user'),
(27,'Can delete user',7,'delete_user'),
(28,'Can view user',7,'view_user'),
(29,'Can add product',8,'add_product'),
(30,'Can change product',8,'change_product'),
(31,'Can delete product',8,'delete_product'),
(32,'Can view product',8,'view_product'),
(33,'Can add categoria',9,'add_categoria'),
(34,'Can change categoria',9,'change_categoria'),
(35,'Can delete categoria',9,'delete_categoria'),
(36,'Can view categoria',9,'view_categoria'),
(37,'Can add contact message',10,'add_contactmessage'),
(38,'Can change contact message',10,'change_contactmessage'),
(39,'Can delete contact message',10,'delete_contactmessage'),
(40,'Can view contact message',10,'view_contactmessage'),
(41,'Can add mensagens_de_ contactos',10,'add_mensagens_de_contactos'),
(42,'Can change mensagens_de_ contactos',10,'change_mensagens_de_contactos'),
(43,'Can delete mensagens_de_ contactos',10,'delete_mensagens_de_contactos'),
(44,'Can view mensagens_de_ contactos',10,'view_mensagens_de_contactos'),
(45,'Can add product image',11,'add_productimage'),
(46,'Can change product image',11,'change_productimage'),
(47,'Can delete product image',11,'delete_productimage'),
(48,'Can view product image',11,'view_productimage'),
(49,'Can add message',12,'add_message'),
(50,'Can change message',12,'change_message'),
(51,'Can delete message',12,'delete_message'),
(52,'Can view message',12,'view_message'),
(53,'Can add conversation',13,'add_conversation'),
(54,'Can change conversation',13,'change_conversation'),
(55,'Can delete conversation',13,'delete_conversation'),
(56,'Can view conversation',13,'view_conversation'),
(57,'Can add licitacao',14,'add_licitacao'),
(58,'Can change licitacao',14,'change_licitacao'),
(59,'Can delete licitacao',14,'delete_licitacao'),
(60,'Can view licitacao',14,'view_licitacao');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES
(1,'pbkdf2_sha256$870000$ucIvnbQcyK6kz7oWRgLWDM$MjCzHVAMUxBSmy3BkwSV4Le+w8Yw+7zr4DYjSSB41NM=','2025-03-19 15:23:50.202961',1,'saul','Saúl','Marques','saul_marques10@hotmail.com',1,1,'2025-02-13 15:43:05.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_conversation`
--

DROP TABLE IF EXISTS `chat_conversation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat_conversation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `user1_id` bigint(20) NOT NULL,
  `user2_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `chat_conversation_user1_id_user2_id_product_id_fa647738_uniq` (`user1_id`,`user2_id`,`product_id`),
  KEY `chat_conversation_user2_id_be3cd90d_fk_loja_user_id` (`user2_id`),
  KEY `chat_conversation_user1_id_40866d67` (`user1_id`),
  KEY `chat_conversation_product_id_a70bba8c_fk_loja_product_id` (`product_id`),
  CONSTRAINT `chat_conversation_product_id_a70bba8c_fk_loja_product_id` FOREIGN KEY (`product_id`) REFERENCES `loja_product` (`id`),
  CONSTRAINT `chat_conversation_user1_id_40866d67_fk_loja_user_id` FOREIGN KEY (`user1_id`) REFERENCES `loja_user` (`id`),
  CONSTRAINT `chat_conversation_user2_id_be3cd90d_fk_loja_user_id` FOREIGN KEY (`user2_id`) REFERENCES `loja_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_conversation`
--

LOCK TABLES `chat_conversation` WRITE;
/*!40000 ALTER TABLE `chat_conversation` DISABLE KEYS */;
INSERT INTO `chat_conversation` VALUES
(10,'2025-04-22 14:17:02.196564',1,3,22),
(11,'2025-04-22 14:27:58.914205',1,7,24);
/*!40000 ALTER TABLE `chat_conversation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_message`
--

DROP TABLE IF EXISTS `chat_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat_message` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `conversation_id` bigint(20) NOT NULL,
  `sender_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chat_message_conversation_id_a1207bf4_fk_chat_conversation_id` (`conversation_id`),
  KEY `chat_message_sender_id_991c686c_fk_loja_user_id` (`sender_id`),
  CONSTRAINT `chat_message_conversation_id_a1207bf4_fk_chat_conversation_id` FOREIGN KEY (`conversation_id`) REFERENCES `chat_conversation` (`id`),
  CONSTRAINT `chat_message_sender_id_991c686c_fk_loja_user_id` FOREIGN KEY (`sender_id`) REFERENCES `loja_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=203 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_message`
--

LOCK TABLES `chat_message` WRITE;
/*!40000 ALTER TABLE `chat_message` DISABLE KEYS */;
INSERT INTO `chat_message` VALUES
(188,'Boas, pode enviar-me o carro por correio para testar?','2025-04-22 14:17:17.039668',10,1),
(189,'por favor','2025-04-22 14:19:45.501545',10,1),
(190,'ok','2025-04-22 14:21:50.865162',10,1),
(191,'ola','2025-04-22 14:28:57.890315',11,1),
(202,'kkkk','2025-04-23 14:40:01.417558',10,1);
/*!40000 ALTER TABLE `chat_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES
(1,'2025-02-13 15:44:48.377642','1','saul',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),
(2,'2025-02-17 09:52:55.910286','1','debug',1,'[{\"added\": {}}]',9,1),
(3,'2025-02-17 09:53:14.052066','1','Product object (1)',1,'[{\"added\": {}}]',8,1),
(4,'2025-02-17 13:37:41.602508','2','Product object (2)',1,'[{\"added\": {}}]',8,1),
(5,'2025-02-17 14:04:41.320455','1','debug',3,'',9,1),
(6,'2025-02-17 14:10:44.029814','2','debug',1,'[{\"added\": {}}]',9,1),
(7,'2025-02-19 15:02:14.663132','5','Teste do novo form',3,'',8,1),
(8,'2025-02-19 15:02:14.663221','6','teste multiple imagens',3,'',8,1),
(9,'2025-02-21 09:29:05.661388','3','Teste user',3,'',8,1),
(10,'2025-02-21 09:29:05.661445','4','teste 1 imagem',3,'',8,1),
(11,'2025-02-21 09:29:05.661469','7','teste outra vez',3,'',8,1),
(12,'2025-02-21 09:29:05.661490','8','Produto falso',3,'',8,1),
(13,'2025-02-21 09:29:05.661512','9','Produto verdadeiro',3,'',8,1),
(14,'2025-02-21 09:29:05.661526','10','Mais um teste',3,'',8,1),
(15,'2025-02-21 09:29:05.661538','11','Another teste',3,'',8,1),
(16,'2025-02-21 09:29:05.661549','12','Yet Another teste',3,'',8,1),
(17,'2025-02-21 09:29:05.661560','13','aaaaaaaa',3,'',8,1),
(18,'2025-02-21 09:29:05.661572','14','zxxxxzzz',3,'',8,1),
(19,'2025-02-21 09:29:05.661583','15','iAOASD',3,'',8,1),
(20,'2025-02-21 09:29:05.661595','16','sss',3,'',8,1),
(21,'2025-02-21 09:29:05.661606','17','asdad',3,'',8,1),
(22,'2025-02-21 09:29:05.661617','18','ssdfsfds',3,'',8,1),
(23,'2025-02-21 09:29:05.661628','19','terqe',3,'',8,1),
(24,'2025-03-06 18:13:34.842680','1','saul@mail.com',2,'[{\"changed\": {\"fields\": [\"Profile picture\"]}}]',7,1),
(25,'2025-03-06 18:13:43.149465','2','boneco@mail.com',2,'[{\"changed\": {\"fields\": [\"Profile picture\"]}}]',7,1),
(26,'2025-03-06 18:21:59.905194','1','saul@mail.com',2,'[{\"changed\": {\"fields\": [\"Profile picture\"]}}]',7,1),
(27,'2025-03-06 18:22:06.385778','1','saul@mail.com',2,'[{\"changed\": {\"fields\": [\"Profile picture\"]}}]',7,1),
(28,'2025-03-11 09:24:57.457140','2','boneco@mail.com',2,'[{\"changed\": {\"fields\": [\"Profile picture\"]}}]',7,1),
(29,'2025-03-13 16:11:00.634039','4','Chat entre Saul e Boneco',1,'[{\"added\": {}}]',13,1),
(30,'2025-03-13 16:11:36.894568','4','Chat entre Saul e Boneco',2,'[]',13,1),
(31,'2025-03-13 16:15:22.898087','3','cmcoimbra@mail.com',2,'[{\"changed\": {\"fields\": [\"Primeiro nome\", \"Ultimo nome\"]}}]',7,1),
(32,'2025-03-13 17:11:51.175091','4','Chat entre Saul e Boneco',3,'',13,1),
(33,'2025-03-13 17:12:09.167848','5','Chat entre Boneco e Saul',1,'[{\"added\": {}}]',13,1),
(34,'2025-03-18 12:34:31.144781','2','[2025-03-18 12:34] Saul: ola',1,'[{\"added\": {}}]',12,1),
(35,'2025-03-19 15:24:48.027389','2','[2025-03-18 12:34] Saul: ola',2,'[]',12,1),
(36,'2025-03-19 15:24:59.660480','3','[2025-03-19 15:24] Boneco: Adeus',1,'[{\"added\": {}}]',12,1),
(37,'2025-03-26 16:46:37.282811','6','Chat entre Saul e Manuel Santos da',1,'[{\"added\": {}}]',13,1),
(38,'2025-03-27 16:24:03.165869','1','saul@mail.com',2,'[{\"changed\": {\"fields\": [\"Cidade\"]}}]',7,1),
(39,'2025-03-27 16:54:20.522451','3','Mode',1,'[{\"added\": {}}]',9,1),
(40,'2025-03-27 16:54:30.467203','3','Moda',2,'[{\"changed\": {\"fields\": [\"Nome\"]}}]',9,1),
(41,'2025-04-02 10:17:49.317706','7','Chat entre nigro1 e Saul',1,'[{\"added\": {}}]',13,1),
(42,'2025-04-02 14:24:15.871715','6','nigro1@racist.com',3,'',7,1),
(43,'2025-04-02 14:59:48.939177','8','Chat entre Saul e Vicente',1,'[{\"added\": {}}]',13,1),
(44,'2025-04-03 14:00:45.574785','7','vicenteconceicao2811@gmail.com',2,'[{\"changed\": {\"fields\": [\"Is staff\", \"Is superuser\"]}}]',7,1),
(46,'2025-04-03 14:08:15.687734','5','debug 2',1,'[{\"added\": {}}]',9,1),
(48,'2025-04-03 14:08:22.388887','5','debug 2',3,'',9,1),
(50,'2025-04-03 14:21:23.833194','8','Teste',1,'[{\"added\": {}}]',9,1),
(53,'2025-04-03 14:28:15.085152','11','Veículos',1,'[{\"added\": {}}]',9,1),
(54,'2025-04-03 14:28:44.786992','8','vicente@mail.com',3,'',7,1),
(55,'2025-04-03 14:39:52.874768','12','Animais',1,'[{\"added\": {}}]',9,1),
(56,'2025-04-03 14:41:10.697657','8','Teste',3,'',9,1),
(57,'2025-04-03 14:41:24.030259','20','Carro de NPC - Bom',2,'[{\"changed\": {\"fields\": [\"Categoria\"]}}]',8,1),
(58,'2025-04-03 14:41:29.434101','21','Carro bacano - Bom',2,'[{\"changed\": {\"fields\": [\"Categoria\"]}}]',8,1),
(59,'2025-04-03 14:41:41.205675','22','Mercedes S500 W220, V8 - Bom',2,'[{\"changed\": {\"fields\": [\"Categoria\"]}}]',8,1),
(60,'2025-04-03 14:41:45.886542','23','Carro triste :( - Bom',2,'[{\"changed\": {\"fields\": [\"Categoria\"]}}]',8,1),
(61,'2025-04-03 14:42:01.303026','24','El primo - Bom',2,'[{\"changed\": {\"fields\": [\"Categoria\"]}}]',8,1),
(62,'2025-04-03 14:42:15.753918','2','debug',3,'',9,1),
(63,'2025-04-03 14:44:17.031262','13','Lazer',1,'[{\"added\": {}}]',9,1),
(64,'2025-04-03 14:49:57.190331','14','Outros',1,'[{\"added\": {}}]',9,1),
(65,'2025-04-03 14:52:26.819965','15','Ferramentas',1,'[{\"added\": {}}]',9,1),
(66,'2025-04-03 14:53:26.325818','16','Decoração',1,'[{\"added\": {}}]',9,1),
(67,'2025-04-09 15:20:04.874810','21','Carro bacano - ⭐⭐⭐',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',8,1),
(68,'2025-04-09 16:31:14.110745','25','KTM Duke 125 - ⭐⭐',3,'',8,1),
(69,'2025-04-09 16:31:14.110888','26','KTM Duke 125 - ⭐⭐',3,'',8,1),
(70,'2025-04-09 16:31:14.111011','27','KTM Duke 125 - ⭐',3,'',8,1),
(71,'2025-04-09 16:35:05.823692','28','Produto teste - ⭐⭐⭐⭐',3,'',8,1),
(72,'2025-04-22 13:44:43.345216','20','Carro de NPC - ⭐',2,'[{\"changed\": {\"fields\": [\"Tipo venda\", \"Estado\"]}}]',8,1),
(73,'2025-04-22 13:44:49.717926','21','Carro bacano - ⭐⭐⭐',2,'[{\"changed\": {\"fields\": [\"Tipo venda\"]}}]',8,1),
(74,'2025-04-22 13:44:57.834141','22','Mercedes S500 W220, V8 - ⭐',2,'[{\"changed\": {\"fields\": [\"Tipo venda\", \"Estado\"]}}]',8,1),
(75,'2025-04-22 13:45:03.940486','23','Carro triste :( - ⭐',2,'[{\"changed\": {\"fields\": [\"Tipo venda\", \"Estado\"]}}]',8,1),
(76,'2025-04-22 13:45:09.096489','24','El primo - ⭐',2,'[{\"changed\": {\"fields\": [\"Tipo venda\", \"Estado\"]}}]',8,1),
(77,'2025-04-22 14:16:32.941249','9','Chat entre Saul e Vicente sobre El primo',3,'',13,1),
(78,'2025-04-22 14:16:32.941333','8','Chat entre Saul e Vicente sobre Teste venda direta',3,'',13,1),
(79,'2025-04-22 14:16:32.941375','6','Chat entre Saul e José Manuel sobre Teste venda direta',3,'',13,1),
(80,'2025-04-22 14:16:32.941416','5','Chat entre Boneco e Saul sobre Teste venda direta',3,'',13,1),
(81,'2025-04-23 14:19:38.249428','9','beatriz@gmail.com',2,'[{\"changed\": {\"fields\": [\"Ultimo nome\", \"Cidade\"]}}]',7,1),
(82,'2025-04-23 16:30:20.387456','12','Chat entre Beatriz e Saul sobre Carro triste :(',3,'',13,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(13,'chat','conversation'),
(12,'chat','message'),
(5,'contenttypes','contenttype'),
(9,'loja','categoria'),
(14,'loja','licitacao'),
(10,'loja','mensagens_de_contactos'),
(8,'loja','product'),
(11,'loja','productimage'),
(7,'loja','user'),
(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2025-02-13 15:42:16.117489'),
(2,'auth','0001_initial','2025-02-13 15:42:16.243239'),
(3,'admin','0001_initial','2025-02-13 15:42:16.274108'),
(4,'admin','0002_logentry_remove_auto_add','2025-02-13 15:42:16.280788'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-02-13 15:42:16.289422'),
(6,'contenttypes','0002_remove_content_type_name','2025-02-13 15:42:16.313387'),
(7,'auth','0002_alter_permission_name_max_length','2025-02-13 15:42:16.326875'),
(8,'auth','0003_alter_user_email_max_length','2025-02-13 15:42:16.336358'),
(9,'auth','0004_alter_user_username_opts','2025-02-13 15:42:16.340848'),
(10,'auth','0005_alter_user_last_login_null','2025-02-13 15:42:16.352691'),
(11,'auth','0006_require_contenttypes_0002','2025-02-13 15:42:16.353429'),
(12,'auth','0007_alter_validators_add_error_messages','2025-02-13 15:42:16.357904'),
(13,'auth','0008_alter_user_username_max_length','2025-02-13 15:42:16.367102'),
(14,'auth','0009_alter_user_last_name_max_length','2025-02-13 15:42:16.375390'),
(15,'auth','0010_alter_group_name_max_length','2025-02-13 15:42:16.383952'),
(16,'auth','0011_update_proxy_permissions','2025-02-13 15:42:16.388273'),
(17,'auth','0012_alter_user_first_name_max_length','2025-02-13 15:42:16.396769'),
(18,'sessions','0001_initial','2025-02-13 15:42:16.406648'),
(19,'loja','0001_initial','2025-02-14 14:01:03.559864'),
(20,'loja','0002_user_last_login_alter_user_email_alter_user_password','2025-02-14 14:25:38.305901'),
(21,'loja','0003_contactmessage','2025-02-17 10:26:04.224782'),
(22,'loja','0004_rename_contactmessage_mensagens_de_contactos','2025-02-17 10:34:25.697368'),
(23,'loja','0005_categoria_icon','2025-02-17 14:06:53.613338'),
(24,'loja','0006_alter_categoria_icon','2025-02-17 14:10:31.466108'),
(25,'loja','0007_product_user','2025-02-17 14:43:13.523753'),
(26,'loja','0008_remove_product_image_productimage','2025-02-17 15:42:17.601161'),
(27,'loja','0009_alter_product_preco','2025-02-18 13:15:14.072658'),
(28,'loja','0010_alter_productimage_image','2025-02-20 17:02:49.676461'),
(29,'loja','0011_alter_productimage_image','2025-02-27 15:35:17.047410'),
(32,'loja','0012_product_estado','2025-03-05 15:51:24.251577'),
(33,'loja','0013_user_profile_picture','2025-03-06 17:20:35.722661'),
(34,'loja','0014_user_is_active_user_is_staff_user_is_superuser','2025-03-06 18:13:06.213678'),
(35,'loja','0015_alter_user_profile_picture','2025-03-11 16:48:00.649455'),
(37,'chat','0001_initial','2025-03-12 17:27:56.966787'),
(38,'chat','0002_alter_conversation_user1_alter_conversation_user2_and_more','2025-03-13 16:10:48.601180'),
(39,'loja','0016_user_has_module_perms','2025-03-18 12:29:42.199678'),
(40,'loja','0017_remove_user_has_module_perms','2025-03-18 12:31:47.120503'),
(41,'loja','0018_user_biografia_user_cidade_user_cp_user_localidade','2025-03-18 13:15:21.194508'),
(42,'loja','0019_licitacao','2025-03-26 16:56:11.349359'),
(43,'loja','0020_alter_user_cidade','2025-03-27 16:23:35.563929'),
(44,'loja','0021_alter_user_telemovel','2025-04-08 14:29:45.228562'),
(45,'loja','0022_alter_product_estado','2025-04-09 14:49:32.044098'),
(46,'loja','0023_product_tipo_venda','2025-04-09 16:03:46.648113'),
(47,'loja','0024_product_fim_leilao_product_inicio_leilao','2025-04-09 16:25:40.559610'),
(48,'loja','0025_product_localidade','2025-04-14 14:23:27.272920'),
(49,'chat','0003_alter_conversation_unique_together_and_more','2025-04-22 13:52:54.913492'),
(50,'loja','0026_product_data_adicionado','2025-04-23 14:49:22.963484');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES
('0uigywjgqr7c83eiipec3v2d2w9znisk','eyJ1c2VyX2lkIjoyfQ:1tsmOp:zK-4N8HoJ3rYlMrarMo6jC0PykSxFFkR73WXJu9SMRo','2025-03-14 17:31:15.630563'),
('436e3emoq7tu9rlke9evxi5pi4868phz','eyJ1c2VyX2lkIjoxfQ:1twgYP:1K5b_WfYKCn0IQgPqehxigsDSqKnUYzMfXz1NPilKmc','2025-04-07 12:05:17.641018'),
('4fg7njqu7iu3v4pftj6rv7xr0e2szh9j','.eJxVjMsOwiAQRf-FtSFQXoNL934DGRiQqoGktCvjv2uTLnR7zzn3xQJuaw3byEuYiZ2ZZKffLWJ65LYDumO7dZ56W5c58l3hBx382ik_L4f7d1Bx1G9tkipGgFdosyxFO0JSCFEoN3kBepLKaCxUXEYBwnpEkKgjkCIrgNj7A933N84:1u0Lkl:Ckn6-H6pQNtnhkQNUglXhlT2A9TPIjyKIhGkoh6m7D4','2025-04-17 14:41:11.417160'),
('6oh0wiees9iqwwrl3k8zvmze9boc3ohf','.eJxVjsEOgyAYg9-F80JAUHGnZfc9Ayn-oGwOF9HTsncfJl48tv3a9MtyHNL2sf6NOLErI1Am3HbF-_nNLsxiW0e7Zb_YSIWQZ8-hf_m0B_REGubSSusSHd8RfqSZP2by0_1gTwMj8ljada9CLUyn0HgZgm7LEwXjhGqrThhdSVVrBAqthzCi6QAjoZ0hRY0wxH5_b_RDag:1u2X72:A73X_XK_3xNz5-1PNZFwm8Sqgkv5u_dMTGFqouPjpHs','2025-04-23 15:13:12.351568'),
('ckc9i7qz2yxhcnvnx0n83iefwvltfmw6','.eJxVjEEOwiAQRe_C2hCgAwWX7j0DGZhBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4kTiLIE6_W8L84LYDumO7zTLPbV2mJHdFHrTL60z8vBzu30HFXr-1YbIAyXEZAZQBrT2PztuUWCsFAZRmMIWDLYgBseiByCbOIZMbPIn3B9mkODc:1u7EgL:HFKaSsu5-Gv3IjvsfGxuwhQytKd1s3iFsrqvzggeY4A','2025-05-06 14:33:05.622886'),
('kvdijpz1gn16i1lyg389y6v6kjmcdexf','.eJxVjEEOwiAQAP_C2RB32xTw6N03EHYXpGogKe2p8e9K0oNeZyazKx-2NfutxcXPoi4K1OmXUeBnLF3II5R71VzLusyke6IP2_StSnxdj_ZvkEPLfWusI5azQxhAWFAmi4asOIbEBu1XI8WBrRUaDRqhEIcIk3OQEo3q_QHlbDhI:1u0LR7:ukJ6HL1-9y71cm6M75EM6ql3oR9E5zH2cx_UHiHcFLg','2025-04-17 14:20:53.524712'),
('px3ax17v5tcywy2aqmrj7ai4u7dzt4g5','eyJ1c2VyX2lkIjoxfQ:1tta1N:42PDVmnGxss3Imfnzr6iPdpy62j9sWce2tUKFrRGGpE','2025-03-16 22:30:21.445013'),
('sc56ddpveyuwxrxhez7crqvhid0jidol','.eJxVjMsOwiAQRf-FtSFQXoNL934DGRiQqoGktCvjv2uTLnR7zzn3xQJuaw3byEuYiZ2ZZKffLWJ65LYDumO7dZ56W5c58l3hBx382ik_L4f7d1Bx1G9tkipGgFdosyxFO0JSCFEoN3kBepLKaCxUXEYBwnpEkKgjkCIrgNj7A933N84:1u7cyS:4yfW37Mt7ZzdnhGcAmkKMTqR9RN_JlpOpr2K0QoSoVo','2025-05-07 16:29:24.761817'),
('tm2xpm46d9ajvzgu01xqkygg0bfwtzrg','.eJxVjMsOwiAQRf-FtSFYGIa6dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtKYSkUKFLFuzggBgzcXSYdUY6R2OB1ADGmYwjutFoCAoSa2KVSYF4fwDujjfe:1u0M6F:llKohG91PykA2G8ZwUEJNP1F8QkpOvl05U0RXYuVbCI','2025-04-17 15:03:23.107509'),
('twcctiky59axm0qils0drmnij8av9cv2','.eJxVjDsOwjAQBe_iGln-Z0NJzxkse3eNA8iR4qRC3B0ipYD2zcx7iZi2tcat8xInEmcRxOl3ywkf3HZA99Rus8S5rcuU5a7Ig3Z5nYmfl8P9O6ip12-taNQDEHhUrhgNyhs0WJzLniwyhwSgA0HmkG3R1hY1WPZADLqMwYn3B9owN7Y:1tzv9H:BnTB8H6K_XdbUdKpGDsym-qrHmWRRUTIAShCiEe-H9E','2025-04-16 10:16:43.309326');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loja_categoria`
--

DROP TABLE IF EXISTS `loja_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loja_categoria` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `icon` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_categoria`
--

LOCK TABLES `loja_categoria` WRITE;
/*!40000 ALTER TABLE `loja_categoria` DISABLE KEYS */;
INSERT INTO `loja_categoria` VALUES
(3,'Moda','uploads/categorias/Pedro-Santos.png'),
(11,'Veículos','uploads/categorias/car-front_PEOozT9.svg'),
(12,'Animais','uploads/categorias/gitlab.svg'),
(13,'Lazer','uploads/categorias/bullseye.svg'),
(14,'Outros','uploads/categorias/exclude.svg'),
(15,'Ferramentas','uploads/categorias/hammer.svg'),
(16,'Decoração','uploads/categorias/lamp.svg');
/*!40000 ALTER TABLE `loja_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loja_licitacao`
--

DROP TABLE IF EXISTS `loja_licitacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loja_licitacao` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `valor` decimal(10,2) NOT NULL,
  `licitado_a` datetime(6) NOT NULL,
  `produto_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `loja_licitacao_produto_id_72523346_fk_loja_product_id` (`produto_id`),
  KEY `loja_licitacao_user_id_ead856e0_fk_loja_user_id` (`user_id`),
  CONSTRAINT `loja_licitacao_produto_id_72523346_fk_loja_product_id` FOREIGN KEY (`produto_id`) REFERENCES `loja_product` (`id`),
  CONSTRAINT `loja_licitacao_user_id_ead856e0_fk_loja_user_id` FOREIGN KEY (`user_id`) REFERENCES `loja_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_licitacao`
--

LOCK TABLES `loja_licitacao` WRITE;
/*!40000 ALTER TABLE `loja_licitacao` DISABLE KEYS */;
INSERT INTO `loja_licitacao` VALUES
(1,11231.00,'2025-03-26 16:59:51.142417',21,1),
(2,12000.00,'2025-03-27 16:00:54.091137',21,1),
(3,13000.00,'2025-03-29 14:49:41.575985',21,1),
(4,10.00,'2025-04-01 10:23:35.077557',23,1),
(5,5.00,'2025-04-03 14:13:17.427581',22,7),
(6,5.00,'2025-04-03 14:13:34.741001',24,7),
(7,10.01,'2025-04-03 15:06:01.788298',23,7),
(8,10.00,'2025-04-09 15:08:31.042415',20,1),
(9,500000.00,'2025-04-09 16:33:37.023037',23,7),
(10,13100.00,'2025-04-13 08:54:01.185361',21,1),
(11,10.00,'2025-04-13 08:54:22.108373',22,1);
/*!40000 ALTER TABLE `loja_licitacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loja_mensagens_de_contactos`
--

DROP TABLE IF EXISTS `loja_mensagens_de_contactos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loja_mensagens_de_contactos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `mensagem` longtext NOT NULL,
  `data_envio` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_mensagens_de_contactos`
--

LOCK TABLES `loja_mensagens_de_contactos` WRITE;
/*!40000 ALTER TABLE `loja_mensagens_de_contactos` DISABLE KEYS */;
INSERT INTO `loja_mensagens_de_contactos` VALUES
(1,'Saul','saul@maildecontacto.com','Adorei','2025-02-17 10:35:28.703309'),
(2,'nigro1','nigro1@racist.com','nigga nigga nigga','2025-04-02 10:13:41.683372');
/*!40000 ALTER TABLE `loja_mensagens_de_contactos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loja_product`
--

DROP TABLE IF EXISTS `loja_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loja_product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(60) NOT NULL,
  `preco` decimal(7,2) NOT NULL,
  `descricao` varchar(250) DEFAULT NULL,
  `categoria_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `tipo_venda` varchar(10) NOT NULL,
  `fim_leilao` datetime(6) DEFAULT NULL,
  `inicio_leilao` datetime(6) DEFAULT NULL,
  `localidade` varchar(255) DEFAULT NULL,
  `data_adicionado` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `loja_product_categoria_id_95d83ee8_fk_loja_categoria_id` (`categoria_id`),
  KEY `loja_product_user_id_69b1f895_fk_loja_user_id` (`user_id`),
  CONSTRAINT `loja_product_categoria_id_95d83ee8_fk_loja_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `loja_categoria` (`id`),
  CONSTRAINT `loja_product_user_id_69b1f895_fk_loja_user_id` FOREIGN KEY (`user_id`) REFERENCES `loja_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_product`
--

LOCK TABLES `loja_product` WRITE;
/*!40000 ALTER TABLE `loja_product` DISABLE KEYS */;
INSERT INTO `loja_product` VALUES
(20,'Carro de NPC',2000.00,'Boa tarde, estou a vender o meu carro, não tem nada de interessante sobre ele',11,1,'1','leilao',NULL,NULL,NULL,'2025-04-23 14:49:22.947501'),
(21,'Carro bacano',900.00,'Carro mesmo muito confiável',11,1,'3','leilao',NULL,NULL,NULL,'2025-04-23 14:49:22.947501'),
(22,'Mercedes S500 W220, V8',10000.00,'Carro em hasta pública',11,3,'1','leilao',NULL,NULL,NULL,'2025-04-23 14:49:22.947501'),
(23,'Carro triste :(',500.85,'Carro ficou triste depois de bater com a cara',11,1,'1','leilao',NULL,NULL,NULL,'2025-04-23 14:49:22.947501'),
(24,'El primo',5000.00,'quem nao quer esta personagem?',12,7,'1','leilao',NULL,NULL,NULL,'2025-04-23 14:49:22.947501'),
(29,'Teste',7800.00,'Sofá em muito bom estado, acreditem. Tem algumas manchas, apenas vistas a luz ultravioleta',16,1,'4','leilao','2025-04-21 13:59:56.546833','2025-04-14 13:59:56.546833',NULL,'2025-04-23 14:49:22.947501'),
(30,'Teste venda direta',850.00,'Alguém me roubou os sofás... Estou muito triste, quem os encontrar recebe uma mini',14,1,'2','venda',NULL,NULL,NULL,'2025-04-23 14:49:22.947501');
/*!40000 ALTER TABLE `loja_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loja_productimage`
--

DROP TABLE IF EXISTS `loja_productimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loja_productimage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `loja_productimage_product_id_e9bb3c50_fk_loja_product_id` (`product_id`),
  CONSTRAINT `loja_productimage_product_id_e9bb3c50_fk_loja_product_id` FOREIGN KEY (`product_id`) REFERENCES `loja_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_productimage`
--

LOCK TABLES `loja_productimage` WRITE;
/*!40000 ALTER TABLE `loja_productimage` DISABLE KEYS */;
INSERT INTO `loja_productimage` VALUES
(7,'uploads/products/20/dsc_5073.png',20),
(8,'uploads/products/20/muleta.png',20),
(9,'uploads/products/21/a67484147bae5b62c7b522653ee14229-1-600x630.jpg',21),
(10,'uploads/products/21/honda_civic_1995_honda_civic_vtec_1_5i_ls_900_euro_7390126691242405423.jpg',21),
(11,'uploads/products/22/Carro-em-Hasta-Publica-7-1620x1080.jpg',22),
(12,'uploads/products/22/Carro-em-Hasta-Publica-3-scaled_1920x1080_acf_cropped-1095x616.jpg',22),
(13,'uploads/products/22/Carro-em-Hasta-Publica-1-1620x1080.jpg',22),
(14,'uploads/products/23/1741891249639.jpg',23),
(15,'uploads/products/23/1741891249631.jpg',23),
(16,'uploads/products/23/Untitled.jpg',23),
(17,'uploads/products/24/skin-highlight-el-primo-brawl-stars-4k-pv4pz0hnrp7lig56.jpg',24),
(24,'uploads/products/29/sofa4.jpg',29),
(25,'uploads/products/29/sofa3.jpg',29),
(26,'uploads/products/29/sofa2.jpg',29),
(27,'uploads/products/29/sofa1.jpg',29),
(28,'uploads/products/30/sofa1.jpg',30);
/*!40000 ALTER TABLE `loja_productimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loja_user`
--

DROP TABLE IF EXISTS `loja_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loja_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `primeiro_nome` varchar(50) NOT NULL,
  `ultimo_nome` varchar(50) NOT NULL,
  `telemovel` varchar(10) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(255) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `biografia` longtext DEFAULT NULL,
  `cidade` varchar(255) DEFAULT NULL,
  `cp` varchar(20) DEFAULT NULL,
  `localidade` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `loja_user_email_5a75d4a1_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_user`
--

LOCK TABLES `loja_user` WRITE;
/*!40000 ALTER TABLE `loja_user` DISABLE KEYS */;
INSERT INTO `loja_user` VALUES
(1,'Saul','Marques','926382343','saul@mail.com','pbkdf2_sha256$870000$xWPscGViYoAIDYCvzEW1xF$XXzth5C6Fmiw+mhmPX8IROiYG9It3nETCrB/a02BeO0=','2025-04-23 16:29:24.758281','uploads/profiles/1/peruca-70-s-homem_VS4acnR.jpg',1,1,1,'Sou o admin desta cena toda','coimbra',NULL,NULL),
(2,'Boneco','Dummy','969696969','boneco@mail.com','pbkdf2_sha256$870000$0jxAQSbmvSxA76D5fZDao4$IUr+7zEeCLOvAomSeCmFyNYgNh9iu4l2ds27UWA10UQ=',NULL,'uploads/profiles/2/perucadohenrique.jpg',1,0,0,NULL,NULL,NULL,NULL),
(3,'José Manuel','Silva','969696969','cmcoimbra@mail.com','pbkdf2_sha256$870000$NaoMOrSoCyG7rj7llqaxIV$J1tJCk7G6vIlFQqCSIHMeCVBKkL2OK8ui1cwifcWzco=','2025-04-23 15:07:29.341811','uploads/profiles/3/Coimbra_-_Jose_Manuel_Silva.png',1,0,0,'Camera Municipal de Coimbra',NULL,NULL,NULL),
(4,'Saul','Marques','926382343','saul_marques10@hotmail.com','pbkdf2_sha256$870000$qpl1YTqivJpo038w0Y1sXQ$eZxL25+xpb1C4LPKizdg0nZIyzBC5z+UK5nWX95b+sY=','2025-04-01 09:46:58.491527','',1,1,1,NULL,NULL,NULL,NULL),
(5,'Teste','Teste 2','858585858','teste@mail.com','pbkdf2_sha256$870000$vsH41qoY5Cd9EciwXTrO5b$hkUazi57bt/tkqc7yKsj7DHBJmNvcw2jBOL/jOpmq2s=','2025-04-01 09:55:59.665048','',1,0,0,NULL,NULL,NULL,NULL),
(7,'Vicente','Santos','910452535','vicenteconceicao2811@gmail.com','pbkdf2_sha256$870000$MDJyUYzAXNKjRBmKlinTwr$RVYv3zp4PWXlL+DW8IWK8LBSC6vX5HcTLikRS/0WduI=','2025-04-03 15:03:23.104869','',1,1,1,'None',NULL,NULL,NULL),
(9,'Beatriz','Vilão',NULL,'beatriz@gmail.com','pbkdf2_sha256$870000$SdGcKrYnHKAUOC8E9rHLCM$98LAdFr/QxX+YXR7hiKXsHUPcJc3Xpqh3np10I7ldg4=','2025-04-22 14:33:05.617646','uploads/profiles/9/beatriz.jpg',1,0,0,'Sou a Beatriz e gosto de animais! <3','coimbra',NULL,NULL);
/*!40000 ALTER TABLE `loja_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-04-24 16:28:59
