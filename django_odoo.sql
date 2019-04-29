/*
 Navicat Premium Data Transfer

 Source Server         : local-mysql57
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : localhost:3306
 Source Schema         : django_odoo

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : 65001

 Date: 29/04/2019 20:53:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account_accountaccount
-- ----------------------------
DROP TABLE IF EXISTS `account_accountaccount`;
CREATE TABLE `account_accountaccount`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `short_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `account_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `usage_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `account_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `account_bank` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `account_card` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `belongs_user_id` int(11) NULL DEFAULT NULL,
  `company_id` int(11) NOT NULL,
  `create_user_id` int(11) NULL DEFAULT NULL,
  `partner_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `account_accountaccou_belongs_user_id_6fe53d93_fk_base_base`(`belongs_user_id`) USING BTREE,
  INDEX `account_accountaccount_company_id_220a0818_fk_base_company_id`(`company_id`) USING BTREE,
  INDEX `account_accountaccou_create_user_id_4b8ccbea_fk_base_base`(`create_user_id`) USING BTREE,
  INDEX `account_accountaccount_partner_id_466712b9_fk_base_partner_id`(`partner_id`) USING BTREE,
  CONSTRAINT `account_accountaccou_belongs_user_id_6fe53d93_fk_base_base` FOREIGN KEY (`belongs_user_id`) REFERENCES `base_baseuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `account_accountaccou_create_user_id_4b8ccbea_fk_base_base` FOREIGN KEY (`create_user_id`) REFERENCES `base_baseuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `account_accountaccount_company_id_220a0818_fk_base_company_id` FOREIGN KEY (`company_id`) REFERENCES `base_company` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `account_accountaccount_partner_id_466712b9_fk_base_partner_id` FOREIGN KEY (`partner_id`) REFERENCES `base_partner` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 133 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (8, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (9, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (10, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (11, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (12, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (13, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (14, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (15, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (16, 'Can add periodic tasks', 6, 'add_periodictasks');
INSERT INTO `auth_permission` VALUES (17, 'Can change periodic tasks', 6, 'change_periodictasks');
INSERT INTO `auth_permission` VALUES (18, 'Can delete periodic tasks', 6, 'delete_periodictasks');
INSERT INTO `auth_permission` VALUES (19, 'Can add interval', 7, 'add_intervalschedule');
INSERT INTO `auth_permission` VALUES (20, 'Can change interval', 7, 'change_intervalschedule');
INSERT INTO `auth_permission` VALUES (21, 'Can delete interval', 7, 'delete_intervalschedule');
INSERT INTO `auth_permission` VALUES (22, 'Can add task', 8, 'add_taskstate');
INSERT INTO `auth_permission` VALUES (23, 'Can change task', 8, 'change_taskstate');
INSERT INTO `auth_permission` VALUES (24, 'Can delete task', 8, 'delete_taskstate');
INSERT INTO `auth_permission` VALUES (25, 'Can add task state', 9, 'add_taskmeta');
INSERT INTO `auth_permission` VALUES (26, 'Can change task state', 9, 'change_taskmeta');
INSERT INTO `auth_permission` VALUES (27, 'Can delete task state', 9, 'delete_taskmeta');
INSERT INTO `auth_permission` VALUES (28, 'Can add worker', 10, 'add_workerstate');
INSERT INTO `auth_permission` VALUES (29, 'Can change worker', 10, 'change_workerstate');
INSERT INTO `auth_permission` VALUES (30, 'Can delete worker', 10, 'delete_workerstate');
INSERT INTO `auth_permission` VALUES (31, 'Can add periodic task', 11, 'add_periodictask');
INSERT INTO `auth_permission` VALUES (32, 'Can change periodic task', 11, 'change_periodictask');
INSERT INTO `auth_permission` VALUES (33, 'Can delete periodic task', 11, 'delete_periodictask');
INSERT INTO `auth_permission` VALUES (34, 'Can add crontab', 12, 'add_crontabschedule');
INSERT INTO `auth_permission` VALUES (35, 'Can change crontab', 12, 'change_crontabschedule');
INSERT INTO `auth_permission` VALUES (36, 'Can delete crontab', 12, 'delete_crontabschedule');
INSERT INTO `auth_permission` VALUES (37, 'Can add saved group result', 13, 'add_tasksetmeta');
INSERT INTO `auth_permission` VALUES (38, 'Can change saved group result', 13, 'change_tasksetmeta');
INSERT INTO `auth_permission` VALUES (39, 'Can delete saved group result', 13, 'delete_tasksetmeta');
INSERT INTO `auth_permission` VALUES (40, 'Can add group object permission', 14, 'add_groupobjectpermission');
INSERT INTO `auth_permission` VALUES (41, 'Can change group object permission', 14, 'change_groupobjectpermission');
INSERT INTO `auth_permission` VALUES (42, 'Can delete group object permission', 14, 'delete_groupobjectpermission');
INSERT INTO `auth_permission` VALUES (43, 'Can add user object permission', 15, 'add_userobjectpermission');
INSERT INTO `auth_permission` VALUES (44, 'Can change user object permission', 15, 'change_userobjectpermission');
INSERT INTO `auth_permission` VALUES (45, 'Can delete user object permission', 15, 'delete_userobjectpermission');
INSERT INTO `auth_permission` VALUES (46, 'Can add user operation log', 16, 'add_useroperationlog');
INSERT INTO `auth_permission` VALUES (47, 'Can change user operation log', 16, 'change_useroperationlog');
INSERT INTO `auth_permission` VALUES (48, 'Can delete user operation log', 16, 'delete_useroperationlog');
INSERT INTO `auth_permission` VALUES (49, 'Can add partner', 17, 'add_partner');
INSERT INTO `auth_permission` VALUES (50, 'Can change partner', 17, 'change_partner');
INSERT INTO `auth_permission` VALUES (51, 'Can delete partner', 17, 'delete_partner');
INSERT INTO `auth_permission` VALUES (52, 'Can add sequence', 18, 'add_sequence');
INSERT INTO `auth_permission` VALUES (53, 'Can change sequence', 18, 'change_sequence');
INSERT INTO `auth_permission` VALUES (54, 'Can delete sequence', 18, 'delete_sequence');
INSERT INTO `auth_permission` VALUES (55, 'Can add company', 19, 'add_company');
INSERT INTO `auth_permission` VALUES (56, 'Can change company', 19, 'change_company');
INSERT INTO `auth_permission` VALUES (57, 'Can delete company', 19, 'delete_company');
INSERT INTO `auth_permission` VALUES (58, 'Can add department', 20, 'add_department');
INSERT INTO `auth_permission` VALUES (59, 'Can change department', 20, 'change_department');
INSERT INTO `auth_permission` VALUES (60, 'Can delete department', 20, 'delete_department');
INSERT INTO `auth_permission` VALUES (61, 'Can add province', 21, 'add_province');
INSERT INTO `auth_permission` VALUES (62, 'Can change province', 21, 'change_province');
INSERT INTO `auth_permission` VALUES (63, 'Can delete province', 21, 'delete_province');
INSERT INTO `auth_permission` VALUES (64, 'Can add base job', 22, 'add_basejob');
INSERT INTO `auth_permission` VALUES (65, 'Can change base job', 22, 'change_basejob');
INSERT INTO `auth_permission` VALUES (66, 'Can delete base job', 22, 'delete_basejob');
INSERT INTO `auth_permission` VALUES (67, 'Can add base city', 23, 'add_basecity');
INSERT INTO `auth_permission` VALUES (68, 'Can change base city', 23, 'change_basecity');
INSERT INTO `auth_permission` VALUES (69, 'Can delete base city', 23, 'delete_basecity');
INSERT INTO `auth_permission` VALUES (70, 'Can add file object', 24, 'add_fileobject');
INSERT INTO `auth_permission` VALUES (71, 'Can change file object', 24, 'change_fileobject');
INSERT INTO `auth_permission` VALUES (72, 'Can delete file object', 24, 'delete_fileobject');
INSERT INTO `auth_permission` VALUES (73, 'Can add base unit', 25, 'add_baseunit');
INSERT INTO `auth_permission` VALUES (74, 'Can change base unit', 25, 'change_baseunit');
INSERT INTO `auth_permission` VALUES (75, 'Can delete base unit', 25, 'delete_baseunit');
INSERT INTO `auth_permission` VALUES (76, 'Can add base user', 26, 'add_baseuser');
INSERT INTO `auth_permission` VALUES (77, 'Can change base user', 26, 'change_baseuser');
INSERT INTO `auth_permission` VALUES (78, 'Can delete base user', 26, 'delete_baseuser');
INSERT INTO `auth_permission` VALUES (79, 'Can add product tag', 27, 'add_producttag');
INSERT INTO `auth_permission` VALUES (80, 'Can change product tag', 27, 'change_producttag');
INSERT INTO `auth_permission` VALUES (81, 'Can delete product tag', 27, 'delete_producttag');
INSERT INTO `auth_permission` VALUES (82, 'Can add product brand', 28, 'add_productbrand');
INSERT INTO `auth_permission` VALUES (83, 'Can change product brand', 28, 'change_productbrand');
INSERT INTO `auth_permission` VALUES (84, 'Can delete product brand', 28, 'delete_productbrand');
INSERT INTO `auth_permission` VALUES (85, 'Can add product price list', 29, 'add_productpricelist');
INSERT INTO `auth_permission` VALUES (86, 'Can change product price list', 29, 'change_productpricelist');
INSERT INTO `auth_permission` VALUES (87, 'Can delete product price list', 29, 'delete_productpricelist');
INSERT INTO `auth_permission` VALUES (88, 'Can add product category', 30, 'add_productcategory');
INSERT INTO `auth_permission` VALUES (89, 'Can change product category', 30, 'change_productcategory');
INSERT INTO `auth_permission` VALUES (90, 'Can delete product category', 30, 'delete_productcategory');
INSERT INTO `auth_permission` VALUES (91, 'Can add product', 31, 'add_product');
INSERT INTO `auth_permission` VALUES (92, 'Can change product', 31, 'change_product');
INSERT INTO `auth_permission` VALUES (93, 'Can delete product', 31, 'delete_product');
INSERT INTO `auth_permission` VALUES (94, 'Can add stock warehouse', 32, 'add_stockwarehouse');
INSERT INTO `auth_permission` VALUES (95, 'Can change stock warehouse', 32, 'change_stockwarehouse');
INSERT INTO `auth_permission` VALUES (96, 'Can delete stock warehouse', 32, 'delete_stockwarehouse');
INSERT INTO `auth_permission` VALUES (97, 'Can add stock location', 33, 'add_stocklocation');
INSERT INTO `auth_permission` VALUES (98, 'Can change stock location', 33, 'change_stocklocation');
INSERT INTO `auth_permission` VALUES (99, 'Can delete stock location', 33, 'delete_stocklocation');
INSERT INTO `auth_permission` VALUES (100, 'Can add account account', 34, 'add_accountaccount');
INSERT INTO `auth_permission` VALUES (101, 'Can change account account', 34, 'change_accountaccount');
INSERT INTO `auth_permission` VALUES (102, 'Can delete account account', 34, 'delete_accountaccount');
INSERT INTO `auth_permission` VALUES (103, 'Can add material', 35, 'add_material');
INSERT INTO `auth_permission` VALUES (104, 'Can change material', 35, 'change_material');
INSERT INTO `auth_permission` VALUES (105, 'Can delete material', 35, 'delete_material');
INSERT INTO `auth_permission` VALUES (106, 'Can add base school', 36, 'add_baseschool');
INSERT INTO `auth_permission` VALUES (107, 'Can change base school', 36, 'change_baseschool');
INSERT INTO `auth_permission` VALUES (108, 'Can delete base school', 36, 'delete_baseschool');
INSERT INTO `auth_permission` VALUES (109, 'Can add teacher', 37, 'add_teacher');
INSERT INTO `auth_permission` VALUES (110, 'Can change teacher', 37, 'change_teacher');
INSERT INTO `auth_permission` VALUES (111, 'Can delete teacher', 37, 'delete_teacher');
INSERT INTO `auth_permission` VALUES (112, 'Can add base course', 38, 'add_basecourse');
INSERT INTO `auth_permission` VALUES (113, 'Can change base course', 38, 'change_basecourse');
INSERT INTO `auth_permission` VALUES (114, 'Can delete base course', 38, 'delete_basecourse');
INSERT INTO `auth_permission` VALUES (115, 'Can add base class', 39, 'add_baseclass');
INSERT INTO `auth_permission` VALUES (116, 'Can change base class', 39, 'change_baseclass');
INSERT INTO `auth_permission` VALUES (117, 'Can delete base class', 39, 'delete_baseclass');
INSERT INTO `auth_permission` VALUES (118, 'Can add student', 40, 'add_student');
INSERT INTO `auth_permission` VALUES (119, 'Can change student', 40, 'change_student');
INSERT INTO `auth_permission` VALUES (120, 'Can delete student', 40, 'delete_student');
INSERT INTO `auth_permission` VALUES (121, 'Can add score record', 41, 'add_scorerecord');
INSERT INTO `auth_permission` VALUES (122, 'Can change score record', 41, 'change_scorerecord');
INSERT INTO `auth_permission` VALUES (123, 'Can delete score record', 41, 'delete_scorerecord');
INSERT INTO `auth_permission` VALUES (124, 'Can add class course map', 42, 'add_classcoursemap');
INSERT INTO `auth_permission` VALUES (125, 'Can change class course map', 42, 'change_classcoursemap');
INSERT INTO `auth_permission` VALUES (126, 'Can delete class course map', 42, 'delete_classcoursemap');
INSERT INTO `auth_permission` VALUES (127, 'Can add examination', 43, 'add_examination');
INSERT INTO `auth_permission` VALUES (128, 'Can change examination', 43, 'change_examination');
INSERT INTO `auth_permission` VALUES (129, 'Can delete examination', 43, 'delete_examination');
INSERT INTO `auth_permission` VALUES (130, 'Can add base grade', 44, 'add_basegrade');
INSERT INTO `auth_permission` VALUES (131, 'Can change base grade', 44, 'change_basegrade');
INSERT INTO `auth_permission` VALUES (132, 'Can delete base grade', 44, 'delete_basegrade');

-- ----------------------------
-- Table structure for base_basecity
-- ----------------------------
DROP TABLE IF EXISTS `base_basecity`;
CREATE TABLE `base_basecity`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `area_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_municipality` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `province_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `base_basecity_province_id_c1a9edf9_fk_base_province_id`(`province_id`) USING BTREE,
  CONSTRAINT `base_basecity_province_id_c1a9edf9_fk_base_province_id` FOREIGN KEY (`province_id`) REFERENCES `base_province` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_basejob
-- ----------------------------
DROP TABLE IF EXISTS `base_basejob`;
CREATE TABLE `base_basejob`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_baseunit
-- ----------------------------
DROP TABLE IF EXISTS `base_baseunit`;
CREATE TABLE `base_baseunit`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `unit_symbol` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `unit_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_base_unit` tinyint(1) NOT NULL,
  `rounding` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `factor` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `compute_method` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `base_baseunit_unit_type_is_base_unit_aead7725_uniq`(`unit_type`, `is_base_unit`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_baseuser
-- ----------------------------
DROP TABLE IF EXISTS `base_baseuser`;
CREATE TABLE `base_baseuser`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_department_manager` tinyint(1) NOT NULL,
  `company_id` int(11) NULL DEFAULT NULL,
  `department_id` int(11) NULL DEFAULT NULL,
  `job_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  INDEX `base_baseuser_company_id_2178dc55_fk_base_company_id`(`company_id`) USING BTREE,
  INDEX `base_baseuser_department_id_bb38eebf_fk_base_department_id`(`department_id`) USING BTREE,
  INDEX `base_baseuser_job_id_47930093_fk_base_basejob_id`(`job_id`) USING BTREE,
  CONSTRAINT `base_baseuser_company_id_2178dc55_fk_base_company_id` FOREIGN KEY (`company_id`) REFERENCES `base_company` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `base_baseuser_department_id_bb38eebf_fk_base_department_id` FOREIGN KEY (`department_id`) REFERENCES `base_department` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `base_baseuser_job_id_47930093_fk_base_basejob_id` FOREIGN KEY (`job_id`) REFERENCES `base_basejob` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of base_baseuser
-- ----------------------------
INSERT INTO `base_baseuser` VALUES (1, '!79Qc2iOaGIiKGvucRlUcuA9met1JJmQ8NdMWZGan', NULL, 0, 'AnonymousUser', '', 1, '2019-04-28 17:02:09.369574', 1, 0, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for base_baseuser_groups
-- ----------------------------
DROP TABLE IF EXISTS `base_baseuser_groups`;
CREATE TABLE `base_baseuser_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `baseuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `base_baseuser_groups_baseuser_id_group_id_24e382e1_uniq`(`baseuser_id`, `group_id`) USING BTREE,
  INDEX `base_baseuser_groups_group_id_ba0dd09e_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `base_baseuser_groups_baseuser_id_715e8ff0_fk_base_baseuser_id` FOREIGN KEY (`baseuser_id`) REFERENCES `base_baseuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `base_baseuser_groups_group_id_ba0dd09e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_baseuser_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `base_baseuser_user_permissions`;
CREATE TABLE `base_baseuser_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `baseuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `base_baseuser_user_permi_baseuser_id_permission_i_6973a8cd_uniq`(`baseuser_id`, `permission_id`) USING BTREE,
  INDEX `base_baseuser_user_p_permission_id_0a42e233_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `base_baseuser_user_p_baseuser_id_2a3635c1_fk_base_base` FOREIGN KEY (`baseuser_id`) REFERENCES `base_baseuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `base_baseuser_user_p_permission_id_0a42e233_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_company
-- ----------------------------
DROP TABLE IF EXISTS `base_company`;
CREATE TABLE `base_company`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `website` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `city_id` int(11) NULL DEFAULT NULL,
  `province_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `base_company_city_id_41edec2f_fk_base_basecity_id`(`city_id`) USING BTREE,
  INDEX `base_company_province_id_a19eedbf_fk_base_province_id`(`province_id`) USING BTREE,
  CONSTRAINT `base_company_city_id_41edec2f_fk_base_basecity_id` FOREIGN KEY (`city_id`) REFERENCES `base_basecity` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `base_company_province_id_a19eedbf_fk_base_province_id` FOREIGN KEY (`province_id`) REFERENCES `base_province` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_department
-- ----------------------------
DROP TABLE IF EXISTS `base_department`;
CREATE TABLE `base_department`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `company_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `base_department_company_id_f62c3b2f_fk_base_company_id`(`company_id`) USING BTREE,
  CONSTRAINT `base_department_company_id_f62c3b2f_fk_base_company_id` FOREIGN KEY (`company_id`) REFERENCES `base_company` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_fileobject
-- ----------------------------
DROP TABLE IF EXISTS `base_fileobject`;
CREATE TABLE `base_fileobject`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model_field` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `file_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `file_suffix` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `file_path` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `file_coding` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `file_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `file_path`(`file_path`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_partner
-- ----------------------------
DROP TABLE IF EXISTS `base_partner`;
CREATE TABLE `base_partner`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_province
-- ----------------------------
DROP TABLE IF EXISTS `base_province`;
CREATE TABLE `base_province`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `short_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_sequence
-- ----------------------------
DROP TABLE IF EXISTS `base_sequence`;
CREATE TABLE `base_sequence`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `padding` int(11) NOT NULL,
  `step_len` int(11) NOT NULL,
  `next_number` int(11) NOT NULL,
  `suffix` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `prefix` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `code`(`code`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for base_useroperationlog
-- ----------------------------
DROP TABLE IF EXISTS `base_useroperationlog`;
CREATE TABLE `base_useroperationlog`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `result` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `base_useroperationlog_user_id_c7480510_fk_base_baseuser_id`(`user_id`) USING BTREE,
  CONSTRAINT `base_useroperationlog_user_id_c7480510_fk_base_baseuser_id` FOREIGN KEY (`user_id`) REFERENCES `base_baseuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for celery_taskmeta
-- ----------------------------
DROP TABLE IF EXISTS `celery_taskmeta`;
CREATE TABLE `celery_taskmeta`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `result` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `date_done` datetime(6) NULL,
  `traceback` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `task_id`(`task_id`) USING BTREE,
  INDEX `celery_taskmeta_hidden_23fd02dc`(`hidden`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for celery_tasksetmeta
-- ----------------------------
DROP TABLE IF EXISTS `celery_tasksetmeta`;
CREATE TABLE `celery_tasksetmeta`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `taskset_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `result` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date_done` datetime(6) NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `taskset_id`(`taskset_id`) USING BTREE,
  INDEX `celery_tasksetmeta_hidden_593cfc24`(`hidden`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_base_baseuser_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_base_baseuser_id` FOREIGN KEY (`user_id`) REFERENCES `base_baseuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (34, 'account', 'accountaccount');
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (23, 'base', 'basecity');
INSERT INTO `django_content_type` VALUES (22, 'base', 'basejob');
INSERT INTO `django_content_type` VALUES (25, 'base', 'baseunit');
INSERT INTO `django_content_type` VALUES (26, 'base', 'baseuser');
INSERT INTO `django_content_type` VALUES (19, 'base', 'company');
INSERT INTO `django_content_type` VALUES (20, 'base', 'department');
INSERT INTO `django_content_type` VALUES (24, 'base', 'fileobject');
INSERT INTO `django_content_type` VALUES (17, 'base', 'partner');
INSERT INTO `django_content_type` VALUES (21, 'base', 'province');
INSERT INTO `django_content_type` VALUES (18, 'base', 'sequence');
INSERT INTO `django_content_type` VALUES (16, 'base', 'useroperationlog');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (12, 'djcelery', 'crontabschedule');
INSERT INTO `django_content_type` VALUES (7, 'djcelery', 'intervalschedule');
INSERT INTO `django_content_type` VALUES (11, 'djcelery', 'periodictask');
INSERT INTO `django_content_type` VALUES (6, 'djcelery', 'periodictasks');
INSERT INTO `django_content_type` VALUES (9, 'djcelery', 'taskmeta');
INSERT INTO `django_content_type` VALUES (13, 'djcelery', 'tasksetmeta');
INSERT INTO `django_content_type` VALUES (8, 'djcelery', 'taskstate');
INSERT INTO `django_content_type` VALUES (10, 'djcelery', 'workerstate');
INSERT INTO `django_content_type` VALUES (14, 'guardian', 'groupobjectpermission');
INSERT INTO `django_content_type` VALUES (15, 'guardian', 'userobjectpermission');
INSERT INTO `django_content_type` VALUES (31, 'product', 'product');
INSERT INTO `django_content_type` VALUES (28, 'product', 'productbrand');
INSERT INTO `django_content_type` VALUES (30, 'product', 'productcategory');
INSERT INTO `django_content_type` VALUES (29, 'product', 'productpricelist');
INSERT INTO `django_content_type` VALUES (27, 'product', 'producttag');
INSERT INTO `django_content_type` VALUES (39, 'school', 'baseclass');
INSERT INTO `django_content_type` VALUES (38, 'school', 'basecourse');
INSERT INTO `django_content_type` VALUES (44, 'school', 'basegrade');
INSERT INTO `django_content_type` VALUES (36, 'school', 'baseschool');
INSERT INTO `django_content_type` VALUES (42, 'school', 'classcoursemap');
INSERT INTO `django_content_type` VALUES (43, 'school', 'examination');
INSERT INTO `django_content_type` VALUES (35, 'school', 'material');
INSERT INTO `django_content_type` VALUES (41, 'school', 'scorerecord');
INSERT INTO `django_content_type` VALUES (40, 'school', 'student');
INSERT INTO `django_content_type` VALUES (37, 'school', 'teacher');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (33, 'stock', 'stocklocation');
INSERT INTO `django_content_type` VALUES (32, 'stock', 'stockwarehouse');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 31 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2019-04-28 17:02:03.871312');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2019-04-28 17:02:03.940088');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2019-04-28 17:02:04.149483');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2019-04-28 17:02:04.188205');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2019-04-28 17:02:04.198204');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2019-04-28 17:02:04.207225');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2019-04-28 17:02:04.217221');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2019-04-28 17:02:04.219931');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2019-04-28 17:02:04.228950');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2019-04-28 17:02:04.239934');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2019-04-28 17:02:04.247933');
INSERT INTO `django_migrations` VALUES (12, 'base', '0001_initial', '2019-04-28 17:02:05.317567');
INSERT INTO `django_migrations` VALUES (13, 'account', '0001_initial', '2019-04-28 17:02:05.348570');
INSERT INTO `django_migrations` VALUES (14, 'account', '0002_auto_20190428_1701', '2019-04-28 17:02:05.731526');
INSERT INTO `django_migrations` VALUES (15, 'admin', '0001_initial', '2019-04-28 17:02:05.853170');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0002_logentry_remove_auto_add', '2019-04-28 17:02:05.875175');
INSERT INTO `django_migrations` VALUES (17, 'djcelery', '0001_initial', '2019-04-28 17:02:06.289436');
INSERT INTO `django_migrations` VALUES (18, 'guardian', '0001_initial', '2019-04-28 17:02:06.677440');
INSERT INTO `django_migrations` VALUES (19, 'product', '0001_initial', '2019-04-28 17:02:07.675735');
INSERT INTO `django_migrations` VALUES (20, 'school', '0001_initial', '2019-04-28 17:02:08.911776');
INSERT INTO `django_migrations` VALUES (21, 'sessions', '0001_initial', '2019-04-28 17:02:08.950785');
INSERT INTO `django_migrations` VALUES (22, 'stock', '0001_initial', '2019-04-28 17:02:09.202519');
INSERT INTO `django_migrations` VALUES (23, 'school', '0002_auto_20190428_1736', '2019-04-28 17:36:29.787202');
INSERT INTO `django_migrations` VALUES (24, 'school', '0003_auto_20190428_1758', '2019-04-28 17:58:12.819355');
INSERT INTO `django_migrations` VALUES (25, 'school', '0004_material_teachers', '2019-04-28 18:09:18.608855');
INSERT INTO `django_migrations` VALUES (26, 'school', '0005_auto_20190428_1823', '2019-04-28 18:24:00.982049');
INSERT INTO `django_migrations` VALUES (27, 'school', '0006_examination_is_create_record', '2019-04-28 18:32:10.984331');
INSERT INTO `django_migrations` VALUES (28, 'school', '0007_material_full_score_tag', '2019-04-28 18:43:23.856327');
INSERT INTO `django_migrations` VALUES (29, 'school', '0008_auto_20190428_1955', '2019-04-28 19:55:30.290084');
INSERT INTO `django_migrations` VALUES (30, 'school', '0009_auto_20190429_0308', '2019-04-29 03:08:48.293249');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_crontabschedule
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_crontabschedule`;
CREATE TABLE `djcelery_crontabschedule`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hour` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `day_of_week` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `day_of_month` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `month_of_year` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_intervalschedule
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_intervalschedule`;
CREATE TABLE `djcelery_intervalschedule`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `every` int(11) NOT NULL,
  `period` varchar(24) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_periodictask
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictask`;
CREATE TABLE `djcelery_periodictask`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `task` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `args` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `kwargs` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `queue` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `exchange` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `routing_key` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `expires` datetime(6) NULL DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) NULL DEFAULT NULL,
  `total_run_count` int(10) UNSIGNED NOT NULL,
  `date_changed` datetime(6) NULL,
  `description` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `crontab_id` int(11) NULL DEFAULT NULL,
  `interval_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `djcelery_periodictas_crontab_id_75609bab_fk_djcelery_`(`crontab_id`) USING BTREE,
  INDEX `djcelery_periodictas_interval_id_b426ab02_fk_djcelery_`(`interval_id`) USING BTREE,
  CONSTRAINT `djcelery_periodictas_crontab_id_75609bab_fk_djcelery_` FOREIGN KEY (`crontab_id`) REFERENCES `djcelery_crontabschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `djcelery_periodictas_interval_id_b426ab02_fk_djcelery_` FOREIGN KEY (`interval_id`) REFERENCES `djcelery_intervalschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_periodictasks
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictasks`;
CREATE TABLE `djcelery_periodictasks`  (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime(6) NULL,
  PRIMARY KEY (`ident`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_taskstate
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_taskstate`;
CREATE TABLE `djcelery_taskstate`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `task_id` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tstamp` datetime(6) NULL,
  `args` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `kwargs` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `eta` datetime(6) NULL DEFAULT NULL,
  `expires` datetime(6) NULL DEFAULT NULL,
  `result` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `traceback` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `runtime` double NULL DEFAULT NULL,
  `retries` int(11) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `worker_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `task_id`(`task_id`) USING BTREE,
  INDEX `djcelery_taskstate_state_53543be4`(`state`) USING BTREE,
  INDEX `djcelery_taskstate_name_8af9eded`(`name`) USING BTREE,
  INDEX `djcelery_taskstate_tstamp_4c3f93a1`(`tstamp`) USING BTREE,
  INDEX `djcelery_taskstate_hidden_c3905e57`(`hidden`) USING BTREE,
  INDEX `djcelery_taskstate_worker_id_f7f57a05_fk_djcelery_workerstate_id`(`worker_id`) USING BTREE,
  CONSTRAINT `djcelery_taskstate_worker_id_f7f57a05_fk_djcelery_workerstate_id` FOREIGN KEY (`worker_id`) REFERENCES `djcelery_workerstate` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_workerstate
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_workerstate`;
CREATE TABLE `djcelery_workerstate`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_heartbeat` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `hostname`(`hostname`) USING BTREE,
  INDEX `djcelery_workerstate_last_heartbeat_4539b544`(`last_heartbeat`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for guardian_groupobjectpermission
-- ----------------------------
DROP TABLE IF EXISTS `guardian_groupobjectpermission`;
CREATE TABLE `guardian_groupobjectpermission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_pk` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `guardian_groupobjectperm_group_id_permission_id_o_3f189f7c_uniq`(`group_id`, `permission_id`, `object_pk`) USING BTREE,
  INDEX `guardian_groupobject_content_type_id_7ade36b8_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `guardian_groupobject_permission_id_36572738_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `guardian_groupobject_content_type_id_7ade36b8_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `guardian_groupobject_group_id_4bbbfb62_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `guardian_groupobject_permission_id_36572738_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for guardian_userobjectpermission
-- ----------------------------
DROP TABLE IF EXISTS `guardian_userobjectpermission`;
CREATE TABLE `guardian_userobjectpermission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_pk` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `guardian_userobjectpermi_user_id_permission_id_ob_b0b3d2fc_uniq`(`user_id`, `permission_id`, `object_pk`) USING BTREE,
  INDEX `guardian_userobjectp_content_type_id_2e892405_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `guardian_userobjectp_permission_id_71807bfc_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `guardian_userobjectp_content_type_id_2e892405_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `guardian_userobjectp_permission_id_71807bfc_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `guardian_userobjectp_user_id_d5c1e964_fk_base_base` FOREIGN KEY (`user_id`) REFERENCES `base_baseuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for product_product
-- ----------------------------
DROP TABLE IF EXISTS `product_product`;
CREATE TABLE `product_product`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_usage_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `can_sale` tinyint(1) NOT NULL,
  `can_purchase` tinyint(1) NOT NULL,
  `product_sale_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `barcode` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_rank` int(11) NOT NULL,
  `product_image` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_length` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_width` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_height` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `brand_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `default_unit_uom_id` int(11) NOT NULL,
  `product_volume_uom_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `product_product_brand_id_fcf1b3f3_fk_product_productbrand_id`(`brand_id`) USING BTREE,
  INDEX `product_product_category_id_0c725779_fk_product_p`(`category_id`) USING BTREE,
  INDEX `product_product_company_id_0965fde9_fk_base_company_id`(`company_id`) USING BTREE,
  INDEX `product_product_default_unit_uom_id_16cc1cbe_fk_base_baseunit_id`(`default_unit_uom_id`) USING BTREE,
  INDEX `product_product_product_volume_uom_i_fb9ab594_fk_base_base`(`product_volume_uom_id`) USING BTREE,
  CONSTRAINT `product_product_brand_id_fcf1b3f3_fk_product_productbrand_id` FOREIGN KEY (`brand_id`) REFERENCES `product_productbrand` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_product_category_id_0c725779_fk_product_p` FOREIGN KEY (`category_id`) REFERENCES `product_productcategory` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_product_company_id_0965fde9_fk_base_company_id` FOREIGN KEY (`company_id`) REFERENCES `base_company` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_product_default_unit_uom_id_16cc1cbe_fk_base_baseunit_id` FOREIGN KEY (`default_unit_uom_id`) REFERENCES `base_baseunit` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_product_product_volume_uom_i_fb9ab594_fk_base_base` FOREIGN KEY (`product_volume_uom_id`) REFERENCES `base_baseunit` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for product_product_tags
-- ----------------------------
DROP TABLE IF EXISTS `product_product_tags`;
CREATE TABLE `product_product_tags`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `producttag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `product_product_tags_product_id_producttag_id_6d60d4e7_uniq`(`product_id`, `producttag_id`) USING BTREE,
  INDEX `product_product_tags_producttag_id_bbe254f9_fk_product_p`(`producttag_id`) USING BTREE,
  CONSTRAINT `product_product_tags_product_id_a72c644e_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product_product` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_product_tags_producttag_id_bbe254f9_fk_product_p` FOREIGN KEY (`producttag_id`) REFERENCES `product_producttag` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for product_productbrand
-- ----------------------------
DROP TABLE IF EXISTS `product_productbrand`;
CREATE TABLE `product_productbrand`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rank` int(11) NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for product_productcategory
-- ----------------------------
DROP TABLE IF EXISTS `product_productcategory`;
CREATE TABLE `product_productcategory`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rank` int(11) NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for product_productpricelist
-- ----------------------------
DROP TABLE IF EXISTS `product_productpricelist`;
CREATE TABLE `product_productpricelist`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `original_price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `purchase_price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sale_price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NULL DEFAULT NULL,
  `create_time` datetime(6) NULL,
  `done_time` datetime(6) NULL DEFAULT NULL,
  `state` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `company_id` int(11) NOT NULL,
  `create_user_id` int(11) NOT NULL,
  `price_uom_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `product_productpricelist_company_id_6066c64d_fk_base_company_id`(`company_id`) USING BTREE,
  INDEX `product_productprice_create_user_id_1dff78f0_fk_base_base`(`create_user_id`) USING BTREE,
  INDEX `product_productprice_price_uom_id_1894d6b6_fk_base_base`(`price_uom_id`) USING BTREE,
  INDEX `product_productprice_product_id_4ddd3bc0_fk_product_p`(`product_id`) USING BTREE,
  CONSTRAINT `product_productprice_create_user_id_1dff78f0_fk_base_base` FOREIGN KEY (`create_user_id`) REFERENCES `base_baseuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_productprice_price_uom_id_1894d6b6_fk_base_base` FOREIGN KEY (`price_uom_id`) REFERENCES `base_baseunit` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_productprice_product_id_4ddd3bc0_fk_product_p` FOREIGN KEY (`product_id`) REFERENCES `product_product` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_productpricelist_company_id_6066c64d_fk_base_company_id` FOREIGN KEY (`company_id`) REFERENCES `base_company` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for product_producttag
-- ----------------------------
DROP TABLE IF EXISTS `product_producttag`;
CREATE TABLE `product_producttag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rank` int(11) NOT NULL,
  `color` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `create_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `product_producttag_create_user_id_ead18549_fk_base_baseuser_id`(`create_user_id`) USING BTREE,
  CONSTRAINT `product_producttag_create_user_id_ead18549_fk_base_baseuser_id` FOREIGN KEY (`create_user_id`) REFERENCES `base_baseuser` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for school_baseclass
-- ----------------------------
DROP TABLE IF EXISTS `school_baseclass`;
CREATE TABLE `school_baseclass`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_year` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `head_teacher_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `school_baseclass_head_teacher_id_f2f35ea6_fk_school_teacher_id`(`head_teacher_id`) USING BTREE,
  INDEX `school_baseclass_school_id_3299d401_fk_school_baseschool_id`(`school_id`) USING BTREE,
  CONSTRAINT `school_baseclass_head_teacher_id_f2f35ea6_fk_school_teacher_id` FOREIGN KEY (`head_teacher_id`) REFERENCES `school_teacher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_baseclass_school_id_3299d401_fk_school_baseschool_id` FOREIGN KEY (`school_id`) REFERENCES `school_baseschool` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_baseclass
-- ----------------------------
INSERT INTO `school_baseclass` VALUES (1, '普通班级1115', '1115', '2011', 1, 2, 1);
INSERT INTO `school_baseclass` VALUES (2, '平行班1108', '1108', '2011', 1, 4, 1);

-- ----------------------------
-- Table structure for school_basecourse
-- ----------------------------
DROP TABLE IF EXISTS `school_basecourse`;
CREATE TABLE `school_basecourse`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_basecourse
-- ----------------------------
INSERT INTO `school_basecourse` VALUES (1, '语文', 'Chinese', 1);
INSERT INTO `school_basecourse` VALUES (2, '数学', 'Mathematical', 1);
INSERT INTO `school_basecourse` VALUES (3, '英语', 'English', 1);
INSERT INTO `school_basecourse` VALUES (4, '生物', 'Biological', 1);
INSERT INTO `school_basecourse` VALUES (5, '物理', 'Physical', 1);
INSERT INTO `school_basecourse` VALUES (6, '化学', 'Chemistry', 1);
INSERT INTO `school_basecourse` VALUES (8, '地理', 'Georaphy', 1);
INSERT INTO `school_basecourse` VALUES (9, '历史', 'History', 1);

-- ----------------------------
-- Table structure for school_basegrade
-- ----------------------------
DROP TABLE IF EXISTS `school_basegrade`;
CREATE TABLE `school_basegrade`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `semester` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `school_basegrade_name_semester_dbd30e70_uniq`(`name`, `semester`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_basegrade
-- ----------------------------
INSERT INTO `school_basegrade` VALUES (1, '高中一年级', '1', 1);
INSERT INTO `school_basegrade` VALUES (2, '高中一年级', '2', 1);
INSERT INTO `school_basegrade` VALUES (3, '高中二年级', '1', 1);
INSERT INTO `school_basegrade` VALUES (4, '高中二年级', '2', 1);
INSERT INTO `school_basegrade` VALUES (5, '高中三年级', '1', 1);
INSERT INTO `school_basegrade` VALUES (6, '高中三年级', '2', 1);
INSERT INTO `school_basegrade` VALUES (7, '一年级', '1', 1);
INSERT INTO `school_basegrade` VALUES (8, '一年级', '2', 1);
INSERT INTO `school_basegrade` VALUES (9, '二年级', '1', 1);
INSERT INTO `school_basegrade` VALUES (10, '二年级', '2', 1);
INSERT INTO `school_basegrade` VALUES (11, '三年级', '1', 1);
INSERT INTO `school_basegrade` VALUES (12, '三年级', '2', 1);

-- ----------------------------
-- Table structure for school_baseschool
-- ----------------------------
DROP TABLE IF EXISTS `school_baseschool`;
CREATE TABLE `school_baseschool`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `short_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_baseschool
-- ----------------------------
INSERT INTO `school_baseschool` VALUES (1, '常德市鼎城区第一中学', 'SCH00001', '一中', 1);

-- ----------------------------
-- Table structure for school_classcoursemap
-- ----------------------------
DROP TABLE IF EXISTS `school_classcoursemap`;
CREATE TABLE `school_classcoursemap`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_use_now` tinyint(1) NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `base_class_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `grade_info_id` int(11) NOT NULL,
  `material_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `school_classcoursemap_grade_info_id_base_class_2abc79cd_uniq`(`grade_info_id`, `base_class_id`, `course_id`) USING BTREE,
  INDEX `school_classcoursema_base_class_id_b0d94706_fk_school_ba`(`base_class_id`) USING BTREE,
  INDEX `school_classcoursemap_course_id_051b7bc1_fk_school_basecourse_id`(`course_id`) USING BTREE,
  INDEX `school_classcoursemap_material_id_fbe9eac9_fk_school_material_id`(`material_id`) USING BTREE,
  INDEX `school_classcoursemap_teacher_id_e97454a6_fk_school_teacher_id`(`teacher_id`) USING BTREE,
  CONSTRAINT `school_classcoursema_base_class_id_b0d94706_fk_school_ba` FOREIGN KEY (`base_class_id`) REFERENCES `school_baseclass` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_classcoursema_grade_info_id_da296574_fk_school_ba` FOREIGN KEY (`grade_info_id`) REFERENCES `school_basegrade` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_classcoursemap_course_id_051b7bc1_fk_school_basecourse_id` FOREIGN KEY (`course_id`) REFERENCES `school_basecourse` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_classcoursemap_material_id_fbe9eac9_fk_school_material_id` FOREIGN KEY (`material_id`) REFERENCES `school_material` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_classcoursemap_teacher_id_e97454a6_fk_school_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `school_teacher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_classcoursemap
-- ----------------------------
INSERT INTO `school_classcoursemap` VALUES (1, 1, '2019-04-28 18:02:26.939288', 1, 1, 1, 1, 3, 4);
INSERT INTO `school_classcoursemap` VALUES (2, 1, '2019-04-28 18:07:15.582645', 1, 1, 3, 1, 4, 1);

-- ----------------------------
-- Table structure for school_examination
-- ----------------------------
DROP TABLE IF EXISTS `school_examination`;
CREATE TABLE `school_examination`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `test_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `test_date` date NULL DEFAULT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `course_map_id` int(11) NOT NULL,
  `invigilator_id` int(11) NOT NULL,
  `read_teacher_id` int(11) NULL DEFAULT NULL,
  `is_create_record` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `school_examination_course_map_id_14f9f38f_fk_school_cl`(`course_map_id`) USING BTREE,
  INDEX `school_examination_invigilator_id_c91fffb1_fk_school_teacher_id`(`invigilator_id`) USING BTREE,
  INDEX `school_examination_read_teacher_id_c7603e62_fk_school_teacher_id`(`read_teacher_id`) USING BTREE,
  CONSTRAINT `school_examination_course_map_id_14f9f38f_fk_school_cl` FOREIGN KEY (`course_map_id`) REFERENCES `school_classcoursemap` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_examination_invigilator_id_c91fffb1_fk_school_teacher_id` FOREIGN KEY (`invigilator_id`) REFERENCES `school_teacher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_examination_read_teacher_id_c7603e62_fk_school_teacher_id` FOREIGN KEY (`read_teacher_id`) REFERENCES `school_teacher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_examination
-- ----------------------------
INSERT INTO `school_examination` VALUES (3, '英语小测试', 's', '2019-04-19', '2019-04-28 21:44:37.039624', 1, 2, 12, 30, 1);
INSERT INTO `school_examination` VALUES (4, '语文小测试', 's', '2019-04-21', '2019-04-29 02:00:01.387183', 1, 1, 1, 17, 1);

-- ----------------------------
-- Table structure for school_material
-- ----------------------------
DROP TABLE IF EXISTS `school_material`;
CREATE TABLE `school_material`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `credits` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `course_info_id` int(11) NOT NULL,
  `grade_id` int(11) NOT NULL,
  `full_score_tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `school_material_course_info_id_6fbe698e_fk_school_basecourse_id`(`course_info_id`) USING BTREE,
  INDEX `school_material_grade_id_f2a117fc_fk_school_basegrade_id`(`grade_id`) USING BTREE,
  CONSTRAINT `school_material_course_info_id_6fbe698e_fk_school_basecourse_id` FOREIGN KEY (`course_info_id`) REFERENCES `school_basecourse` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_material_grade_id_f2a117fc_fk_school_basegrade_id` FOREIGN KEY (`grade_id`) REFERENCES `school_basegrade` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_material
-- ----------------------------
INSERT INTO `school_material` VALUES (1, '小学一年级语文第一学期教材', 'M000001', '5', 1, 1, 7, '100');
INSERT INTO `school_material` VALUES (2, '小学一年级语文第二学期教材', 'M00000002', '5', 1, 1, 8, '100');
INSERT INTO `school_material` VALUES (3, '高一年级语文第一学期教材', 'G000001', '5', 1, 1, 1, '100');
INSERT INTO `school_material` VALUES (4, '高一英语第一期教材', 'G00002', '4', 1, 3, 1, '100');
INSERT INTO `school_material` VALUES (5, '高中数学1', 'M00001', '5', 1, 2, 7, '100');
INSERT INTO `school_material` VALUES (6, '高中数学2', 'M00002', '5', 1, 2, 8, '100');
INSERT INTO `school_material` VALUES (7, '高中数学1(文)', 'M0000332', '5', 1, 2, 1, '100');

-- ----------------------------
-- Table structure for school_material_teachers
-- ----------------------------
DROP TABLE IF EXISTS `school_material_teachers`;
CREATE TABLE `school_material_teachers`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `material_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `school_material_teachers_material_id_teacher_id_4c065aea_uniq`(`material_id`, `teacher_id`) USING BTREE,
  INDEX `school_material_teac_teacher_id_58b31930_fk_school_te`(`teacher_id`) USING BTREE,
  CONSTRAINT `school_material_teac_material_id_94dd773c_fk_school_ma` FOREIGN KEY (`material_id`) REFERENCES `school_material` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_material_teac_teacher_id_58b31930_fk_school_te` FOREIGN KEY (`teacher_id`) REFERENCES `school_teacher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_material_teachers
-- ----------------------------
INSERT INTO `school_material_teachers` VALUES (2, 7, 20);
INSERT INTO `school_material_teachers` VALUES (3, 7, 31);
INSERT INTO `school_material_teachers` VALUES (1, 7, 32);

-- ----------------------------
-- Table structure for school_scorerecord
-- ----------------------------
DROP TABLE IF EXISTS `school_scorerecord`;
CREATE TABLE `school_scorerecord`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_score_tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `score` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `score_level` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `grade_point` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `credits` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_joined` tinyint(1) NOT NULL,
  `is_passed` tinyint(1) NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `create_teacher_id` int(11) NOT NULL,
  `examination_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `real_score` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `school_scorerecord_create_teacher_id_1e897222_fk_school_te`(`create_teacher_id`) USING BTREE,
  INDEX `school_scorerecord_examination_id_e2b86311_fk_school_ex`(`examination_id`) USING BTREE,
  INDEX `school_scorerecord_student_id_ec608c2c_fk_school_student_id`(`student_id`) USING BTREE,
  CONSTRAINT `school_scorerecord_create_teacher_id_1e897222_fk_school_te` FOREIGN KEY (`create_teacher_id`) REFERENCES `school_teacher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_scorerecord_examination_id_e2b86311_fk_school_ex` FOREIGN KEY (`examination_id`) REFERENCES `school_examination` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `school_scorerecord_student_id_ec608c2c_fk_school_student_id` FOREIGN KEY (`student_id`) REFERENCES `school_student` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 139 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_scorerecord
-- ----------------------------
INSERT INTO `school_scorerecord` VALUES (37, '100', '23', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 10, '23');
INSERT INTO `school_scorerecord` VALUES (38, '100', '72', 'C', '2.2', '8.8', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 82, '72');
INSERT INTO `school_scorerecord` VALUES (39, '100', '27', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 58, '27');
INSERT INTO `school_scorerecord` VALUES (40, '100', '28', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 63, '28');
INSERT INTO `school_scorerecord` VALUES (41, '100', '52', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 57, '52');
INSERT INTO `school_scorerecord` VALUES (42, '100', '0', 'D', '0.0', '0.0', 0, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 18, '0');
INSERT INTO `school_scorerecord` VALUES (43, '100', '33', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 90, '33');
INSERT INTO `school_scorerecord` VALUES (44, '100', '96', 'A', '4.6', '18.4', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 50, '96');
INSERT INTO `school_scorerecord` VALUES (45, '100', '62', 'C', '1.2', '4.8', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 55, '62');
INSERT INTO `school_scorerecord` VALUES (46, '100', '36', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 86, '36');
INSERT INTO `school_scorerecord` VALUES (47, '100', '60', 'C', '1.0', '4.0', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 39, '60');
INSERT INTO `school_scorerecord` VALUES (48, '100', '75', 'B', '2.5', '10.0', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 31, '75');
INSERT INTO `school_scorerecord` VALUES (49, '100', '2', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 47, '2');
INSERT INTO `school_scorerecord` VALUES (50, '100', '91', 'A', '4.1', '16.4', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 12, '91');
INSERT INTO `school_scorerecord` VALUES (51, '100', '96', 'A', '4.6', '18.4', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 20, '96');
INSERT INTO `school_scorerecord` VALUES (52, '100', '34', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 56, '34');
INSERT INTO `school_scorerecord` VALUES (53, '100', '64', 'C', '1.4', '5.6', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 11, '64');
INSERT INTO `school_scorerecord` VALUES (54, '100', '29', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 23, '29');
INSERT INTO `school_scorerecord` VALUES (55, '100', '61', 'C', '1.1', '4.4', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 22, '61');
INSERT INTO `school_scorerecord` VALUES (56, '100', '3', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 87, '3');
INSERT INTO `school_scorerecord` VALUES (57, '100', '59', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 77, '59');
INSERT INTO `school_scorerecord` VALUES (58, '100', '4', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 49, '4');
INSERT INTO `school_scorerecord` VALUES (59, '100', '86', 'B', '3.6', '14.4', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 89, '86');
INSERT INTO `school_scorerecord` VALUES (60, '100', '31', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 92, '31');
INSERT INTO `school_scorerecord` VALUES (61, '100', '18', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 91, '18');
INSERT INTO `school_scorerecord` VALUES (62, '100', '84', 'B', '3.4', '13.6', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 35, '84');
INSERT INTO `school_scorerecord` VALUES (63, '100', '37', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 24, '37');
INSERT INTO `school_scorerecord` VALUES (64, '100', '84', 'B', '3.4', '13.6', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 76, '84');
INSERT INTO `school_scorerecord` VALUES (65, '100', '35', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 102, '35');
INSERT INTO `school_scorerecord` VALUES (66, '100', '21', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 72, '21');
INSERT INTO `school_scorerecord` VALUES (67, '100', '18', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 16, '18');
INSERT INTO `school_scorerecord` VALUES (68, '100', '0', 'D', '0.0', '0.0', 0, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 65, '0');
INSERT INTO `school_scorerecord` VALUES (69, '100', '35', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 15, '35');
INSERT INTO `school_scorerecord` VALUES (70, '100', '51', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 101, '51');
INSERT INTO `school_scorerecord` VALUES (71, '100', '7', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 64, '7');
INSERT INTO `school_scorerecord` VALUES (72, '100', '67', 'C', '1.7', '6.8', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 81, '67');
INSERT INTO `school_scorerecord` VALUES (73, '100', '94', 'A', '4.4', '17.6', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 75, '94');
INSERT INTO `school_scorerecord` VALUES (74, '100', '96', 'A', '4.6', '18.4', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 5, '96');
INSERT INTO `school_scorerecord` VALUES (75, '100', '0', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 29, '0');
INSERT INTO `school_scorerecord` VALUES (76, '100', '49', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 85, '49');
INSERT INTO `school_scorerecord` VALUES (77, '100', '51', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 67, '51');
INSERT INTO `school_scorerecord` VALUES (78, '100', '39', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 6, '39');
INSERT INTO `school_scorerecord` VALUES (79, '100', '75', 'B', '2.5', '10.0', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 96, '75');
INSERT INTO `school_scorerecord` VALUES (80, '100', '60', 'C', '1.0', '4.0', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 8, '60');
INSERT INTO `school_scorerecord` VALUES (81, '100', '86', 'B', '3.6', '14.4', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 104, '86');
INSERT INTO `school_scorerecord` VALUES (82, '100', '33', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 59, '33');
INSERT INTO `school_scorerecord` VALUES (83, '100', '59', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 51, '59');
INSERT INTO `school_scorerecord` VALUES (84, '100', '73', 'C', '2.3', '9.2', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 95, '73');
INSERT INTO `school_scorerecord` VALUES (85, '100', '75', 'B', '2.5', '10.0', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 94, '75');
INSERT INTO `school_scorerecord` VALUES (86, '100', '54', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.862946', 1, 30, 3, 68, '54');
INSERT INTO `school_scorerecord` VALUES (87, '100', '96', 'A', '4.6', '18.4', 1, 1, '2019-04-29 02:30:12.862946', 1, 30, 3, 71, '96');
INSERT INTO `school_scorerecord` VALUES (88, '100', '65', 'C', '1.5', '7.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 10, '65');
INSERT INTO `school_scorerecord` VALUES (89, '100', '67', 'C', '1.7', '8.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 82, '67');
INSERT INTO `school_scorerecord` VALUES (90, '100', '73', 'C', '2.3', '11.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 58, '73');
INSERT INTO `school_scorerecord` VALUES (91, '100', '33', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 63, '33');
INSERT INTO `school_scorerecord` VALUES (92, '100', '5', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 57, '5');
INSERT INTO `school_scorerecord` VALUES (93, '100', '80', 'B', '3.0', '15.0', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 18, '80');
INSERT INTO `school_scorerecord` VALUES (94, '100', '70', 'C', '2.0', '10.0', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 90, '70');
INSERT INTO `school_scorerecord` VALUES (95, '100', '46', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 50, '46');
INSERT INTO `school_scorerecord` VALUES (96, '100', '33', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 55, '33');
INSERT INTO `school_scorerecord` VALUES (97, '100', '19', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 86, '19');
INSERT INTO `school_scorerecord` VALUES (98, '100', '81', 'B', '3.1', '15.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 39, '81');
INSERT INTO `school_scorerecord` VALUES (99, '100', '94', 'A', '4.4', '22.0', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 31, '94');
INSERT INTO `school_scorerecord` VALUES (100, '100', '37', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 47, '37');
INSERT INTO `school_scorerecord` VALUES (101, '100', '22', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 12, '22');
INSERT INTO `school_scorerecord` VALUES (102, '100', '83', 'B', '3.3', '16.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 20, '83');
INSERT INTO `school_scorerecord` VALUES (103, '100', '71', 'C', '2.1', '10.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 56, '71');
INSERT INTO `school_scorerecord` VALUES (104, '100', '75', 'B', '2.5', '12.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 11, '75');
INSERT INTO `school_scorerecord` VALUES (105, '100', '19', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 23, '19');
INSERT INTO `school_scorerecord` VALUES (106, '100', '14', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 22, '14');
INSERT INTO `school_scorerecord` VALUES (107, '100', '30', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 87, '30');
INSERT INTO `school_scorerecord` VALUES (108, '100', '15', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 77, '15');
INSERT INTO `school_scorerecord` VALUES (109, '100', '57', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 49, '57');
INSERT INTO `school_scorerecord` VALUES (110, '100', '97', 'A', '4.7', '23.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 89, '97');
INSERT INTO `school_scorerecord` VALUES (111, '100', '20', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 92, '20');
INSERT INTO `school_scorerecord` VALUES (112, '100', '65', 'C', '1.5', '7.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 91, '65');
INSERT INTO `school_scorerecord` VALUES (113, '100', '22', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 35, '22');
INSERT INTO `school_scorerecord` VALUES (114, '100', '19', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 24, '19');
INSERT INTO `school_scorerecord` VALUES (115, '100', '9', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 76, '9');
INSERT INTO `school_scorerecord` VALUES (116, '100', '47', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 102, '47');
INSERT INTO `school_scorerecord` VALUES (117, '100', '45', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 72, '45');
INSERT INTO `school_scorerecord` VALUES (118, '100', '80', 'B', '3.0', '15.0', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 16, '80');
INSERT INTO `school_scorerecord` VALUES (119, '100', '30', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 65, '30');
INSERT INTO `school_scorerecord` VALUES (120, '100', '39', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 15, '39');
INSERT INTO `school_scorerecord` VALUES (121, '100', '65', 'C', '1.5', '7.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 101, '65');
INSERT INTO `school_scorerecord` VALUES (122, '100', '77', 'B', '2.7', '13.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 64, '77');
INSERT INTO `school_scorerecord` VALUES (123, '100', '99', 'A', '4.9', '24.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 81, '99');
INSERT INTO `school_scorerecord` VALUES (124, '100', '19', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 75, '19');
INSERT INTO `school_scorerecord` VALUES (125, '100', '57', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 5, '57');
INSERT INTO `school_scorerecord` VALUES (126, '100', '14', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 29, '14');
INSERT INTO `school_scorerecord` VALUES (127, '100', '70', 'C', '2.0', '10.0', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 85, '70');
INSERT INTO `school_scorerecord` VALUES (128, '100', '100', 'A', '5.0', '25.0', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 67, '100');
INSERT INTO `school_scorerecord` VALUES (129, '100', '37', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 6, '37');
INSERT INTO `school_scorerecord` VALUES (130, '100', '11', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 96, '11');
INSERT INTO `school_scorerecord` VALUES (131, '100', '64', 'C', '1.4', '7.0', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 8, '64');
INSERT INTO `school_scorerecord` VALUES (132, '100', '97', 'A', '4.7', '23.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 104, '97');
INSERT INTO `school_scorerecord` VALUES (133, '100', '65', 'C', '1.5', '7.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 59, '65');
INSERT INTO `school_scorerecord` VALUES (134, '100', '63', 'C', '1.3', '6.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 51, '63');
INSERT INTO `school_scorerecord` VALUES (135, '100', '87', 'A', '3.7', '18.5', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 95, '87');
INSERT INTO `school_scorerecord` VALUES (136, '100', '5', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 94, '5');
INSERT INTO `school_scorerecord` VALUES (137, '100', '58', 'D', '0', '0.0', 1, 0, '2019-04-29 02:30:12.988970', 1, 17, 4, 68, '58');
INSERT INTO `school_scorerecord` VALUES (138, '100', '96', 'A', '4.6', '23.0', 1, 1, '2019-04-29 02:30:12.988970', 1, 17, 4, 71, '96');

-- ----------------------------
-- Table structure for school_student
-- ----------------------------
DROP TABLE IF EXISTS `school_student`;
CREATE TABLE `school_student`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `base_class_id` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `school_student_base_class_id_1c0a1dd6_fk_school_baseclass_id`(`base_class_id`) USING BTREE,
  CONSTRAINT `school_student_base_class_id_1c0a1dd6_fk_school_baseclass_id` FOREIGN KEY (`base_class_id`) REFERENCES `school_baseclass` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 105 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_student
-- ----------------------------
INSERT INTO `school_student` VALUES (5, '辛艳', '120113195703206126', 1, 1);
INSERT INTO `school_student` VALUES (6, '陈帆', '150521196009219279', 1, 1);
INSERT INTO `school_student` VALUES (7, '叶芳', '350721196408140654', 2, 1);
INSERT INTO `school_student` VALUES (8, '陈磊', '450821195509086532', 1, 1);
INSERT INTO `school_student` VALUES (9, '刘桂芳', '11022919550509712X', 2, 1);
INSERT INTO `school_student` VALUES (10, '丁辉', '410802193105121770', 1, 1);
INSERT INTO `school_student` VALUES (11, '朱玉英', '500234198704034786', 1, 1);
INSERT INTO `school_student` VALUES (12, '方桂芳', '120000195302257734', 1, 1);
INSERT INTO `school_student` VALUES (13, '刘欢', '130127194912281005', 2, 1);
INSERT INTO `school_student` VALUES (14, '陈琴', '140110198711167452', 2, 1);
INSERT INTO `school_student` VALUES (15, '苏桂兰', '210882194509294183', 1, 1);
INSERT INTO `school_student` VALUES (16, '章春梅', '211121197806086675', 1, 1);
INSERT INTO `school_student` VALUES (17, '文利', '341182197103275201', 2, 1);
INSERT INTO `school_student` VALUES (18, '吴红', '22052319331202931X', 1, 1);
INSERT INTO `school_student` VALUES (19, '余荣', '230710194907285043', 2, 1);
INSERT INTO `school_student` VALUES (20, '曾涛', '341103193701119985', 1, 1);
INSERT INTO `school_student` VALUES (21, '覃婷婷', '360124198207293707', 2, 1);
INSERT INTO `school_student` VALUES (22, '李浩', '450921199106193126', 1, 1);
INSERT INTO `school_student` VALUES (23, '李凤兰', '340404196810260019', 1, 1);
INSERT INTO `school_student` VALUES (24, '王帅', '130600199003200116', 1, 1);
INSERT INTO `school_student` VALUES (25, '张秀梅', '411729197607018339', 2, 1);
INSERT INTO `school_student` VALUES (26, '汪娟', '130302197209294450', 2, 1);
INSERT INTO `school_student` VALUES (27, '杜敏', '532326197402236217', 2, 1);
INSERT INTO `school_student` VALUES (28, '王凤兰', '632625196405060607', 2, 1);
INSERT INTO `school_student` VALUES (29, '郑丹丹', '632200198208109950', 1, 1);
INSERT INTO `school_student` VALUES (30, '张丽', '441402194105060428', 2, 1);
INSERT INTO `school_student` VALUES (31, '战坤', '520301198912147664', 1, 1);
INSERT INTO `school_student` VALUES (32, '夏帅', '632223195301126617', 2, 1);
INSERT INTO `school_student` VALUES (33, '朱超', '36090219431012778X', 2, 1);
INSERT INTO `school_student` VALUES (34, '罗秀荣', '420804198409133356', 2, 1);
INSERT INTO `school_student` VALUES (35, '汪丽华', '341502193708287362', 1, 1);
INSERT INTO `school_student` VALUES (36, '孙秀华', '150525196606259856', 2, 1);
INSERT INTO `school_student` VALUES (37, '李红霞', '14010519780129680X', 2, 1);
INSERT INTO `school_student` VALUES (38, '赵建国', '220721195310313357', 2, 1);
INSERT INTO `school_student` VALUES (39, '彭秀云', '360426199512294232', 1, 1);
INSERT INTO `school_student` VALUES (40, '易浩', '450126199110016542', 2, 1);
INSERT INTO `school_student` VALUES (41, '汪丹丹', '610113199007151664', 2, 1);
INSERT INTO `school_student` VALUES (42, '朱龙', '411503194910186281', 2, 1);
INSERT INTO `school_student` VALUES (43, '萧兵', '37142519801125746X', 2, 1);
INSERT INTO `school_student` VALUES (44, '高凤英', '330781195006263166', 2, 1);
INSERT INTO `school_student` VALUES (45, '郑莹', '540235194909080263', 2, 1);
INSERT INTO `school_student` VALUES (46, '夏雪梅', '623022199201262128', 2, 1);
INSERT INTO `school_student` VALUES (47, '戚淑兰', '210421197007076409', 1, 1);
INSERT INTO `school_student` VALUES (48, '安莹', '370881195910179598', 2, 1);
INSERT INTO `school_student` VALUES (49, '杨凤英', '220521193104213152', 1, 1);
INSERT INTO `school_student` VALUES (50, '孙畅', '420526193909147518', 1, 1);
INSERT INTO `school_student` VALUES (51, '韩娟', '130109196910066113', 1, 1);
INSERT INTO `school_student` VALUES (52, '蒋杰', '530301196912052166', 2, 1);
INSERT INTO `school_student` VALUES (53, '李娟', '150124196711052453', 2, 1);
INSERT INTO `school_student` VALUES (54, '李凯', '410304194602102159', 2, 1);
INSERT INTO `school_student` VALUES (55, '崔林', '632626193208252207', 1, 1);
INSERT INTO `school_student` VALUES (56, '朱明', '152223199012192435', 1, 1);
INSERT INTO `school_student` VALUES (57, '吴浩', '350400199302187660', 1, 1);
INSERT INTO `school_student` VALUES (58, '史宇', '110109195109033764', 1, 1);
INSERT INTO `school_student` VALUES (59, '鞠桂芳', '540222199512040571', 1, 1);
INSERT INTO `school_student` VALUES (60, '晁莉', '429005199604163476', 2, 1);
INSERT INTO `school_student` VALUES (61, '杨英', '450481198707071794', 2, 1);
INSERT INTO `school_student` VALUES (62, '刘建平', '653024196209095912', 2, 1);
INSERT INTO `school_student` VALUES (63, '吴敏', '420701194908076613', 1, 1);
INSERT INTO `school_student` VALUES (64, '董超', '43310019411007741X', 1, 1);
INSERT INTO `school_student` VALUES (65, '符成', '130401199806262367', 1, 1);
INSERT INTO `school_student` VALUES (66, '卢颖', '320921197910222807', 2, 1);
INSERT INTO `school_student` VALUES (67, '陈丽华', '520424197201133296', 1, 1);
INSERT INTO `school_student` VALUES (68, '马红霞', '220421194209060366', 1, 1);
INSERT INTO `school_student` VALUES (69, '张桂芝', '211223197604185307', 2, 1);
INSERT INTO `school_student` VALUES (70, '卢桂花', '34040419351124922X', 2, 1);
INSERT INTO `school_student` VALUES (71, '龚红', '530100196706283679', 1, 1);
INSERT INTO `school_student` VALUES (72, '秦小红', '220200198105097602', 1, 1);
INSERT INTO `school_student` VALUES (73, '赵慧', '511826194205111705', 2, 1);
INSERT INTO `school_student` VALUES (74, '李志强', '341502194507135519', 2, 1);
INSERT INTO `school_student` VALUES (75, '赵建', '320322194810013792', 1, 1);
INSERT INTO `school_student` VALUES (76, '王建华', '653125195103157414', 1, 1);
INSERT INTO `school_student` VALUES (77, '李雪梅', '620900197706134067', 1, 1);
INSERT INTO `school_student` VALUES (78, '谭东', '140227195406224835', 2, 1);
INSERT INTO `school_student` VALUES (79, '许超', '220182195505080055', 2, 1);
INSERT INTO `school_student` VALUES (80, '杨帆', '540101193310178850', 2, 1);
INSERT INTO `school_student` VALUES (81, '赵健', '370828193210032113', 1, 1);
INSERT INTO `school_student` VALUES (82, '何玉', '430502195305214249', 1, 1);
INSERT INTO `school_student` VALUES (83, '俞旭', '520401196612183723', 2, 1);
INSERT INTO `school_student` VALUES (84, '陈刚', '513331196604129966', 2, 1);
INSERT INTO `school_student` VALUES (85, '郭倩', '11011319571210076X', 1, 1);
INSERT INTO `school_student` VALUES (86, '张莹', '37162619741119507X', 1, 1);
INSERT INTO `school_student` VALUES (87, '李玉梅', '231202199904207986', 1, 1);
INSERT INTO `school_student` VALUES (88, '潘静', '450000198810112195', 2, 1);
INSERT INTO `school_student` VALUES (89, '杨杰', '532503198703068879', 1, 1);
INSERT INTO `school_student` VALUES (90, '孙倩', '150581194010046886', 1, 1);
INSERT INTO `school_student` VALUES (91, '欧晶', '451028199401161246', 1, 1);
INSERT INTO `school_student` VALUES (92, '梁桂荣', '13010419601124843X', 1, 1);
INSERT INTO `school_student` VALUES (93, '石桂英', '140411199910086628', 2, 1);
INSERT INTO `school_student` VALUES (94, '马燕', '511703199204287568', 1, 1);
INSERT INTO `school_student` VALUES (95, '马明', '450803196711215512', 1, 1);
INSERT INTO `school_student` VALUES (96, '陈桂英', '450603198811202928', 1, 1);
INSERT INTO `school_student` VALUES (97, '崔萍', '340621199103042654', 2, 1);
INSERT INTO `school_student` VALUES (98, '罗东', '330400198208314055', 2, 1);
INSERT INTO `school_student` VALUES (99, '王彬', '320104199603212501', 2, 1);
INSERT INTO `school_student` VALUES (100, '刘磊', '211404196601012838', 2, 1);
INSERT INTO `school_student` VALUES (101, '苏秀华', '152922197811150269', 1, 1);
INSERT INTO `school_student` VALUES (102, '王梅', '330185197405074719', 1, 1);
INSERT INTO `school_student` VALUES (103, '李岩', '62100019500925674X', 2, 1);
INSERT INTO `school_student` VALUES (104, '靳秀华', '370923194109059344', 1, 1);

-- ----------------------------
-- Table structure for school_teacher
-- ----------------------------
DROP TABLE IF EXISTS `school_teacher`;
CREATE TABLE `school_teacher`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 35 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of school_teacher
-- ----------------------------
INSERT INTO `school_teacher` VALUES (1, '李四', 'LiSi', 1);
INSERT INTO `school_teacher` VALUES (2, '张三', 'zhangsan', 1);
INSERT INTO `school_teacher` VALUES (3, '老师2号', 'T00002', 1);
INSERT INTO `school_teacher` VALUES (4, '老师1号', 'T00000023', 1);
INSERT INTO `school_teacher` VALUES (5, '莫丹', '341225194002020538', 1);
INSERT INTO `school_teacher` VALUES (6, '张娟', '511024195605218999', 1);
INSERT INTO `school_teacher` VALUES (7, '杜帆', '710000193912059285', 1);
INSERT INTO `school_teacher` VALUES (8, '胡博', '431025195812212334', 1);
INSERT INTO `school_teacher` VALUES (9, '杨雷', '230904195907308215', 1);
INSERT INTO `school_teacher` VALUES (10, '白秀荣', '330800193108247309', 1);
INSERT INTO `school_teacher` VALUES (11, '崔欢', '370612198701169684', 1);
INSERT INTO `school_teacher` VALUES (12, '常利', '640105199411173203', 1);
INSERT INTO `school_teacher` VALUES (13, '李勇', '330502193411248140', 1);
INSERT INTO `school_teacher` VALUES (14, '许荣', '350302195702285859', 1);
INSERT INTO `school_teacher` VALUES (15, '王莉', '371526193103294072', 1);
INSERT INTO `school_teacher` VALUES (16, '周刚', '421101196404058611', 1);
INSERT INTO `school_teacher` VALUES (17, '杨玉梅', '150521197512079167', 1);
INSERT INTO `school_teacher` VALUES (18, '张红霞', '130622196303193549', 1);
INSERT INTO `school_teacher` VALUES (19, '徐玉英', '441324195407076553', 1);
INSERT INTO `school_teacher` VALUES (20, '仝岩', '513400198708229312', 1);
INSERT INTO `school_teacher` VALUES (21, '罗佳', '620825193609091783', 1);
INSERT INTO `school_teacher` VALUES (22, '黄东', '350403195607226326', 1);
INSERT INTO `school_teacher` VALUES (23, '左成', '340501193411012459', 1);
INSERT INTO `school_teacher` VALUES (24, '贺兵', '330521194912171747', 1);
INSERT INTO `school_teacher` VALUES (25, '郭浩', '370830195401127917', 1);
INSERT INTO `school_teacher` VALUES (26, '王春梅', '211303198605016163', 1);
INSERT INTO `school_teacher` VALUES (27, '屈云', '320706195904085769', 1);
INSERT INTO `school_teacher` VALUES (28, '赵杨', '340103197102274577', 1);
INSERT INTO `school_teacher` VALUES (29, '周莹', '410182199205078256', 1);
INSERT INTO `school_teacher` VALUES (30, '李欣', '340828197207268937', 1);
INSERT INTO `school_teacher` VALUES (31, '刘雪', '14042919970506663X', 1);
INSERT INTO `school_teacher` VALUES (32, '任丽华', '610826198011288351', 1);
INSERT INTO `school_teacher` VALUES (33, '陈宇', '511024197503113802', 1);
INSERT INTO `school_teacher` VALUES (34, '夏玲', '451024196308082800', 1);

-- ----------------------------
-- Table structure for stock_stocklocation
-- ----------------------------
DROP TABLE IF EXISTS `stock_stocklocation`;
CREATE TABLE `stock_stocklocation`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `loc_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `short_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `posx` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `posy` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `posz` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `company_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `stock_stocklocation_company_id_0ef058d8_fk_base_company_id`(`company_id`) USING BTREE,
  CONSTRAINT `stock_stocklocation_company_id_0ef058d8_fk_base_company_id` FOREIGN KEY (`company_id`) REFERENCES `base_company` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stock_stockwarehouse
-- ----------------------------
DROP TABLE IF EXISTS `stock_stockwarehouse`;
CREATE TABLE `stock_stockwarehouse`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `short_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NULL,
  `is_active` tinyint(1) NOT NULL,
  `city_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `province_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `stock_stockwarehouse_city_id_0e41086f_fk_base_basecity_id`(`city_id`) USING BTREE,
  INDEX `stock_stockwarehouse_company_id_4dea09cb_fk_base_company_id`(`company_id`) USING BTREE,
  INDEX `stock_stockwarehouse_province_id_e399e93d_fk_base_province_id`(`province_id`) USING BTREE,
  CONSTRAINT `stock_stockwarehouse_city_id_0e41086f_fk_base_basecity_id` FOREIGN KEY (`city_id`) REFERENCES `base_basecity` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `stock_stockwarehouse_company_id_4dea09cb_fk_base_company_id` FOREIGN KEY (`company_id`) REFERENCES `base_company` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `stock_stockwarehouse_province_id_e399e93d_fk_base_province_id` FOREIGN KEY (`province_id`) REFERENCES `base_province` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
