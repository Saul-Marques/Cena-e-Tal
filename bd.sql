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
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_conversation`
--

LOCK TABLES `chat_conversation` WRITE;
/*!40000 ALTER TABLE `chat_conversation` DISABLE KEYS */;
INSERT INTO `chat_conversation` VALUES
(20,'2025-05-15 14:37:15.709409',3,1,3),
(21,'2025-05-22 14:13:59.929796',3,1,2),
(22,'2025-06-01 06:44:33.100667',3,5,8),
(23,'2025-06-03 08:44:58.532885',6,4,9);
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
) ENGINE=InnoDB AUTO_INCREMENT=292 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_message`
--

LOCK TABLES `chat_message` WRITE;
/*!40000 ALTER TABLE `chat_message` DISABLE KEYS */;
INSERT INTO `chat_message` VALUES
(288,'boas','2025-05-22 01:52:04.394994',20,3),
(289,'Boas, boa noite','2025-05-22 01:52:28.505701',20,1),
(290,'Podes me oferecer o Mercedes? Tenho 10€ e um big mac!','2025-06-01 06:44:52.389612',22,3),
(291,'nga','2025-06-03 08:46:03.314055',23,4);
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
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES
(100,'2025-05-14 17:33:09.103589','2','saul_marques10@hotmail.com',3,'',7,1),
(101,'2025-05-27 15:19:32.796346','5','Produto com imagem manhosa - Mau',3,'',8,1),
(102,'2025-05-27 15:28:51.631782','6','Produto com imagem manhosa - Mau',3,'',8,1),
(103,'2025-05-27 15:28:51.631899','7','Produto com imagem manhosa - Mau',3,'',8,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
(50,'loja','0026_product_data_adicionado','2025-04-23 14:49:22.963484'),
(51,'loja','0027_user_groups_user_user_permissions','2025-05-08 14:31:15.304436'),
(52,'loja','0028_product_is_active','2025-05-13 15:54:10.517938'),
(53,'loja','0029_alter_product_estado','2025-05-13 16:25:53.844809');
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
('5psjxag3b13d9x4gv3oxonux2sp1ffum','.eJxVjDsOwjAQRO_iGlnGP7SU9JzBWnt3cQA5UpxUEXcnkVJAOfPezKoSLnNNS-cpDaSuyqnTb5exvLjtgJ7YHqMuY5unIetd0Qft-j4Sv2-H-3dQsddtHVgMOYhgUKw4IBM9e0MYyEcjkQSNsxyLRSEokItH3vLljJIhkPp8Afo4OPM:1uNCW8:DgLnnq8IhjOZ0ReyqTk7l_tCorVnhGElhjTscngTQM4','2025-06-19 15:28:32.357122'),
('60d1lm10e1d3q3ckzgl3rrcubzkttbsn','.eJxVjMsOwiAQRf-FtSFD5VFcuu83kBkYpGogKe3K-O_apAvd3nPOfYmA21rC1nkJcxIXocTpdyOMD647SHestyZjq-syk9wVedAup5b4eT3cv4OCvXxrQ9ECMUdNzqGKpLIZB9DKoCECdJYtgB8x66xT8uTteUD2ng0kh1m8P_u-OIs:1uHlyY:bYXxnMrZyG482eOcnFRBv0-EwueJc4wtFlz1EGMZHOU','2025-06-04 16:07:26.668144'),
('6oh0wiees9iqwwrl3k8zvmze9boc3ohf','.eJxVjsEOgyAYg9-F80JAUHGnZfc9Ayn-oGwOF9HTsncfJl48tv3a9MtyHNL2sf6NOLErI1Am3HbF-_nNLsxiW0e7Zb_YSIWQZ8-hf_m0B_REGubSSusSHd8RfqSZP2by0_1gTwMj8ljada9CLUyn0HgZgm7LEwXjhGqrThhdSVVrBAqthzCi6QAjoZ0hRY0wxH5_b_RDag:1u2X72:A73X_XK_3xNz5-1PNZFwm8Sqgkv5u_dMTGFqouPjpHs','2025-04-23 15:13:12.351568'),
('ckc9i7qz2yxhcnvnx0n83iefwvltfmw6','.eJxVjEEOwiAQRe_C2hCgAwWX7j0DGZhBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4kTiLIE6_W8L84LYDumO7zTLPbV2mJHdFHrTL60z8vBzu30HFXr-1YbIAyXEZAZQBrT2PztuUWCsFAZRmMIWDLYgBseiByCbOIZMbPIn3B9mkODc:1u7EgL:HFKaSsu5-Gv3IjvsfGxuwhQytKd1s3iFsrqvzggeY4A','2025-05-06 14:33:05.622886'),
('cn7swkpaeuee52mq0sezronqr8yxp963','.eJxVjMsOwiAQRf-FtSFD5VFcuu83kBkYpGogKe3K-O_apAvd3nPOfYmA21rC1nkJcxIXocTpdyOMD647SHestyZjq-syk9wVedAup5b4eT3cv4OCvXxrQ9ECMUdNzqGKpLIZB9DKoCECdJYtgB8x66xT8uTteUD2ng0kh1m8P_u-OIs:1uHv5z:4j3pDaSof3p5EJkfLb1oNps62re3wx05SKiLak0PrEU','2025-06-05 01:51:43.992035'),
('dezcn5nn173w9e6mpn8wj8juja3jm3ff','.eJxVjMsOwiAQRf-FtSFYGIa6dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtKYSkUKFLFuzggBgzcXSYdUY6R2OB1ADGmYwjutFoCAoSa2KVSYF4fwDujjfe:1uChP6:S4IFriCsLG-sgyHnZgCa3DdJhmXMZaSxWSmfWNPskuE','2025-05-21 16:13:52.052972'),
('hbtf7po877unacjqhw7v2pm5x7j1kk1f','.eJxVjMsOwiAQRf-FtSFYGIa6dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtKYSkUKFLFuzggBgzcXSYdUY6R2OB1ADGmYwjutFoCAoSa2KVSYF4fwDujjfe:1uA8kp:nUhXl-aZYv7WftjLwqdg1hMOXUuIytFkH8UMzv_YCmM','2025-05-14 14:49:43.282707'),
('j69ji7a0wxn8w279z2gtywipa73r6obt','.eJxVjDEOwjAMRe-SGUUxpm7CyM4ZIjtOSQGlUtNOiLtDpQ6w_vfef5nI61Li2vIcRzVnA84cfkfh9Mh1I3rneptsmuoyj2I3xe602euk-XnZ3b-Dwq186yACkhDxJBQEvAqLknZ0JFQIEiBJJvUheICuz-z6waUBQYkZkzfvDxkiOI4:1uChPt:U88LYs59QlANxsOMyajYKfOXQHR24FXmvFJnJ-gSI-s','2025-05-21 16:14:41.887600'),
('j99h90kuyullsjuairge1wn4xphwkfrc','.eJxVjMsOwiAQRf-FtSFD5VFcuu83kBkYpGogKe3K-O_apAvd3nPOfYmA21rC1nkJcxIXocTpdyOMD647SHestyZjq-syk9wVedAup5b4eT3cv4OCvXxrQ9ECMUdNzqGKpLIZB9DKoCECdJYtgB8x66xT8uTteUD2ng0kh1m8P_u-OIs:1uFaa2:LmSgjWVygVRs-D5zhM4B2Tv-Bo3DcVRejlyinRfJ9Ko','2025-05-29 15:33:06.116411'),
('kvdijpz1gn16i1lyg389y6v6kjmcdexf','.eJxVjEEOwiAQAP_C2RB32xTw6N03EHYXpGogKe2p8e9K0oNeZyazKx-2NfutxcXPoi4K1OmXUeBnLF3II5R71VzLusyke6IP2_StSnxdj_ZvkEPLfWusI5azQxhAWFAmi4asOIbEBu1XI8WBrRUaDRqhEIcIk3OQEo3q_QHlbDhI:1u0LR7:ukJ6HL1-9y71cm6M75EM6ql3oR9E5zH2cx_UHiHcFLg','2025-04-17 14:20:53.524712'),
('kx7ekrm5glnwgd4sh7cgt7qlctlqesxu','.eJxVjEEOwiAQRe_C2hBgOnVw6d4zEBgmUjWQlHZlvLtt0oVu_3v_vVWI61LC2mUOU1YXNarT75YiP6XuID9ivTfNrS7zlPSu6IN2fWtZXtfD_QuU2Mv2lgRIhtA4SMkN3g7sLRBZztaDIdpSYpMjRkRCYIijN5BR5OwjG_X5ArvmNxI:1uMNGB:Asz83A9_ZYhczlnemid5ZpiNArjSYY6vLI_o-mWHAHk','2025-06-17 08:44:39.939023'),
('llgf31ayrrj55nbcizpv3fb9x7p2w43m','.eJxVjDEOwyAUQ-_CXCHgQ4CO3XMGBHwoaSuQQjJVvXuJlKFdLNnP9ps4v2_F7T2tbkFyJZyTy28YfHymehB8-HpvNLa6rUugR4WetNO5YXrdzu7fQfG9jLVkFpiaWIYspBYMFBcCsxEY0VhrjFVhskGbYcEkPTR6rrSEzMcMyOcLy6Y2nw:1uChYK:oVpfM69kDPUyouqMoSBy8KDjjF1887pqgAuNgvafjIM','2025-05-21 16:23:24.996315'),
('niy1tbv35f890gk3j74rpaf3vu31yb40','.eJxVjMsOwiAQRf-FtSFD5VFcuu83kBkYpGogKe3K-O_apAvd3nPOfYmA21rC1nkJcxIXocTpdyOMD647SHestyZjq-syk9wVedAup5b4eT3cv4OCvXxrQ9ECMUdNzqGKpLIZB9DKoCECdJYtgB8x66xT8uTteUD2ng0kh1m8P_u-OIs:1uOerp:vJheUIc6bAAUYSYmDj78bQu8YwPHD-keRQaKCtPoA5U','2025-06-23 15:56:57.034750'),
('px3ax17v5tcywy2aqmrj7ai4u7dzt4g5','eyJ1c2VyX2lkIjoxfQ:1tta1N:42PDVmnGxss3Imfnzr6iPdpy62j9sWce2tUKFrRGGpE','2025-03-16 22:30:21.445013'),
('tm2xpm46d9ajvzgu01xqkygg0bfwtzrg','.eJxVjMsOwiAQRf-FtSFYGIa6dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguAsXpd2MKj1R3EO9Ub02GVtdlZrkr8qBdTi2m5_Vw_w4K9fKtKYSkUKFLFuzggBgzcXSYdUY6R2OB1ADGmYwjutFoCAoSa2KVSYF4fwDujjfe:1u0M6F:llKohG91PykA2G8ZwUEJNP1F8QkpOvl05U0RXYuVbCI','2025-04-17 15:03:23.107509'),
('twcctiky59axm0qils0drmnij8av9cv2','.eJxVjDsOwjAQBe_iGln-Z0NJzxkse3eNA8iR4qRC3B0ipYD2zcx7iZi2tcat8xInEmcRxOl3ywkf3HZA99Rus8S5rcuU5a7Ig3Z5nYmfl8P9O6ip12-taNQDEHhUrhgNyhs0WJzLniwyhwSgA0HmkG3R1hY1WPZADLqMwYn3B9owN7Y:1tzv9H:BnTB8H6K_XdbUdKpGDsym-qrHmWRRUTIAShCiEe-H9E','2025-04-16 10:16:43.309326'),
('uhrc28f5nl68kjjlbr8qxekhxr9g0ybb','.eJxVjMEOwiAQBf-Fs2moLWzryXj3G8gCS0ERTGnjwfjv0qSXXt_MvC8rYUrrW9ELQ2QXtnj65Oiyc8EEjO112kBj8oudmMJ18WotNKtgq9wfN43mSWkD9oFpyrVKyxx0synNTktzz5bibXcPBx6LrzXSCEZq5KAFCssdIIEciHTfDSMAh_FssZPEN0N2ugXhiEsQtaou-_0BI6hIHQ:1uA9Kt:xQ4sAia8PQ7zjsydHuAPRTiAlwHXXYHhwY9y3xGRORc','2025-05-14 15:26:59.900155');
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_categoria`
--

LOCK TABLES `loja_categoria` WRITE;
/*!40000 ALTER TABLE `loja_categoria` DISABLE KEYS */;
INSERT INTO `loja_categoria` VALUES
(3,'Moda','uploads/categorias/t-shirt.png'),
(11,'Veículos','uploads/categorias/car-front_PEOozT9.svg'),
(12,'Animais','uploads/categorias/animais_Q3d2OtQ.png'),
(13,'Lazer','uploads/categorias/bullseye.svg'),
(14,'Outros','uploads/categorias/outros.png'),
(15,'Ferramentas','uploads/categorias/nut.svg'),
(16,'Decoração','uploads/categorias/lamp.svg'),
(17,'Entretenimento','uploads/categorias/dpad.svg');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_licitacao`
--

LOCK TABLES `loja_licitacao` WRITE;
/*!40000 ALTER TABLE `loja_licitacao` DISABLE KEYS */;
INSERT INTO `loja_licitacao` VALUES
(1,100.00,'2025-06-01 06:44:26.134787',8,3),
(2,50.00,'2025-06-01 07:00:22.263495',9,1),
(3,51.00,'2025-06-03 08:44:55.740640',9,6);
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
(1,'Saul','saul@maildecontacto.com','Adorei','2025-02-17 10:35:28.703309');
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
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `loja_product_categoria_id_95d83ee8_fk_loja_categoria_id` (`categoria_id`),
  KEY `loja_product_user_id_69b1f895_fk_loja_user_id` (`user_id`),
  CONSTRAINT `loja_product_categoria_id_95d83ee8_fk_loja_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `loja_categoria` (`id`),
  CONSTRAINT `loja_product_user_id_69b1f895_fk_loja_user_id` FOREIGN KEY (`user_id`) REFERENCES `loja_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_product`
--

LOCK TABLES `loja_product` WRITE;
/*!40000 ALTER TABLE `loja_product` DISABLE KEYS */;
INSERT INTO `loja_product` VALUES
(2,'Produto Inicial',100.00,'Produto inical para testar as fixtures, será uma venda direta',14,1,'5','venda',NULL,NULL,'lisboa','2025-05-14 17:35:43.344690',1),
(3,'Produto Inicial 2',101.00,'Produto inicial para testar os leiloes e categorias',15,1,'4','leilao','2025-05-21 17:36:36.958966','2025-05-14 17:36:36.958966','castelo_branco','2025-05-14 17:36:36.959965',0),
(4,'Pokemons',58.00,'Pokemons à venda ou para alugar',12,3,'3','venda',NULL,NULL,'coimbra','2025-05-15 14:42:34.570638',1),
(8,'Mercedes S500 W220 V8',10000.00,'Automóvel em hasta pública',11,5,'3','leilao','2025-06-08 06:30:10.302170','2025-06-01 06:30:10.302170','coimbra','2025-06-01 06:30:10.302765',1),
(9,'Furão não registado',200.00,'Furão não é legal, deve ter imigrado do norte de África, através de barco',12,4,'4','leilao','2025-06-08 06:46:56.961291','2025-06-01 06:46:56.961291','coimbra','2025-06-01 06:46:56.961911',0),
(10,'Cão',20.00,'Cão mau',12,4,'1','venda',NULL,NULL,'coimbra','2025-06-05 14:00:24.585819',1),
(11,'Bom preço',1000.00,'Seat Ibiza 6k, conta com 318.000 km.\r\nCarro em estado modesto de conservação.\r\nCarro de garagem desde há um ano para cá. ',11,3,'3','venda',NULL,NULL,'coimbra','2025-06-05 14:03:30.503554',1),
(12,'Carro mal estacionado',500.00,'Este carro está mal estacionado em via pública, por favor alguém o venha cá buscar.',11,5,'1','leilao','2025-06-12 15:27:51.745752','2025-06-05 15:27:51.745752','coimbra','2025-06-05 15:27:51.746536',1),
(13,'Sofá mal parado',200.00,'Este sofá está aqui a ocupar espaço, por favor venham buscar...',16,3,'3','venda',NULL,NULL,'aveiro','2025-06-05 15:29:19.305267',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_productimage`
--

LOCK TABLES `loja_productimage` WRITE;
/*!40000 ALTER TABLE `loja_productimage` DISABLE KEYS */;
INSERT INTO `loja_productimage` VALUES
(3,'uploads/products/2/produto_teste.png',2),
(4,'uploads/products/3/aguabenta.jpg',3),
(5,'uploads/products/4/cover6.gif',4),
(8,'uploads/products/8/Carro-em-Hasta-Publica-3-scaled_1920x1080_acf_cropped-1095x616.jpg',8),
(9,'uploads/products/8/Carro-em-Hasta-Publica-1-1620x1080.jpg',8),
(10,'uploads/products/8/Carro-em-Hasta-Publica-7-1620x1080.jpg',8),
(11,'uploads/products/9/furao1.jpg',9),
(12,'uploads/products/9/furao2.jpg',9),
(13,'uploads/products/10/beatriz.jpg',10),
(14,'uploads/products/11/465574201_3850455068500096_343345367352257547_n.jpg',11),
(15,'uploads/products/11/a67484147bae5b62c7b522653ee14229-1-600x630.jpg',11),
(16,'uploads/products/12/465541280_10226387419460389_8685852876173240736_n.jpg',12),
(17,'uploads/products/13/sofa1.jpg',13),
(18,'uploads/products/13/sofa3.jpg',13),
(19,'uploads/products/13/sofa2.jpg',13),
(20,'uploads/products/13/sofa4.jpg',13);
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_user`
--

LOCK TABLES `loja_user` WRITE;
/*!40000 ALTER TABLE `loja_user` DISABLE KEYS */;
INSERT INTO `loja_user` VALUES
(1,'Admin','Cena&Tal','926382343','projetopdi@mail.com','pbkdf2_sha256$870000$fX57qGbSDSJK6zYinRBLoS$fwKWIxX3qlmCKuGY2fkdwZoZ+bOJVW0ZScn3CiCd+zE=','2025-06-09 15:56:57.023987','uploads/profiles/1/admin.png',1,1,1,'Sou o admin do Cena&Tal','coimbra',NULL,NULL),
(3,'Saul','Marques',NULL,'saul@mail.com','pbkdf2_sha256$870000$GgPAyI6O3ilsWF99r3TXCJ$Qs9F5ivIZm6Mw9/cXo++hnH4l9ujTpGWpxuP1FmQPnA=','2025-06-05 15:28:32.351016','uploads/profiles/3/peruca-70-s-homem.jpg',1,0,0,'Já fui o admin, agora não sou...','coimbra',NULL,NULL),
(4,'Beatriz','Vilão','938499457','beatriz@mail.com','pbkdf2_sha256$870000$8js43b8KefUQgNsmkEjNYk$A+ZIBZX9SkYUYnNCYCruixIEKf/oEz9lsRkzJ2s+1e4=','2025-06-03 08:45:04.051101','uploads/profiles/4/Kookaburra-best.jpeg',1,0,0,'Boas, gosto de animais','coimbra',NULL,NULL),
(5,'José Manuel','Silva','969696969','cmcoimbra@mail.com','pbkdf2_sha256$870000$il32tRi84gCMrYwnFZx51Q$I/HWAFHkvKk2WN3hoHRxbBAUeqTUicT/REPRLer5HCo=','2025-06-05 15:26:41.279865','uploads/profiles/5/Coimbra_-_Jose_Manuel_Silva_8NVPGUq.png',1,0,0,'Camera de Coimbra, vendemos mercedes','coimbra',NULL,NULL),
(6,'Ze','Cataerva','','zecataerva@gmail.com','pbkdf2_sha256$870000$njHs9gVHH9xiRmbIvN4Pam$zOIP6S3VxBMAjwFZZRw3nArIscLe0Sx71Kjw7AYO9wU=','2025-06-03 08:44:39.933604','',1,0,0,NULL,'cidade',NULL,NULL);
/*!40000 ALTER TABLE `loja_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loja_user_groups`
--

DROP TABLE IF EXISTS `loja_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loja_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `loja_user_groups_user_id_group_id_ae5d1744_uniq` (`user_id`,`group_id`),
  KEY `loja_user_groups_group_id_e26e34b0_fk_auth_group_id` (`group_id`),
  CONSTRAINT `loja_user_groups_group_id_e26e34b0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `loja_user_groups_user_id_6bda011a_fk_loja_user_id` FOREIGN KEY (`user_id`) REFERENCES `loja_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_user_groups`
--

LOCK TABLES `loja_user_groups` WRITE;
/*!40000 ALTER TABLE `loja_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `loja_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loja_user_user_permissions`
--

DROP TABLE IF EXISTS `loja_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loja_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `loja_user_user_permissions_user_id_permission_id_be22a674_uniq` (`user_id`,`permission_id`),
  KEY `loja_user_user_permi_permission_id_a741ce5a_fk_auth_perm` (`permission_id`),
  CONSTRAINT `loja_user_user_permi_permission_id_a741ce5a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `loja_user_user_permissions_user_id_f4843159_fk_loja_user_id` FOREIGN KEY (`user_id`) REFERENCES `loja_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja_user_user_permissions`
--

LOCK TABLES `loja_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `loja_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `loja_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-06-09 17:13:18
