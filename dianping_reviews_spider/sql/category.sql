/*
 Navicat Premium Data Transfer
 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : dianping_reviews_db
 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001
 Date: 21/04/2018 20:45:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category`  (
  `index` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `category` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`index`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('0', '不限', 'http://www.dianping.com/chengdu/ch10/g110');
INSERT INTO `category` VALUES ('1', '四川火锅', 'http://www.dianping.com/chengdu/ch10/g3023');
INSERT INTO `category` VALUES ('10', '焖锅', 'http://www.dianping.com/chengdu/ch10/g34065');
INSERT INTO `category` VALUES ('11', '豆捞', 'http://www.dianping.com/chengdu/ch10/g32712');
INSERT INTO `category` VALUES ('12', '打边炉/港式火锅', 'http://www.dianping.com/chengdu/ch10/g34063');
INSERT INTO `category` VALUES ('13', '日韩火锅', 'http://www.dianping.com/chengdu/ch10/g34062');
INSERT INTO `category` VALUES ('14', '蒸汽火锅', 'http://www.dianping.com/chengdu/ch10/g34066');
INSERT INTO `category` VALUES ('15', '粥底火锅', 'http://www.dianping.com/chengdu/ch10/g34064');
INSERT INTO `category` VALUES ('2', '川味火锅/麻辣火锅', 'http://www.dianping.com/chengdu/ch10/g34060');
INSERT INTO `category` VALUES ('3', '鱼火锅', 'http://www.dianping.com/chengdu/ch10/g3027');
INSERT INTO `category` VALUES ('4', '干锅', 'http://www.dianping.com/chengdu/ch10/g4345');
INSERT INTO `category` VALUES ('5', '汤锅', 'http://www.dianping.com/chengdu/ch10/g4273');
INSERT INTO `category` VALUES ('6', '自助火锅', 'http://www.dianping.com/chengdu/ch10/g34061');
INSERT INTO `category` VALUES ('7', '老北京火锅', 'http://www.dianping.com/chengdu/ch10/g208');
INSERT INTO `category` VALUES ('8', '小火锅', 'http://www.dianping.com/chengdu/ch10/g4477');
INSERT INTO `category` VALUES ('9', '芋儿鸡', 'http://www.dianping.com/chengdu/ch10/g32713');

SET FOREIGN_KEY_CHECKS = 1;