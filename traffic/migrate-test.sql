BEGIN;
--
-- Create model Closed_roads
--
CREATE TABLE `traffic_closed_roads` (`perm_no` integer UNSIGNED NOT NULL PRIMARY KEY, `type` smallint NOT NULL, `location` varchar(100) NOT NULL, `neighbor` varchar(100) NOT NULL, `lat` double precision NOT NULL, `lng` double precision NOT NULL, `note` varchar(500) NOT NULL, `start_date` date NOT NULL, `end_date` date NOT NULL, `wkday_hrs` varchar(30) NOT NULL, `wkend_hrs` varchar(30) NOT NULL, `wkday_hrsfull` varchar(50) NOT NULL, `wkend_hrsfull` varchar(50) NOT NULL, `backfill` bool NOT NULL, `coordinate` bool NOT NULL, `traffic_ctl` bool NOT NULL, `closure` bool NOT NULL, `onelane` bool NOT NULL, `postno` bool NOT NULL, `pat` bool NOT NULL, `ctl_plan` bool NOT NULL, `emerge` bool NOT NULL, `buss` bool NOT NULL, `ped_clean` bool NOT NULL, `off_police` bool NOT NULL, `flagper` bool NOT NULL, `penndot` bool NOT NULL, `rdline` varchar(50000) NOT NULL);
--
-- Create model Counts_sensors
--
CREATE TABLE `traffic_counts_sensors` (`sid` varchar(10) NOT NULL PRIMARY KEY, `coordinates` longtext NOT NULL, `counts` longtext NOT NULL);
--
-- Create model Counts_sensors_links
--
CREATE TABLE `traffic_counts_sensors_links` (`sid` varchar(10) NOT NULL PRIMARY KEY, `coordinates` longtext NOT NULL);
--
-- Create model Crashdata
--
CREATE TABLE `traffic_crashdata` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Cnty` smallint NOT NULL, `First` smallint NOT NULL, `Severe` smallint NOT NULL, `Weather` smallint NOT NULL, `Roadcon` smallint NOT NULL, `Y2010` smallint NOT NULL, `Y2011` smallint NOT NULL, `Y2012` smallint NOT NULL, `Y2013` smallint NOT NULL, `Y2014` smallint NOT NULL, `Ypre` double precision NOT NULL, `Ystd` double precision NOT NULL);
--
-- Create model GIS_links
--
CREATE TABLE `traffic_gis_links` (`link_id` varchar(20) NOT NULL PRIMARY KEY, `miles` double precision NOT NULL, `from_node` varchar(10) NOT NULL, `to_node` varchar(10) NOT NULL, `s_lon` double precision NOT NULL, `s_lat` double precision NOT NULL, `e_lon` double precision NOT NULL, `e_lat` double precision NOT NULL, `geometries` longtext NOT NULL);
--
-- Create model GTFS_calendar
--
CREATE TABLE `traffic_gtfs_calendar` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `service_id` varchar(50) NOT NULL, `monday` varchar(1) NOT NULL, `tuesday` varchar(1) NOT NULL, `wednesday` varchar(1) NOT NULL, `thursday` varchar(1) NOT NULL, `friday` varchar(1) NOT NULL, `saturday` varchar(1) NOT NULL, `sunday` varchar(1) NOT NULL, `start_date` date NOT NULL, `end_date` date NOT NULL, `GTFS` varchar(50) NOT NULL);
--
-- Create model Incidents
--
CREATE TABLE `traffic_incidents` (`eventid` varchar(15) NOT NULL PRIMARY KEY, `st_rt_no` smallint UNSIGNED NOT NULL, `sr` varchar(255) NOT NULL, `cause` varchar(25) NOT NULL, `status` varchar(20) NOT NULL, `close_date` date NOT NULL, `close_time` time(6) NOT NULL, `open_date` date NOT NULL, `open_time` time(6) NOT NULL, `s_lat` double precision NOT NULL, `s_lon` double precision NOT NULL, `e_lat` double precision NOT NULL, `e_lon` double precision NOT NULL, `geoJson` longtext NOT NULL);
--
-- Create model Link
--
--
-- Create model Meter
--
CREATE TABLE `traffic_meter` (`mid` varchar(20) NOT NULL PRIMARY KEY, `street_name` varchar(20) NOT NULL, `block` varchar(5) NOT NULL, `latitude` double precision NOT NULL, `longitude` double precision NOT NULL);
--
-- Create model PAcounty
--
CREATE TABLE `traffic_pacounty` (`county_code` integer NOT NULL PRIMARY KEY, `county_name` varchar(100) NOT NULL);
--
-- Create model Parking
--
CREATE TABLE `traffic_parking` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `weekday` varchar(3) NOT NULL, `occupancy` longtext NOT NULL, `meter_id` varchar(20) NOT NULL);
--
-- Create model Parking_lots
--
CREATE TABLE `traffic_parking_lots` (`lot_id` smallint UNSIGNED NOT NULL PRIMARY KEY, `name` varchar(100) NOT NULL, `max_spots` smallint UNSIGNED NOT NULL, `lon` double precision NOT NULL, `lat` double precision NOT NULL);
--
-- Create model PAroad
--
CREATE TABLE `traffic_paroad` (`pid` integer NOT NULL PRIMARY KEY, `street_name` varchar(100) NOT NULL, `Cnty` smallint NOT NULL, `First` smallint NOT NULL, `length` varchar(10) NOT NULL, `coordinate` longtext NOT NULL);
--
-- Create model Permissions
--
CREATE TABLE `traffic_permissions` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
--
-- Create model Philly_congestion
--
--
-- Create model Philly_congestion_array
--
--
-- Create model Philly_congestion_array_online
--
--
-- Create model Philly_DMS
--
--
-- Create model Philly_link
--
--
-- Create model Philly_online_loading
--
--
-- Create model Philly_request
--
--
-- Create model Real_time_tmc_data
--
CREATE TABLE `traffic_real_time_tmc_data` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `tmc` varchar(9) NOT NULL, `date` date NOT NULL, `time` time(6) NOT NULL, `speed` double precision NOT NULL, `avg_speed` double precision NOT NULL, `ref_speed` double precision NOT NULL, `delta` smallint NOT NULL, `score` smallint NOT NULL, `c_value` smallint NOT NULL, `travel_time` double precision NOT NULL, `cong_level` smallint NOT NULL);
--
-- Create model Route
--
CREATE TABLE `traffic_route` (`route_id` varchar(10) NOT NULL PRIMARY KEY, `agency_id` varchar(10) NOT NULL, `short_name` varchar(5) NOT NULL UNIQUE, `long_name` varchar(50) NOT NULL, `inbound_stops_geoJson` longtext NOT NULL, `route_type` varchar(1) NOT NULL, `outbound_stops_geoJson` longtext NOT NULL, `inbound_geoJson` longtext NOT NULL, `outbound_geoJson` longtext NOT NULL);
--
-- Create model Route_dict
--
CREATE TABLE `traffic_route_dict` (`short_name` varchar(5) NOT NULL PRIMARY KEY, `route_number_in_APCAVL` varchar(5) NOT NULL UNIQUE);
--
-- Create model SPCCorridorNodeInfo
--
CREATE TABLE `traffic_spccorridornodeinfo` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Corridor_Number` smallint UNSIGNED NOT NULL, `Corridor_Name` varchar(50) NOT NULL, `Node_Number` varchar(5) NOT NULL, `Node_Name` varchar(50) NOT NULL, `Latitude` double precision NOT NULL, `Longitude` double precision NOT NULL);
--
-- Create model SPCCorridorNodeInfo2013to2015
--
CREATE TABLE `traffic_spccorridornodeinfo2013to2015` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Corridor_Number` smallint UNSIGNED NOT NULL, `Corridor_Name` varchar(50) NOT NULL, `Node_Number` varchar(5) NOT NULL, `Node_Name` varchar(50) NOT NULL, `Latitude` double precision NOT NULL, `Longitude` double precision NOT NULL);
--
-- Create model SPCtraveltime
--
CREATE TABLE `traffic_spctraveltime` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Year` smallint UNSIGNED NOT NULL, `Corridor_Number` smallint UNSIGNED NOT NULL, `Start_Node` varchar(50) NOT NULL, `End_Node` varchar(50) NOT NULL, `AM_Peak_Hour_Volume` smallint UNSIGNED NOT NULL, `PM_Peak_Hour_Volume` smallint UNSIGNED NOT NULL, `Speed_Limit` smallint UNSIGNED NOT NULL, `Distance` double precision NOT NULL, `Travel_Time_At_Posted_Speed_Limit` double precision NOT NULL, `Weighted_Avg_Speed` double precision NOT NULL, `AM_Travel_Time` double precision NOT NULL, `PM_Travel_Time` double precision NOT NULL, `AM_Avg_Speed` double precision NOT NULL, `AM_Weighted_Speed` double precision NOT NULL, `AM_Delay_Per_Vehicle` double precision NOT NULL, `PM_Avg_Speed` double precision NOT NULL, `PM_Weighted_Speed` double precision NOT NULL, `PM_Delay_Per_Vehicle` double precision NOT NULL, `AM_Total_Delay` double precision NOT NULL, `PM_Total_Delay` double precision NOT NULL, `Direction` varchar(5) NOT NULL);
--
-- Create model SPCtraveltime2013to2015
--
CREATE TABLE `traffic_spctraveltime2013to2015` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `Year` smallint UNSIGNED NOT NULL, `Corridor_Number` smallint UNSIGNED NOT NULL, `Start_Node` varchar(50) NOT NULL, `End_Node` varchar(50) NOT NULL, `Time` double precision NOT NULL, `Travel_Time` double precision NOT NULL, `Speed` double precision NOT NULL, `Travel_Time_At_Posted_Speed_Limit` double precision NOT NULL, `Posted_Speed_Limit` smallint UNSIGNED NOT NULL);
--
-- Create model Stop
--
CREATE TABLE `traffic_stop` (`stop_id` varchar(10) NOT NULL PRIMARY KEY, `code` varchar(10) NOT NULL, `name` varchar(60) NOT NULL, `geoJson` longtext NOT NULL, `lat` double precision NOT NULL, `lon` double precision NOT NULL, `zone_id` varchar(5) NOT NULL);
--
-- Create model Stop_route
--
CREATE TABLE `traffic_stop_route` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `stop_id` varchar(10) NOT NULL, `route_id` varchar(10) NOT NULL, `direction` varchar(1) NOT NULL, `order` smallint UNSIGNED NOT NULL);
--
-- Create model Stop_time
--
CREATE TABLE `traffic_stop_time` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `trip_id` varchar(50) NOT NULL, `arrival_time` varchar(8) NOT NULL, `departure_time` varchar(8) NOT NULL, `stop_id` varchar(10) NOT NULL, `stop_sequence` smallint UNSIGNED NOT NULL, `pickup_type` varchar(1) NOT NULL, `drop_off_type` varchar(1) NOT NULL, `GTFS` varchar(50) NOT NULL);
--
-- Create model Street
--
CREATE TABLE `traffic_street` (`sid` varchar(20) NOT NULL PRIMARY KEY, `street_name` varchar(100) NOT NULL, `coordinate` longtext NOT NULL);
--
-- Create model Streetparking
--
CREATE TABLE `traffic_streetparking` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `occupancy` longtext NOT NULL, `street_id` varchar(20) NOT NULL);
--
-- Create model Streetpre
--
CREATE TABLE `traffic_streetpre` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `occupancy` longtext NOT NULL, `street_id` varchar(20) NOT NULL);
--
-- Create model Streetrate
--
CREATE TABLE `traffic_streetrate` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `rate` longtext NOT NULL, `street_id` varchar(20) NOT NULL);
--
-- Create model Streetratepre
--
CREATE TABLE `traffic_streetratepre` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `rate` longtext NOT NULL, `street_id` varchar(20) NOT NULL);
--
-- Create model TMC
--
CREATE TABLE `traffic_tmc` (`tmc` varchar(9) NOT NULL PRIMARY KEY, `road` varchar(50) NOT NULL, `direction` varchar(1) NOT NULL, `intersection` varchar(100) NOT NULL, `state` varchar(2) NOT NULL, `county` varchar(20) NOT NULL, `zip` varchar(5) NOT NULL, `s_lat` double precision NOT NULL, `s_lon` double precision NOT NULL, `e_lat` double precision NOT NULL, `e_lon` double precision NOT NULL, `miles` double precision NOT NULL, `road_order` smallint UNSIGNED NOT NULL, `reference_speed` double precision NOT NULL);
--
-- Create model TMC_data
--
CREATE TABLE `traffic_tmc_data` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `time` time(6) NOT NULL, `speed` double precision NOT NULL, `avg_speed` double precision NOT NULL, `travel_time` double precision NOT NULL, `tmc_id` varchar(9) NOT NULL);
--
-- Create model TMC_Here
--
CREATE TABLE `traffic_tmc_here` (`tmc` varchar(9) NOT NULL PRIMARY KEY, `state` varchar(2) NOT NULL, `county` varchar(20) NOT NULL, `miles` double precision NOT NULL, `road_number` varchar(20) NOT NULL, `road_name` varchar(100) NOT NULL, `lat` double precision NOT NULL, `lon` double precision NOT NULL, `direction` varchar(1) NOT NULL, `coordinates` longtext NOT NULL);
--
-- Create model TMC_Here_data
--
CREATE TABLE `traffic_tmc_here_data` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `epoch` smallint UNSIGNED NOT NULL, `tt_all` smallint UNSIGNED NOT NULL, `tt_pv` smallint UNSIGNED NOT NULL, `tt_ft` smallint UNSIGNED NOT NULL, `spd_all` double precision NOT NULL, `spd_pv` double precision NOT NULL, `spd_ft` double precision NOT NULL, `tmc_id` varchar(9) NOT NULL);
--
-- Create model TMC_real_time
--
CREATE TABLE `traffic_tmc_real_time` (`tmc` varchar(9) NOT NULL PRIMARY KEY, `road` varchar(50) NOT NULL, `direction` varchar(1) NOT NULL, `intersection` varchar(100) NOT NULL, `state` varchar(2) NOT NULL, `county` varchar(20) NOT NULL, `zip` varchar(5) NOT NULL, `s_lat` double precision NOT NULL, `s_lon` double precision NOT NULL, `e_lat` double precision NOT NULL, `e_lon` double precision NOT NULL, `miles` double precision NOT NULL, `road_order` smallint UNSIGNED NOT NULL, `reference` double precision NOT NULL, `speed` double precision NOT NULL, `average` double precision NOT NULL, `ttm` double precision NOT NULL, `congestion` smallint UNSIGNED NOT NULL);
--
-- Create model TMC_Ritis
--
CREATE TABLE `traffic_tmc_ritis` (`tmc` varchar(9) NOT NULL PRIMARY KEY, `road_name` varchar(50) NOT NULL, `direction` varchar(1) NOT NULL, `intersection` varchar(100) NOT NULL, `state` varchar(2) NOT NULL, `county` varchar(20) NOT NULL, `zip` varchar(5) NOT NULL, `s_lat` double precision NOT NULL, `s_lon` double precision NOT NULL, `e_lat` double precision NOT NULL, `e_lon` double precision NOT NULL, `miles` double precision NOT NULL, `road_order` smallint UNSIGNED NOT NULL, `coordinates` longtext NOT NULL);
--
-- Create model Transit_data
--
CREATE TABLE `traffic_transit_data` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `dow` varchar(1) NOT NULL, `dir` varchar(1) NOT NULL, `route` varchar(4) NOT NULL, `tripa` varchar(4) NOT NULL, `blocka` varchar(10) NOT NULL, `vehnoa` varchar(4) NOT NULL, `date` date NOT NULL, `stopa` smallint UNSIGNED NOT NULL, `qstopa` varchar(8) NOT NULL, `aname` longtext NOT NULL, `hour` smallint UNSIGNED NOT NULL, `minute` smallint UNSIGNED NOT NULL, `second` smallint UNSIGNED NOT NULL, `dhour` smallint UNSIGNED NOT NULL, `dminute` smallint UNSIGNED NOT NULL, `dsecond` smallint UNSIGNED NOT NULL, `on_num` smallint UNSIGNED NOT NULL, `off_num` smallint UNSIGNED NOT NULL, `load_num` smallint UNSIGNED NOT NULL, `dlmiles` double precision NOT NULL, `dlmin` double precision NOT NULL, `dlpmls` double precision NOT NULL, `dwtime` double precision NOT NULL, `delta` smallint UNSIGNED NOT NULL, `schtim` smallint UNSIGNED NOT NULL, `schdev` double precision NOT NULL, `srtime` double precision NOT NULL, `artime` double precision NOT NULL);
--
-- Create model Transit_shape
--
CREATE TABLE `traffic_transit_shape` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `shape_id` varchar(10) NOT NULL, `lat` double precision NOT NULL, `lon` double precision NOT NULL, `sequence` integer UNSIGNED NOT NULL);
--
-- Create model Trip
--
CREATE TABLE `traffic_trip` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `service_id` varchar(35) NOT NULL, `trip_id` varchar(50) NOT NULL, `headsign` varchar(100) NOT NULL, `direction_id` varchar(1) NOT NULL, `block_id` varchar(20) NOT NULL, `shape_id` varchar(10) NOT NULL, `GTFS` varchar(50) NOT NULL, `route_id` varchar(10) NOT NULL);
--
-- Create model TwitterEvents
--
CREATE TABLE `traffic_twitterevents` (`eventid` varchar(15) NOT NULL PRIMARY KEY, `st_rt_no` smallint UNSIGNED NOT NULL, `sr` varchar(255) NOT NULL, `cause` varchar(25) NOT NULL, `status` varchar(20) NOT NULL, `close_date` date NOT NULL, `close_time` time(6) NOT NULL, `open_date` date NOT NULL, `open_time` time(6) NOT NULL, `s_lat` double precision NOT NULL, `s_lon` double precision NOT NULL, `e_lat` double precision NOT NULL, `e_lon` double precision NOT NULL, `geoJson` longtext NOT NULL);
--
-- Create model Weather
--
CREATE TABLE `traffic_weather` (`county` varchar(20) NOT NULL PRIMARY KEY, `state` varchar(2) NOT NULL, `api` varchar(30) NOT NULL, `update_time` time(6) NOT NULL, `geoJson` longtext NOT NULL, `weather` longtext NOT NULL);
--
-- Create model Weather_zipcode
--
CREATE TABLE `traffic_weather_zipcode` (`zipcode` varchar(5) NOT NULL PRIMARY KEY, `geoJson` longtext NOT NULL);
--
-- Create model Weather_zipcode_data
--
CREATE TABLE `traffic_weather_zipcode_data` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `query_time` datetime(6) NOT NULL, `code` smallint UNSIGNED NOT NULL, `timestamp` longtext NOT NULL, `temp` smallint NOT NULL, `text` longtext NOT NULL, `zipcode_id` varchar(5) NOT NULL);
--
-- Alter index_together for tmc_ritis (1 constraint(s))
--
CREATE INDEX `traffic_tmc_ritis_road_name_52ec1382_idx` ON `traffic_tmc_ritis` (`road_name`, `road_order`);
--
-- Alter unique_together for stop_time (1 constraint(s))
--
ALTER TABLE `traffic_stop_time` ADD CONSTRAINT `traffic_stop_time_trip_id_33352328_uniq` UNIQUE (`trip_id`, `stop_sequence`, `GTFS`);
--
-- Alter index_together for stop_time (2 constraint(s))
--
CREATE INDEX `traffic_stop_time_trip_id_9c9bbc16_idx` ON `traffic_stop_time` (`trip_id`, `stop_id`, `GTFS`);
CREATE INDEX `traffic_stop_time_stop_id_deb3b1fd_idx` ON `traffic_stop_time` (`stop_id`, `GTFS`);
--
-- Add field link to philly_congestion_array_online
--
--
-- Add field loading to philly_congestion_array_online
--
--
-- Add field link to philly_congestion_array
--
--
-- Add field request to philly_congestion_array
--
--
-- Add field link to philly_congestion
--
--
-- Add field request to philly_congestion
--
--
-- Alter index_together for incidents (1 constraint(s))
--
CREATE INDEX `traffic_incidents_close_date_004610a4_idx` ON `traffic_incidents` (`close_date`, `close_time`);
--
-- Alter unique_together for gtfs_calendar (1 constraint(s))
--
ALTER TABLE `traffic_gtfs_calendar` ADD CONSTRAINT `traffic_gtfs_calendar_service_id_f69c13e2_uniq` UNIQUE (`service_id`, `GTFS`);
--
-- Add field pid to crashdata
--
ALTER TABLE `traffic_crashdata` ADD COLUMN `pid_id` integer NOT NULL;
ALTER TABLE `traffic_crashdata` ALTER COLUMN `pid_id` DROP DEFAULT;
--
-- Alter unique_together for trip (1 constraint(s))
--
ALTER TABLE `traffic_trip` ADD CONSTRAINT `traffic_trip_trip_id_4fda0093_uniq` UNIQUE (`trip_id`, `GTFS`);
--
-- Alter index_together for trip (1 constraint(s))
--
CREATE INDEX `traffic_trip_route_id_508496c8_idx` ON `traffic_trip` (`route_id`, `GTFS`, `direction_id`);
--
-- Alter index_together for tmc_data (1 constraint(s))
--
CREATE INDEX `traffic_tmc_data_tmc_id_01cfa80e_idx` ON `traffic_tmc_data` (`tmc_id`, `date`, `time`);
--
-- Alter index_together for crashdata (1 constraint(s))
--
CREATE INDEX `traffic_crashdata_Severe_1568ae62_idx` ON `traffic_crashdata` (`Severe`, `Weather`, `Roadcon`, `Cnty`);
CREATE INDEX `traffic_crashdata_7fb55ed0` ON `traffic_crashdata` (`First`);
ALTER TABLE `traffic_parking` ADD CONSTRAINT `traffic_parking_meter_id_f7cecec2_fk_traffic_meter_mid` FOREIGN KEY (`meter_id`) REFERENCES `traffic_meter` (`mid`);
CREATE INDEX `traffic_parking_5fc73231` ON `traffic_parking` (`date`);
CREATE INDEX `traffic_paroad_a8147dfc` ON `traffic_paroad` (`Cnty`);
CREATE INDEX `traffic_paroad_7fb55ed0` ON `traffic_paroad` (`First`);
CREATE INDEX `traffic_stop_route_91455da7` ON `traffic_stop_route` (`stop_id`);
CREATE INDEX `traffic_stop_route_b4347999` ON `traffic_stop_route` (`route_id`);
ALTER TABLE `traffic_streetparking` ADD CONSTRAINT `traffic_streetparking_street_id_7a067db7_fk_traffic_street_sid` FOREIGN KEY (`street_id`) REFERENCES `traffic_street` (`sid`);
CREATE INDEX `traffic_streetparking_5fc73231` ON `traffic_streetparking` (`date`);
ALTER TABLE `traffic_streetpre` ADD CONSTRAINT `traffic_streetpre_street_id_5614d93e_fk_traffic_street_sid` FOREIGN KEY (`street_id`) REFERENCES `traffic_street` (`sid`);
CREATE INDEX `traffic_streetpre_5fc73231` ON `traffic_streetpre` (`date`);
ALTER TABLE `traffic_streetrate` ADD CONSTRAINT `traffic_streetrate_street_id_00d89b00_fk_traffic_street_sid` FOREIGN KEY (`street_id`) REFERENCES `traffic_street` (`sid`);
CREATE INDEX `traffic_streetrate_5fc73231` ON `traffic_streetrate` (`date`);
ALTER TABLE `traffic_streetratepre` ADD CONSTRAINT `traffic_streetratepre_street_id_a7f66ffa_fk_traffic_street_sid` FOREIGN KEY (`street_id`) REFERENCES `traffic_street` (`sid`);
CREATE INDEX `traffic_streetratepre_5fc73231` ON `traffic_streetratepre` (`date`);
CREATE INDEX `traffic_tmc_3c68cbe4` ON `traffic_tmc` (`road`);
ALTER TABLE `traffic_tmc_data` ADD CONSTRAINT `traffic_tmc_data_tmc_id_e082a6f7_fk_traffic_tmc_tmc` FOREIGN KEY (`tmc_id`) REFERENCES `traffic_tmc` (`tmc`);
ALTER TABLE `traffic_tmc_here_data` ADD CONSTRAINT `traffic_tmc_here_data_tmc_id_f8114462_fk_traffic_tmc_here_tmc` FOREIGN KEY (`tmc_id`) REFERENCES `traffic_tmc_here` (`tmc`);
CREATE INDEX `traffic_tmc_here_data_5fc73231` ON `traffic_tmc_here_data` (`date`);
CREATE INDEX `traffic_tmc_real_time_3c68cbe4` ON `traffic_tmc_real_time` (`road`);
CREATE INDEX `traffic_tmc_ritis_77dc3286` ON `traffic_tmc_ritis` (`road_name`);
CREATE INDEX `traffic_transit_shape_644311d9` ON `traffic_transit_shape` (`shape_id`);
ALTER TABLE `traffic_trip` ADD CONSTRAINT `traffic_trip_route_id_a71f2c98_fk_traffic_route_route_id` FOREIGN KEY (`route_id`) REFERENCES `traffic_route` (`route_id`);
ALTER TABLE `traffic_weather_zipcode_data` ADD CONSTRAINT `traffic_w_zipcode_id_4c9f5be4_fk_traffic_weather_zipcode_zipcode` FOREIGN KEY (`zipcode_id`) REFERENCES `traffic_weather_zipcode` (`zipcode`);
CREATE INDEX `traffic_crashdata_252a6649` ON `traffic_crashdata` (`pid_id`);
ALTER TABLE `traffic_crashdata` ADD CONSTRAINT `traffic_crashdata_pid_id_2961eb9f_fk_traffic_paroad_pid` FOREIGN KEY (`pid_id`) REFERENCES `traffic_paroad` (`pid`);

COMMIT;
